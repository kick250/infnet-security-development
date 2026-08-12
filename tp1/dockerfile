FROM python:3.12

WORKDIR /web/app

ENTRYPOINT [ "/bin/bash", "/web/docker-entrypoint.sh" ]
CMD ["fastapi", "dev", "--host", "0.0.0.0", "--port", "3000"]