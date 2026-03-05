FROM llvm-base:latest

RUN brew install zig
RUN zig version
