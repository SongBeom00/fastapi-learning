FROM python:3.12-slim

WORKDIR /app

# uv 설치
RUN pip install uv

# 의존성 파일 복사
COPY pyproject.toml uv.lock ./

# 가상환경 생성 및 의존성 설치 (이 한 줄로 충분합니다)
# 'uv sync'는 pyproject.toml을 읽고 .venv에 의존성을 설치합니다.
RUN uv venv && uv sync --no-cache

# PATH 환경 변수 설정 (매우 중요)
# 컨테이너가 .venv 안의 실행 파일(uvicorn 등)을 찾을 수 있도록 경로를 추가합니다.
ENV PATH="/app/.venv/bin:$PATH"

# 실제 코드 복사
COPY ./app ./app

# 이제 PATH가 설정되었으므로 uvicorn을 바로 호출할 수 있습니다.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]