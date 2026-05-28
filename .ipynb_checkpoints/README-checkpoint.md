# Curso de LLMs y Aplicaciones de IA

## Descripción

Este curso proporciona una introducción completa a los Modelos de Lenguaje Grande (LLMs) y sus aplicaciones prácticas. Los notebooks están diseñados para ser **standalone** (independientes), con explicaciones en **español** y código/comentarios en **inglés**.

## Estructura del Curso

| Notebook | Tema | Duración | Dificultad |
|----------|------|----------|------------|
| 00 | Introducción a NLP con HuggingFace | 3-4h | Básico |
| 00 | PyTorch vs Tensorflow | 2-2.5h | Básico |
| 01 | Introducción a NLP y Embeddings Básicos | 2-2.5h | Básico |
| 02 | Embeddings con Transformers | 2-2.5h | Básico |
| 03 | Ingeniería de Prompts | 2-2.5h | Básico |
| 04 | Chatbots Básicos | 1.5-2h | Básico |
| 05 | Vector Stores y Retrieval | 2-2.5h | Intermedio |
| 06 | Introducción a RAG | 2.5-3h | Intermedio |
| 07 | Reranking y Optimización | 2h | Intermedio |
| 08 | Introducción a Agentes | 2-2.5h | Intermedio |
| 09 | Agentes con LangChain | 2.5-3h | Avanzado |
| 10 | LangGraph y Flujos | 2.5-3h | Avanzado |
| 11 | RAG Avanzado Agentic | 2.5-3h | Avanzado |
| 12 | Modelos de Gran Contexto y Multimodales | 2h | Avanzado |

## Progresión recomendada

```
Introducción (00)
       ↓
Fundamentos (01-04)
       ↓
Retrieval (05-07)
       ↓
Agentes (08-10)
       ↓
Avanzado (11-12)
```

## Requisitos

### APIs (Gratuitas)
- **Groq API** (gratis): https://console.groq.com/keys
  - Tier gratuito generoso para modelos Llama 3.3
- **HuggingFace** (gratis): Modelos de embeddings open source

### Configuración del Entorno Virtual

Se recomienda usar Python 3.12+ para este curso. Puedes gestionar las dependencias usando **pip** (con `requirements.txt`) o **Poetry** (con `pyproject.toml`). Elige el método que prefieras:

---

## Opción 1: Instalación con pip (tradicional)

### 1. Crear el entorno virtual

```bash
# Windows
py -3.12 -m venv .venv

# Linux/Mac
python3.12 -m venv .venv
```

### 2. Activar el entorno virtual

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

> **Nota:** Sabrás que el entorno está activado cuando veas `(.venv)` al inicio de tu línea de comandos.

### 3. Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. (Opcional) Instalar en modo editable

Si prefieres instalar el proyecto como un paquete editable (útil para desarrollo):

```bash
pip install -e .
```

### Desactivar el entorno

Cuando termines de trabajar:

```bash
deactivate
```

---

## Opción 2: Instalación con Poetry (recomendado)

Poetry es un gestor de dependencias moderno que simplifica la gestión de paquetes y entornos virtuales.

### 1. Instalar Poetry

**Windows (PowerShell):**
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

**Linux/Mac:**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

> **Nota:** Después de instalar Poetry, asegúrate de agregar Poetry al PATH. En Windows, puede requerir reiniciar PowerShell o agregar manualmente la ruta de Poetry.

Verifica la instalación:
```bash
poetry --version
```

### 2. Configurar Poetry para usar entornos virtuales en el proyecto

```bash
poetry config virtualenvs.in-project true
```

Esto creará el entorno virtual en `.venv` dentro del proyecto (compatible con VS Code/Cursor).

### 3. Instalar dependencias

Poetry leerá automáticamente el archivo `pyproject.toml` y creará un entorno virtual si no existe:

```bash
poetry install
```

Este comando:
- Crea un entorno virtual (si no existe)
- Instala todas las dependencias del proyecto
- Instala el proyecto en modo editable

### 4. Activar el entorno virtual de Poetry

**Opción A: Usar el shell de Poetry (recomendado)**
```bash
poetry shell
```

**Opción B: Ejecutar comandos directamente**
```bash
poetry run python script.py
poetry run jupyter notebook
```

**Opción C: Activar manualmente el entorno**
Una vez que Poetry crea el entorno virtual en `.venv`, puedes activarlo como un entorno virtual normal:

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### Comandos útiles de Poetry

