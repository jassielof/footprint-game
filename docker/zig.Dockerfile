FROM fedora:latest

RUN dnf install -y curl bash unzip tar

# RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal --default-toolchain stable
# ENV PATH="/root/.cargo/bin:${PATH}"
# RUN rustup default stable
# RUN cargo --version
# RUN rustc --version


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
