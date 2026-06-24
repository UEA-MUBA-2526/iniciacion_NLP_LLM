# Guía de Ejecución (RUN)

Instrucciones para **evaluadores** y **revisores**. Valida la progresión pedagógica (RAG → Reranking → Agentes) ejecutando notebooks y ejercicios resueltos en Jupyter.

---

## 1. Preparación del entorno

### 1.1 Clonar e instalar

```bash
git clone <url-del-repositorio>
cd iniciacion_NLP_LLM
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
python -m ipykernel install --user --name=iniciacion-nlp-llm
```

**Linux / macOS:**

```bash
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
$EDITOR .env
python -m ipykernel install --user --name=iniciacion-nlp-llm
```

En `.env`:

```env
GROQ_API_KEY=gsk_tu_clave_valida
```

Obtén una clave en [console.groq.com](https://console.groq.com).

> **Importante:** Si recibes `401 Invalid API Key`, reinicia el kernel de Jupyter y vuelve a ejecutar la celda de configuración. No uses placeholders como `gsk_reemplaza_con_tu_clave`.

### 1.2 Verificar instalación

```bash
python -c "import langchain, langgraph, faiss, sentence_transformers; print('OK')"
jupyter lab --version
```

### 1.3 Lanzar Jupyter Lab

```bash
jupyter lab
```

Selecciona el kernel `iniciacion-nlp-llm` y abre `notebook/` o `exercises/`.

---

## 2. Orden recomendado de ejecución

Cada notebook teórico tiene un ejercicio homólogo en `exercises/` con prefijo `EX_`.

### Regla general

1. Ejecutar el **notebook teórico** en `notebook/` (*Run All* o celda a celda).
2. Revisar el **ejercicio resuelto** en `exercises/`.
3. No saltar al módulo 06 sin haber completado al menos 03–05.

### Mapa completo de módulos

| Orden | Notebook (`notebook/`) | Ejercicio (`exercises/`) | Tema |
|:-----:|--------------------------|--------------------------|------|
| 0a | `00_Frameworks_Pytorch_vs_Tensorflow.ipynb` | `EX_00_Frameworks_Pytorch_vs_Tensorflow.ipynb` | PyTorch vs TensorFlow |
| 0b | `00_Introduccion_NLP_casos_de_uso.ipynb` | `EX_00_Introduccion_NLP_casos_de_uso.ipynb` | Casos de uso NLP |
| 1 | `01_Introduccion_NLP_Embeddings_Basicos.ipynb` | `EX_01_Introduccion_NLP_Embeddings_Basicos.ipynb` | Embeddings básicos |
| 2 | `02_Embeddings_Transformers.ipynb` | `EX_02_Embeddings_Transformers.ipynb` | Sentence Transformers |
| 3 | `03_Ingenieria_de_Prompts.ipynb` | `EX_03_Ingenieria_de_Prompts.ipynb` | Prompting + Groq |
| 4 | `04_Chatbots_Basicos.ipynb` | `EX_04_Chatbots_Basicos.ipynb` | Chatbots y memoria |
| 5 | `05_Vectorstores_Retrieval.ipynb` | `EX_05_Vectorstores_Retrieval.ipynb` | FAISS, chunking |
| **6** | **`06_Introduccion_RAG.ipynb`** | **`EX_06_Introduccion_RAG.ipynb`** | **RAG básico** |
| **7** | **`07_Reranking_Optimizacion.ipynb`** | **`EX_07_Reranking_Optimizacion.ipynb`** | **Reranking** |
| **8** | **`08_Introduccion_Agentes.ipynb`** | **`EX_08_Introduccion_Agentes.ipynb`** | **Introducción a agentes** |
| **9** | **`09_Agentes_LangChain.ipynb`** | **`EX_09_Agentes_LangChain.ipynb`** | **Agentes LangChain** |
| **10** | **`10_LangGraph_Flujos.ipynb`** | **`EX_10_LangGraph_Flujos.ipynb`** | **LangGraph** |
| **11** | **`11_RAG_Avanzado_Agentico.ipynb`** | **`EX_11_RAG_Avanzado_Agentico.ipynb`** | **Agentic RAG** |
| 12 | `12_Modelos_Contexto_Multimodales.ipynb` | `EX_12_Modelos_Contexto_Multimodales.ipynb` | Multimodal / contexto largo |

### Rutas según tiempo disponible

| Tiempo | Ruta |
|--------|------|
| **30 min** | `06` + `07` (notebook y exercise) |
| **1 h** | `06` → `07` → `08` → `09` |
| **2 h** | `05` → `06` → `07` → `09` → `10` → `11` |
| **Evaluación completa** | Todos los pares 00–12 en orden |

### Notas por módulo

| Módulo | Notas |
|--------|-------|
| 00–02 | Descarga modelos Hugging Face (~400 MB). Primera ejecución lenta. |
| 03+ | Requiere `GROQ_API_KEY`. Celda de config con `getpass` si falta en entorno. |
| 05 | Puede persistir índice FAISS en `notebook/faiss_index/`. |
| 07 | Cross-Encoder `cross-encoder/ms-marco-MiniLM-L-6-v2`. Demo `"latency vs throughput"`. |
| 08 | Tools Python puras + concepto de bucles infinitos en agentes. |
| 09 | `create_tool_calling_agent` + `AgentExecutor`. Validación de API key en celda de setup. |
| 10 | Grafos `StateGraph`, nodos `retrieve` / `generate`, routing condicional. |
| 11 | LangGraph con múltiples llamadas LLM por consulta. Latencia alta. |
| 12 | Experimental; puede requerir recursos adicionales. |

---

## 3. Cómo ejecutar un notebook

1. Abrir Jupyter Lab desde la raíz del repo.
2. Elegir kernel `iniciacion-nlp-llm`.
3. Ejecutar **primero** la celda de configuración (imports + `GROQ_API_KEY`).
4. Continuar con *Run All* o celda a celda.
5. Repetir con el ejercicio homólogo en `exercises/`.

### Reproducción rápida offline (RAG + Reranking sin API)

Pega en una celda nueva o usa la sección correspondiente del notebook `07`:

```python
import numpy as np
from sentence_transformers import SentenceTransformer, CrossEncoder, util

docs = [
    "La latencia mide el tiempo de respuesta (delay) de una petición individual.",
    "El throughput representa la cantidad total de datos procesados por segundo.",
    "Cómo cocinar pasta italiana en solo diez minutos.",
    "Optimización de ancho de banda y rendimiento en redes de alta velocidad.",
]
query = "latency vs throughput"

bi = SentenceTransformer("all-MiniLM-L6-v2")
top_idx = np.argsort(util.cos_sim(bi.encode(query), bi.encode(docs))[0].tolist())[::-1][:3]
candidates = [docs[i] for i in top_idx]

cross = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
for text, score in sorted(
    zip(candidates, cross.predict([[query, c] for c in candidates])),
    key=lambda x: x[1], reverse=True,
):
    print(f"{score:.4f} | {text[:70]}...")
```

---

## 4. Qué hace el sistema / Qué NO hace

### Qué hace

| Capacidad | Ubicación |
|-----------|-----------|
| Embeddings y búsqueda semántica | Notebooks 01–02, 05 |
| RAG con LangChain | Notebook 06, EX_06 |
| Reranking Bi-Encoder + Cross-Encoder | Notebook 07, EX_07 |
| Tools y agentes ReAct | Notebooks 08–09, EX_08–EX_09 |
| Flujos LangGraph | Notebook 10, EX_10 |
| Agentic RAG con verificación | Notebook 11, EX_11 |
| Ejercicios resueltos | `exercises/EX_00` – `EX_12` |

### Qué NO hace

| Limitación | Impacto |
|------------|---------|
| Sin app desplegada | Solo notebooks Jupyter; no hay servicio HTTP ni Streamlit en la entrega |
| Sin persistencia global de índices | FAISS se reconstruye por sesión salvo módulo 05 |
| Sin memoria conversacional unificada | Cada notebook gestiona memoria de forma local |
| Sin rate limiting propio | Depende de cuotas Groq |
| Protección básica anti-injection | Instrucciones en prompts, no guardrails de producción |
| Contexto acotado | Chunking fijo; docs largos pueden perder información periférica |
| Sin CI/CD ni monitorización | Entrega académica |

---

## 5. Solución de problemas

| Síntoma | Acción |
|---------|--------|
| `401 Invalid API Key` | Reiniciar kernel; crear clave nueva en console.groq.com; no usar placeholder en `.env` |
| `429 Too Many Requests` | Esperar 60 s; evitar *Run All* repetido en notebook 11 |
| Error spaCy | `python -m spacy download en_core_web_sm` |
| FAISS / torch OOM | Reducir `k` del retriever; cerrar otros procesos |
| Primera ejecución lenta | Normal; modelos se cachean en `~/.cache/huggingface` |
| Kernel no detectado | `python -m ipykernel install --user --name=iniciacion-nlp-llm` |

---

## 6. Control de calidad

Ejecutar los casos de **[QUALITY_GATE.md](QUALITY_GATE.md)** antes de la entrega.

Validación rápida sugerida:

1. `notebook/06` — pregunta in-domain sobre el corpus del notebook.
2. `notebook/06` — pregunta fuera de dominio (ej. geografía no presente).
3. `notebook/07` — query `"latency vs throughput"`: rerank prioriza chunks técnicos.
4. `exercises/EX_09` — agente `count_words` responde con conteo correcto.
5. `notebook/11` — consulta sin contexto suficiente activa rama `no_info`.
