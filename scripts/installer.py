import asyncio
import json
import re

import aiohttp


async def fetch(session, url, **kwargs):
    async with session.get(url, **kwargs) as r:
        return await r.json() if "json" in r.content_type else await r.text()


async def get_versions():
    async with aiohttp.ClientSession() as s:
        tasks = {
            "node": fetch(s, "https://nodejs.org/dist/index.json"),
            "bun": fetch(s, "https://api.github.com/repos/oven-sh/bun/releases/latest"),
            "deno": fetch(
                s, "https://api.github.com/repos/denoland/deno/releases/latest"
            ),
            "zig": fetch(s, "https://ziglang.org/download/index.json"),
            "rust": fetch(
                s, "https://static.rust-lang.org/dist/channel-rust-stable.toml"
            ),
            "c3": fetch(s, "https://api.github.com/repos/c3lang/c3c/releases/latest"),
            "odin": fetch(
                s, "https://api.github.com/repos/odin-lang/Odin/releases/latest"
            ),
            "gcc": fetch(s, "https://api.github.com/repos/gcc-mirror/gcc/tags"),
            "clang": fetch(
                s, "https://api.github.com/repos/llvm/llvm-project/releases/latest"
            ),
            "java": fetch(s, "https://api.adoptium.net/v3/info/available_releases"),
            "go": fetch(s, "https://go.dev/dl/?mode=json"),
        }
        results = await asyncio.gather(*tasks.values(), return_exceptions=True)
        raw = dict(zip(tasks.keys(), results))

    versions = {}

    versions["NODE"] = raw["node"][0]["version"].lstrip("v")
    versions["BUN"] = raw["bun"]["tag_name"].lstrip("v")
    versions["DENO"] = raw["deno"]["tag_name"].lstrip("v")
    versions["ZIG"] = next(
        k for k in raw["zig"] if k != "master"
    )  # latest stable e.g. "0.13.0"

    # Rust: parse TOML for version line
    rust_match = re.search(r'^version = "(.+)"', raw["rust"], re.MULTILINE)
    versions["RUST"] = rust_match.group(1)

    versions["C3"] = raw["c3"]["tag_name"].lstrip("v")
    versions["ODIN"] = raw["odin"]["tag_name"]  # e.g. dev-2024-11

    # GCC: find latest release tag like releases/gcc-14.2.0
    gcc_tags = [
        t["name"]
        for t in raw["gcc"]
        if re.match(r"releases/gcc-\d+\.\d+\.\d+$", t["name"])
    ]
    versions["GCC"] = gcc_tags[0].replace("releases/gcc-", "")

    versions["CLANG"] = raw["clang"]["tag_name"].lstrip("llvmorg-")
    versions["JAVA"] = str(raw["java"]["most_recent_lts"])  # e.g. "21"
    versions["GO"] = raw["go"][0]["version"].replace("go", "")

    return versions


if __name__ == "__main__":
    versions = asyncio.run(get_versions())

    # Write as Docker build args
    with open(".toolchain.env", "w") as f:
        for k, v in versions.items():
            print(f"{k}={v}")
            f.write(f"{k}={v}\n")

    # Also write as JSON for GH Actions matrix or other tooling
    with open("versions.json", "w") as f:
        json.dump(versions, f, indent=2)
