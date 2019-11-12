FROM alpine:latest

# create image with right timezone for Vienna
#ARG TZ=Europe/Vienna
#RUN touch "/etc/timezone" && \
#    ln -sf "/usr/share/zoneinfo/$TZ" /etc/localtime && \
#    echo "$TZ" > /etc/timezone


RUN echo Hello world
