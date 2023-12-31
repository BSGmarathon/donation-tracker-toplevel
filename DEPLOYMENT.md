# How to deploy this package
Because I am lazy and do not want to write a lot of documentation, I'm just gonna give you my docker compose file running in portainer. Have fun

```yaml
version: '3.9'
services:
  tracker:
    image: ghcr.io/bsgmarathon/tracker:latest
    restart: always
    networks:
      - caddy
    volumes:
      - "tracker_db:/app/tracker_development/db:rw"
      - "static:/var/www/html/static:rw"
    # you have to supply this yourself
    configs:
      - source: local.py
        target: /app/tracker_development/tracker_development/local.py

  # We assume that you use caddy as normal, just here for illustrations
  caddy:
    image: lucaslorentz/caddy-docker-proxy:ci-alpine
    ports:
      - "80:80"
      - "443:443"
    environment:
      - CADDY_INGRESS_NETWORKS=caddy
      - CADDY_DOCKER_CADDYFILE_PATH=
    labels:
      caddy.email: john.doe@example.com
    networks:
      - caddy
    volumes:
      - data:/data
      - /var/run/docker.sock:/var/run/docker.sock
      - tracker_static:/var/tracker/static:ro
    deploy:
      placement:
        constraints:
          - node.role == manager
      replicas: 1
      restart_policy:
        condition: any
      resources:
        reservations:
          cpus: '0.2'
          memory: 400M

configs:
  local.py:
    name: tracker.local.py_v9
    external: true

volumes:
  static: { }
  tracker_db:
    external: true
  data:
    name: caddy_data
    driver: local

networks:
  caddy:
    name: caddy
```

And the caddyfile that is used. As you can see, static files are served through caddy
```caddyfile
tracker.bsgmarathon.com {
  reverse_proxy tracker_app:8000

  handle_path /static/* {
    root * /var/tracker/static
    file_server
  }
}
```