FROM homebrew/brew:master

RUN brew install c3c
RUN c3c --version
