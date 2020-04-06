FROM alpine:latest

## DEBUG DOCKERFILE FILE WITH PRIVILEGED USER ## 

ENV GID=1001 \
    GNAME=group \
    UID=1001 \
    UNAME=user

# set -x: print commands and their outputs
RUN set -x && \
    apk --update add bash vim tzdata && \
    addgroup -g $GID -S $GNAME && \
    adduser -S -D -H -u $UID -h $HOME -s /sbin/nologin -G $GNAME -g $GNAME $UNAME && \
    #<<<< only for debugging # \
    apk add --no-cache sudo && \
    echo "$UNAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    #>>>> only for debugging # \
    #unlink /usr/bin/env && \
    #unlink /usr/bin/top && \
    #unlink /bin/ps && \
    echo user was created

# create image with right timezone for Vienna
ARG TZ=Europe/Vienna
RUN touch "/etc/timezone" && \
    ln -sf "/usr/share/zoneinfo/$TZ" /etc/localtime && \
    echo "$TZ" > /etc/timezone

RUN echo Hello world

#ENTRYPOINT ["/bin/bash"]
#CMD ["-x","/start-mysql.sh"]

