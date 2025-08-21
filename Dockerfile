# -------- 빌더 스테이지 --------
FROM python:3.11-slim as builder

WORKDIR /app

RUN pip install uv

COPY requirements.txt .

RUN uv venv --python=/usr/local/bin/python && \
    uv pip install --requirement requirements.txt

# -------- 런타임 스테이지 --------
FROM python:3.11-slim

# ❗ 빌더와 같은 경로로 설정
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# ❗ .venv는 /app/.venv 로 복사
COPY --from=builder /app/.venv /app/.venv
COPY . .

EXPOSE 8000

# uvicorn을 PATH에서 실행 (이제 PATH에 /app/.venv/bin 이 들어 있음)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]