FROM caddy:latest

WORKDIR /etc/caddy

COPY Caddyfile Caddyfile

RUN apk add --no-cache curl

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f -s http://localhost/status/ || exit 1