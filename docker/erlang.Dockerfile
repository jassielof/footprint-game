FROM erlang:latest

RUN erl -eval 'io:format("~p~n", [erlang:system_info(otp_release)]), halt().' -noshell
