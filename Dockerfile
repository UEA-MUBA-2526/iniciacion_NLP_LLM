# Python 3.13 + JupyterLab + curso (requirements.txt).
# Monta el directorio del proyecto en /workspace para leer y escribir notebooks locales.
FROM python:3.13-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONUNBUFFERED=1

WORKDIR /workspace

# Compilación (gensim, etc.) y bibliotecas usadas por ruedas binarias (matplotlib, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    libgomp1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt && \
    python -m spacy download es_core_news_sm && \
    python -m spacy download en_core_web_sm

EXPOSE 8888

# Sin token por comodidad en uso local; no expongas el puerto a Internet.
CMD jupyter lab \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --ServerApp.allow_root=True \
    --ServerApp.token="" \
    --ServerApp.password="" \
    --ServerApp.root_dir=/workspace
