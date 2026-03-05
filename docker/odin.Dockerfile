FROM homebrew/brew:master

RUN brew install odin
RUN odin version
