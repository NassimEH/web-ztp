FROM python:3.10-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean && \
    apt-get autoremove -y 
    
COPY . .

RUN chmod +x entrypoint.sh

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f -s http://localhost:8000/status/ || exit 1

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
