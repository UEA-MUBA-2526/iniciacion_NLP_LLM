# Iniciación a NLP, LLMs, RAG, Reranking y Agentes

Repositorio de entrega del curso **LLMs y Aplicaciones de IA**. Documenta una progresión completa desde los fundamentos de procesamiento de lenguaje natural hasta arquitecturas avanzadas de **Retrieval-Augmented Generation (RAG)**, **Reranking** y **Agentes** (LangChain + LangGraph).

| Área | Contenido |
|------|-----------|
| Teoría y demos guiadas | [`notebook/`](notebook/) — 13 notebooks numerados (00–12) |
| Ejercicios resueltos | [`exercises/`](exercises/) — Actividades prácticas alineadas con cada módulo |
| Guía de ejecución | [`RUN.md`](RUN.md) — Orden recomendado, comandos y limitaciones |
| Control de calidad | [`QUALITY_GATE.md`](QUALITY_GATE.md) — 10 casos de prueba manuales y mitigaciones |

---

## Descripción del proyecto

El repositorio implementa y explica un sistema de QA aumentado por recuperación que evoluciona en complejidad a través de notebooks ejecutables:

1. **Fundamentos NLP** — Tokenización, embeddings clásicos y con transformers.
2. **Prompting y chatbots** — Ingeniería de prompts y conversación con LLMs (Groq).
3. **Retrieval** — Vector stores (FAISS), chunking y búsqueda semántica.
4. **RAG** — Ensamblaje contexto + generación con LangChain.
5. **Reranking** — Segunda etapa con Cross-Encoder y reranking asistido por LLM.
6. **Agentes** — Tool use, ReAct y flujos con LangGraph.
7. **Agentic RAG** — Clasificación, reformulación, verificación y auto-corrección en grafo.
8. **Multimodalidad** — Introducción a modelos de contexto extendido y visión-lenguaje.

La **entrega evaluable** consiste en los notebooks teóricos (`notebook/`), sus ejercicios resueltos (`exercises/`) y la documentación de ejecución y calidad.

---

## Requisitos del sistema

| Requisito | Detalle |
|-----------|---------|
| **SO** | Windows 10/11, macOS 12+, o Linux (64-bit) |
| **Python** | 3.12 – 3.14 (recomendado 3.12) |
| **RAM** | Mínimo 8 GB; recomendado 16 GB |
| **Disco** | ~4 GB libres (PyTorch, TensorFlow, modelos Hugging Face) |
| **Red** | Conexión a internet (descarga de modelos, API Groq) |
| **API Key** | Cuenta gratuita en [console.groq.com](https://console.groq.com) → `GROQ_API_KEY` |

> Los notebooks 00–02 pueden ejecutarse sin API key. A partir del módulo 03 se requiere `GROQ_API_KEY`.

---

## Instalación

```bash
git clone <url-del-repositorio>
cd iniciacion_NLP_LLM
python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name=iniciacion-nlp-llm
```

Configura la API key (los notebooks también pueden pedirla con `getpass`):

```bash
copy .env.example .env   # Windows
# cp .env.example .env   # Linux/macOS
# Editar .env → GROQ_API_KEY=gsk_...
```

Alternativa con Poetry: `poetry install` (ver `pyproject.toml`).

---

## Inicio rápido

```bash
jupyter lab
```

Ruta mínima recomendada para evaluar el hilo **RAG → Reranking → Agentes**:

| Paso | Notebook | Ejercicio |
|------|----------|-----------|
| 1 | `06_Introduccion_RAG.ipynb` | `EX_06_Introduccion_RAG.ipynb` |
| 2 | `07_Reranking_Optimizacion.ipynb` | `EX_07_Reranking_Optimizacion.ipynb` |
| 3 | `08_Introduccion_Agentes.ipynb` | `EX_08_Introduccion_Agentes.ipynb` |
| 4 | `09_Agentes_LangChain.ipynb` | `EX_09_Agentes_LangChain.ipynb` |
| 5 | `10_LangGraph_Flujos.ipynb` | `EX_10_LangGraph_Flujos.ipynb` |
| 6 | `11_RAG_Avanzado_Agentico.ipynb` | `EX_11_RAG_Avanzado_Agentico.ipynb` |

Detalle completo del orden de ejecución: **[RUN.md](RUN.md)**.

---

## Estructura del repositorio

```
iniciacion_NLP_LLM/
├── notebook/           # Material teórico (00–12)
├── exercises/          # Ejercicios resueltos (EX_00–EX_12)
├── requirements.txt
├── pyproject.toml
├── .env.example
├── RUN.md
├── QUALITY_GATE.md
└── README.md
```

---

## Control de calidad

Antes de entregar o evaluar, revisar **[QUALITY_GATE.md](QUALITY_GATE.md)**:

- Tabla de **10 casos de prueba manuales** (in-domain, OOD, reranking, agentes, API key, etc.).
- **4 fallos críticos** documentados con estrategias de mitigación.
- Checklist pre-entrega.

---

## Autoría y licencia

Curso de LLMs y Aplicaciones de IA — MIT License (ver `pyproject.toml`).
