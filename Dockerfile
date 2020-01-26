FROM python:3.7-slim AS builder

WORKDIR /root

RUN apt-get -qq update && apt-get -qq install --no-install-recommends build-essential

RUN python -m venv venv
ENV PATH="/root/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.7-slim

RUN useradd -u 12345 -m launcher
WORKDIR /home/launcher
COPY --chown=launcher:launcher --from=builder /root/venv /home/launcher/venv

ENV PATH="/home/launcher/venv/bin:$PATH"

# Default SMTP config  set to Gmail
ENV SMTP_SERVER="smtp.gmail.com"
ENV SMTP_PORT="587"

COPY --chown=launcher:launcher ip_change.py .

USER launcher
ENTRYPOINT ["python", "ip_change.py"]
CMD ["-h"]
