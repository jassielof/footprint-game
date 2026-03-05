FROM llvm-base:latest

RUN brew install c3c
RUN c3c --version
