FROM caddy:latest

WORKDIR /etc/caddy

RUN apk add --no-cache curl envsubst && \
	rm -rf /var/cache/apk/* /lib/apk/db/scripts.tar

COPY Caddyfile.tmpl Caddyfile.tmpl
