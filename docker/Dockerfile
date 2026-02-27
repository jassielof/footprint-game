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

COPY --from=node:latest /usr/local/bin/node /usr/local/bin/node
COPY --from=node:latest /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY --from=node:latest /usr/local/bin/npm /usr/local/bin/npm
COPY --from=node:latest /usr/local/bin/npx /usr/local/bin/npx

COPY --from=php:latest /usr/local/bin/php /usr/local/bin/

COPY --from=mcr.microsoft.com/dotnet/sdk:latest /usr/share/dotnet /usr/share/dotnet
ENV DOTNET_ROOT=/usr/share/dotnet
ENV PATH="${DOTNET_ROOT}:${PATH}"
RUN dotnet --version
RUN dotnet --info

RUN curl -fsSL https://install.julialang.org | sh
RUN juliaup update
RUN julia --version

COPY --from=nimlang/nim:latest /opt/nim /opt/nim
ENV PATH="/opt/nim/bin:${PATH}"
RUN nim --version

COPY --from=golang:latest /usr/local/go /usr/local/go
ENV PATH="/usr/local/go/bin:${PATH}"
RUN go version

COPY --from=ruby:latest /usr/local /usr/local
RUN ruby --version
RUN gem --version

COPY --from=haskell:latest /usr/local /usr/local
RUN ghc --version
