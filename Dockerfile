# Use official Python base image
FROM python:3.11-slim

ENV DOCKER_HEADLESS=1

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install system dependencies for Playwright browsers
RUN apt-get update && \
    apt-get install -y \
        wget gnupg curl unzip \
        libglib2.0-0 libnss3 libfontconfig1 \
        libxss1 libgtk-3-0 libasound2 \
        xvfb libx11-xcb1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Install Python dependencies
RUN pip install -r requirements.txt
RUN pip install pytest pytest-html

# Install Playwright browsers
RUN playwright install

# Default command using xvfb so headful browser works in Docker#CMD ["pytest", "--html=report.html", "--self-contained-html"]
