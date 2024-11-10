FROM mysql:5.7

COPY data.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

VOLUME ["/backup/"]