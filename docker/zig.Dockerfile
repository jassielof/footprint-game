FROM homebrew/brew:master

RUN brew install zig
RUN zig version
