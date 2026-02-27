FROM fedora:latest

RUN dnf install -y curl bash unzip tar

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal --default-toolchain stable
ENV PATH="/root/.cargo/bin:${PATH}"
RUN rustup default stable
RUN cargo --version
RUN rustc --version

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv --version
RUN uvx --version

COPY --from=denoland/deno:bin /deno /usr/local/bin/deno
RUN deno --version

RUN curl -fsSL https://bun.com/install | bash
ENV PATH="/root/.bun/bin:${PATH}"
RUN bun --version
RUN bunx --version

RUN curl -o- https://fnm.vercel.app/install | bash -s -- --install-dir /fnm
ENV PATH="/fnm:${PATH}"
RUN fnm --version
RUN eval "$(fnm env)"
RUN fnm install --latest
ENV PATH="/fnm/versions/node/$(fnm current)/bin:${PATH}"
RUN node --version
RUN npm --version

COPY --from=php:latest /usr/local/bin/php /usr/local/bin/

RUN https://dot.net/v1/dotnet-install.sh | bash -s -- --install-dir /dotnet
ENV DOTNET_ROOT=/dotnet
ENV PATH="/dotnet/tools:${PATH}"
ENV PATH="/dotnet:${PATH}"
RUN dotnet --version
RUN dotnet tool --help

RUN curl -fsSL https://install.julialang.org | sh
RUN juliaup update
RUN julia --version

