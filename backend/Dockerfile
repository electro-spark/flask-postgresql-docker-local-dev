FROM --platform=$BUILDPLATFORM python:latest AS builder

# Install packages
RUN mkdir /packages
COPY ./requirements.txt /packages
RUN pip install --no-cache-dir -r /packages/requirements.txt

# Copy app
WORKDIR /app
COPY app /app

# Configure app
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=8000
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 8000

# Start app
CMD ["flask", "run"]
