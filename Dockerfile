FROM python:3.10-slim-bullseye

# Environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Work directory
WORKDIR /newsletter-manager

# Dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .