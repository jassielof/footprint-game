FROM homebrew/brew:master

RUN brew install gleam
RUN gleam --version
