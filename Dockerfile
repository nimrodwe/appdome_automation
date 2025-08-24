# Use official Python base image
FROM python:3.11-slim

ENV DOCKER_HEADLESS=1

# -----------------------------
# Install system dependencies + Java (needed for Jenkins agent)
# -----------------------------
RUN apt-get update && \
    apt-get install -y \
        wget gnupg curl unzip git \
        libglib2.0-0 libnss3 libfontconfig1 \
        libxss1 libgtk-3-0 libasound2 \
        xvfb libx11-xcb1 \
        default-jdk \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# -----------------------------
# Create Jenkins agent user
# -----------------------------
RUN useradd -m -d /home/jenkins jenkins
RUN mkdir -p /home/jenkins/agent && chown -R jenkins:jenkins /home/jenkins/agent

# -----------------------------
# Set working directories
# -----------------------------
WORKDIR /app
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install -r requirements.txt
RUN pip install pytest pytest-html

# Install Playwright browsers
RUN playwright install

# -----------------------------
# Switch to Jenkins user for running as agent
# -----------------------------
USER jenkins
WORKDIR /home/jenkins/agent

# -----------------------------
# Default command (for manual runs; Jenkins overrides this)
# -----------------------------
CMD ["pytest", "/app/tests/", "--html=/app/report.html", "--self-contained-html"]
