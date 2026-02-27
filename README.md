# Footprint game

## Rules

### Strictly required

- **Output:** Attempt to print `Hello, world!`followed by a newline to the standard output. Error handling for the output is optional and at the implementer's discretion. The benchmark runs in a controlled CI environment where the output is expected to be successful, so the focus is on the footprint rather than error handling.
- **Exit code:** Exit with code 0 or the platform's equivalent success code under normal execution. The program must not intentionally exit with a non-zero code.
- **Output destination:** Standard output (`stdout`) only, not standard error (`stderr`).
- **Size measurement:** Measured via Python's `os.path.getsize()` for cross-platform consistency.

Other than that, regarding logic or implementation:

- It should be labeled respectively when:
  - Using system calls or not
  - Using assembly or not
  - Linking or not (static or dynamic)

Everything is allowed.

## Languages

Obviously would be fun to include all possible languages, but there are compiled to machine (AOT) and non-compiled (JIT, interpreted, etc.). So there we have some subcategories.

- Compiled to machine code or ahead of time.
- Generally non-compiled.

### Compiled languages

These include:

- C/C++ (GNU, LLVM, MSVC)
- Rust
- Zig
- Go
- D
- Nim
- Odin
- C3
- etc.

### Non-compiled languages

These include:

- Python
- JS/TS (Node, Deno, Bun)
- C# (.NET)
- Java
- Kotlin

### Versions

Any latest version available, we could consider only stable versions or LTS, but languages that aren't generally available or stable (pre-1.0) can't really be comparable, thus, whenever possible it'll be used the latest available (stable, non preview or similar).

## Build and compilation

Mainly via the compiler directly whenever possible, if one has to add the build system orchestrator, a label should be added to it, only if the build system is strictly required, for example prior .NET 10 it required an external tool to run C# directly as scripts, now with .NET 10, it can be done directly with `dotnet run` without the need of a project file.

### Optimization and modes

If a compiler/project can be built with different modes, each combination mix should be labeled.

Languages like C#, have it weirdly, for example, one can build it normally, which becomes runtime dependent, or publish it as a self-contained (which bundles its runtime along with it), or AOT mode, or trimmed, etc.

If possible, each combination, should be registered and tracked. Only if it's not too much work or added complexity.

## Operating system policy

Default: `ubuntu-latest`

With overrides:

- Windows
  - MSVC for C/C++
- MacOS
  - Swift
  - Objective-C/C++

Leaderboards shouldn't compare across different OS (by default, the user could still want to (via jupyter settings)).

## Continuous integration

Just GitHub Actions. I have Pro plan thanks to education, so I get benefits.

The respective job/runner should run automatically only on the affected languages, if the C code is changed or improved, only re-run the C job, and so on. Otherwise it would be a waste of resources and time.

### Jobs structure

Basically one job per toolchain. Each job will be responsible, for those languages requiring special compilers like Microsoft's MSVC or Apple's Swift, they'll have to run on their respective OS.

The CI should obviously be optimized for speed, since it costs money. So caching should be used whenever possible.

## Scripting

For any type of scripting or automation, Python will be used, to not introduce locking to a single platform like Bash or PowerShell, etc.

## Insights

Jupyter will be used for all the insights. And it'll be exported to HTML for GitHub Pages.

## Metadata/labels

Every attempt should be labeled with the following metadata:

- Language: C, Rust, Go, etc.
- Compiler/toolchain: GCC, Clang, MSVC, Zig, Rustc, etc.
- Method: As mentioned in the rules
- OS: Linux, Windows, MacOS
  - Version: Latest, LTS, etc.
- Build mode or optimization level: Debug, Release, etc.
- Notes
