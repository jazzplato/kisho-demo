FROM python:3.9.1

# create and set working directory
WORKDIR /django
COPY ./kisho /django
COPY ./wait_for.py ./
COPY ./requirements.txt ./

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV PORT=8080

# Install project dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN groupadd -r django && useradd -r -g django django
RUN chown -R django .

EXPOSE 8080
HEALTHCHECK --interval=10m --timeout=5s \
    CMD curl -f http://localhost:$PORT/cinema/health/ || exit 1

USER django
CMD gunicorn kisho.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --timeout 300