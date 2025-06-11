FROM caddy:latest

WORKDIR /etc/caddy

RUN apk add --no-cache curl && \
    apk add --no-cache envsubst

COPY Caddyfile.tmpl Caddyfile.tmpl

RUN envsubst < Caddyfile.tmpl > Caddyfile && \
    rm Caddyfile.tmpl

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f -s http://localhost/status/ || exit 1