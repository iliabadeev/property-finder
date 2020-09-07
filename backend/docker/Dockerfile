# Python base. Recommended by https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.7-buster

# Copy all working files into container
COPY ./ /app
# Change working directory
WORKDIR /app
# Install dependencies
RUN pip install -r /app/requirements.txt

# Args
ARG PRODUCTION_BUILD
ARG WORKERS=1
ARG HOST='0.0.0.0'
ARG PORT=5000
# If not production build -> make interactive
ARG INTERACTIVITY='--reload --log-level debug'
ENV GUNICORN_CMD_ARGS="-w $WORKERS -b $HOST:$PORT $INTERACTIVITY"

# Run
EXPOSE 5000
ENTRYPOINT ["gunicorn", "wsgi:server"]
