FROM mongo:latest

COPY init-script.js /docker-entrypoint-initdb.d/

CMD ["mongod", "--bind_ip_all"]