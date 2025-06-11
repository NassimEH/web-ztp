FROM caddy:latest

WORKDIR /etc/caddy

RUN apk add --no-cache curl && \
    apk add --no-cache envsubst

COPY Caddyfile.tmpl Caddyfile.tmpl
