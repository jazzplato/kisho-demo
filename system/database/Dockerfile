FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD=tmp
ENV MYSQL_DATABASE=KishoCinema
ENV MYSQL_USER=kisho
ENV MYSQL_PASSWORD=KishoKurokawa
COPY ./data/ /data/
COPY ./sql_docker/ /docker-entrypoint-initdb.d/