```bash
# Ver dependencias instaladas
poetry show

# Agregar una nueva dependencia
poetry add nombre-paquete

# Agregar una dependencia de desarrollo
poetry add --group dev nombre-paquete

# Actualizar todas las dependencias
poetry update

# Actualizar una dependencia específica
poetry update nombre-paquete

# Ver información del entorno
poetry env info

# Eliminar el entorno virtual
poetry env remove python

# Exportar a requirements.txt (si necesitas compatibilidad)
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

### Desactivar el entorno

Si usaste `poetry shell`:
```bash
exit
```

Si activaste manualmente el entorno virtual:
```bash
deactivate
```

---

## Configuración adicional

### Registrar el kernel de Jupyter

Si quieres usar los notebooks en Jupyter o VS Code/Cursor:

**Con pip:**
```bash
python -m ipykernel install --user --name iniciacion_nlp_llm --display-name "Python (NLP/LLM Course)"
```

**Con Poetry:**
```bash
poetry run python -m ipykernel install --user --name iniciacion_nlp_llm --display-name "Python (NLP/LLM Course)"
```

### Instalar CLIP para el Notebook 12

Para el notebook de modelos multimodales:

**Con pip:**
```bash
pip install git+https://github.com/openai/CLIP.git
```

**Con Poetry:**
```bash
poetry add git+https://github.com/openai/CLIP.git
```

---

## Comparación: pip vs Poetry

| Característica | pip + venv | Poetry |
|----------------|------------|--------|
| Gestión de dependencias | Manual (`requirements.txt`) | Automática (`pyproject.toml`) |
| Resolución de conflictos | Manual | Automática |
| Lock file | No | Sí (`poetry.lock`) |
| Entornos virtuales | Manual | Automático |
| Instalación editable | `pip install -e .` | `poetry install` (por defecto) |
| Agregar dependencias | Editar `requirements.txt` | `poetry add paquete` |
| Compatibilidad | Universal | Requiere Poetry instalado |

**Recomendación:** Si eres nuevo en Python, empieza con pip. Si buscas una experiencia más moderna y automatizada, usa Poetry.

### Librerías principales

Las dependencias están definidas en `requirements.txt` (para pip) y `pyproject.toml` (para Poetry). Ambas contienen las mismas dependencias:

- **PyTorch** - Framework de deep learning
- **Transformers** - Modelos de Hugging Face
- **Sentence-Transformers** - Embeddings de oraciones
- **LangChain** - Framework para aplicaciones LLM
- **LangGraph** - Flujos de trabajo con grafos
- **FAISS** - Búsqueda de vectores similares
- **Gensim** - Word2Vec, GloVe
- **spaCy** - Procesamiento de lenguaje natural
- **Jupyter** - Notebooks interactivos

> **Nota:** El proyecto incluye tanto `requirements.txt` como `pyproject.toml` para máxima compatibilidad. Puedes usar cualquiera de los dos métodos de instalación según tu preferencia.

## Características

- **Sin costos de API**: Usa Groq (gratis) y modelos HuggingFace
- **Standalone**: Cada notebook es independiente
- **Práctico**: Código ejecutable con ejemplos reales
- **Progresivo**: De conceptos básicos a sistemas avanzados
- **Bilingüe**: Explicaciones en español, código en inglés

## Contenido por notebook

### 00 - Introducción a NLP con HuggingFace
- Ecosistema HuggingFace
- Casos de uso de NLP
- Clasificación de texto y análisis de sentimiento
- Named Entity Recognition (NER)
- Topic Modeling
- Componentes de pipelines de NLP
- Ejemplos prácticos con corpus real

### 00 - PyTorch vs Tensorflow
- Comparativa de frameworks de Deep Learning
- Funciones de activación
- Construcción de modelos
- Entrenamiento y explotación
- Diferencias y similitudes

### 01 - Introducción a NLP y Embeddings Básicos
- One-Hot Encoding (Scikit-Learn, Keras)
- Word2Vec (modelo propio y pre-entrenados)
- GloVe
- Visualización con PCA

### 02 - Embeddings con Transformers
- BERT y BETO (español)
- Sentence Transformers
- Búsqueda semántica
- Visualización 3D con UMAP

### 03 - Ingeniería de Prompts
- Zero-shot y Few-shot
- Prompts con rol
- Chain of Thought
- Formato de salida
- Temperatura y diversidad

### 04 - Chatbots Básicos
- Chatbot basado en reglas
- Chatbot con LLM
- Memoria conversacional
- Interfaces con Streamlit

### 05 - Vector Stores y Retrieval
- FAISS
- Document Loaders
- Text Splitters
- Similarity Search
- Persistencia

### 06 - Introducción a RAG
- Arquitectura RAG
- Implementación paso a paso
- RAG con LangChain
- Memoria conversacional

### 07 - Reranking y Optimización
- Cross-Encoder
- Bi-Encoder
- LLM como Reranker
- Estrategias combinadas

### 08 - Introducción a Agentes
- Componentes de un agente
- Chain of Thought y ReAct
- Herramientas personalizadas
- Primer agente simple

### 09 - Agentes con LangChain
- Tipos de agentes
- Herramientas integradas
- Agente con RAG
- Memoria en agentes
- Salidas estructuradas

### 10 - LangGraph y Flujos
- Estados y grafos
- Flujos condicionales
- RAG con LangGraph
- Auto-corrección
- Checkpoints

### 11 - RAG Avanzado Agentic
- Arquitectura completa
- Clasificación de preguntas
- Reformulación de queries
- Verificación de calidad
- Evaluación

### 12 - Modelos de Gran Contexto y Multimodales
- Ventana de contexto
- LCM vs RAG
- CLIP
- Búsqueda de imágenes por texto
- Futuro de los LLMs

## Autor

Curso creado por Francisco Espiga Fernández

## Licencia

Material educativo para uso no comercial.
