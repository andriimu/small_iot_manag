# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Specify the Python version to use
ARG PYTHON_VERSION=3.12.0
FROM python:${PYTHON_VERSION}-slim AS base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Set the working directory
RUN mkdir /api_app
WORKDIR /api_app
# Switch to the non-privileged user to run the application.

USER appuser
#Copy requirements
COPY requirements.txt . 
# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/

RUN pip install -r requirements.txt

# Copy the source code into the container.
COPY . .

WORKDIR /api_iot

# Expose the port that the application listens on.
EXPOSE 8080

# Run the application.
CMD ["python", "maintwo.py"]