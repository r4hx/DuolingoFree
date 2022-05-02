FROM python:3.9.12 as builder
WORKDIR /app/
COPY requirements.txt /app/
RUN python3 -m pip install --no-cache-dir --no-warn-script-location --upgrade pip && \
    python3 -m pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*


FROM python:3.9.12-slim
WORKDIR /app/
COPY . .
COPY --from=builder /root/.local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
