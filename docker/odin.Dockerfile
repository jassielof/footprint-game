FROM llvm-base:latest

RUN brew install odin
RUN odin version
