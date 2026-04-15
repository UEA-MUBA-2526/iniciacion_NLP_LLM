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

Se recomienda usar Python 3.12+ para este curso. Puedes gestionar las dependencias usando **pip** (con `requirements.txt`) o **Poetry** (con `pyproject.toml`). Elige el método que prefieras.

Si prefieres no instalar Python ni paquetes en el sistema, puedes usar **Docker con JupyterLab** (Python 3.13 y dependencias del curso ya instaladas); las instrucciones están al final de este README, en **Entorno con Docker (JupyterLab)**.

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

DespuÃ©s, selecciona en Jupyter o VS Code/Cursor el kernel `Python (NLP/LLM Course)` para ejecutar los notebooks con el entorno del proyecto. Si necesitas instalar paquetes desde una celda, usa `%pip install ...` en lugar de `!pip install ...` para que la instalaciÃ³n ocurra en el mismo kernel activo.

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

---

## Entorno con Docker (JupyterLab)

Si tienes problemas instalando Python o las dependencias en tu ordenador, puedes usar **Docker**: el contenedor incluye **Python 3.13**, **JupyterLab** y las librerías del curso (`requirements.txt`). Al arrancar el contenedor debes **montar la carpeta del repositorio** en `/workspace` para que Jupyter vea tus notebooks y puedas **guardar cambios en disco** (lectura y escritura).

En la raíz del repositorio hay un `Dockerfile` para construir la imagen. El profesorado puede publicar la misma imagen en Docker Hub para que los estudiantes solo tengan que hacer `docker pull` y `docker run`.

**Nombre de imagen de ejemplo en Docker Hub** (sustituye si el curso usa otro):

`franespiga/iniciacion-nlp-llm:jupyter`

### Instalación de Docker en macOS

1. Descarga e instala **[Docker Desktop para Mac](https://docs.docker.com/desktop/setup/install/mac-install/)** desde la documentación oficial de Docker.
2. Abre **Docker Desktop** y espera a que el estado indique que el motor está en ejecución.
3. Abre **Terminal** y comprueba la instalación:

```bash
docker --version
```

### Instalación de Docker en Windows

1. Descarga e instala **[Docker Desktop para Windows](https://docs.docker.com/desktop/setup/install/windows-install/)** desde la documentación oficial de Docker.
2. Si el instalador lo pide, activa el subsistema **WSL 2** y reinicia cuando se indique.
3. Abre **Docker Desktop** y espera a que esté listo.
4. Abre **PowerShell** o **Símbolo del sistema** y comprueba:

```cmd
docker --version
```

### Descargar la imagen desde Docker Hub

Desde una terminal, en cualquier carpeta:

```bash
docker pull franespiga/iniciacion-nlp-llm:jupyter
```

*(Si la imagen aún no está publicada, usa la sección siguiente para construirla en local.)*

### Construir la imagen en local (alternativa)

Clona el repositorio y entra en la carpeta raíz del proyecto (donde está el `Dockerfile`):

```bash
docker build -t iniciacion-nlp-llm:jupyter .
```

**Profesorado (publicar en Docker Hub):** inicia sesión con `docker login`, etiqueta la imagen con el nombre del repositorio remoto (por ejemplo `docker tag iniciacion-nlp-llm:jupyter franespiga/iniciacion-nlp-llm:jupyter`) y súbela con `docker push franespiga/iniciacion-nlp-llm:jupyter`. La primera construcción puede tardar bastante por PyTorch, TensorFlow y el resto de dependencias.

### Arrancar el contenedor y montar tu carpeta del curso

Debes ejecutar estos comandos **desde la raíz del repositorio** clonado (donde están `notebook/`, `requirements.txt`, etc.), para que el volumen monte todo el proyecto.

**macOS / Linux (bash o zsh):**

```bash
cd /ruta/al/iniciacion_NLP_LLM
docker run --rm -it -p 8888:8888 -v "$(pwd):/workspace" franespiga/iniciacion-nlp-llm:jupyter
```

Si construiste la imagen localmente con el nombre `iniciacion-nlp-llm:jupyter`, usa ese mismo nombre al final del comando en lugar de `franespiga/iniciacion-nlp-llm:jupyter`.

**Windows (PowerShell):**

```powershell
cd C:\ruta\al\iniciacion_NLP_LLM
docker run --rm -it -p 8888:8888 -v "${PWD}:/workspace" franespiga/iniciacion-nlp-llm:jupyter
```

**Windows (Símbolo del sistema, cmd.exe):**

```cmd
cd C:\ruta\al\iniciacion_NLP_LLM
docker run --rm -it -p 8888:8888 -v "%cd%:/workspace" franespiga/iniciacion-nlp-llm:jupyter
```

- **`-p 8888:8888`**: JupyterLab queda accesible en el puerto 8888 de tu máquina.
- **`-v "...:/workspace"`**: tu carpeta del proyecto se monta en `/workspace` dentro del contenedor con permisos de lectura y escritura; los cambios en notebooks se guardan en tu disco.
- **`--rm`**: el contenedor se elimina al cerrarlo (la imagen se conserva).

### Abrir JupyterLab en el navegador

Cuando el contenedor esté en marcha, abre:

[http://localhost:8888/lab](http://localhost:8888/lab)

La imagen está configurada **sin contraseña ni token** para facilitar el uso en local. **No expongas el puerto 8888 a Internet** ni uses esta configuración en servidores públicos.

### Notas adicionales

- **Ordenadores Apple Silicon (M1/M2/M3):** si la imagen de Docker Hub solo está construida para `linux/amd64`, Docker puede emularla; si ves errores o lentitud extrema, pide una imagen multi-arquitectura o construye la imagen en tu Mac con `docker build`.
- **Modelos descargados** (Hugging Face, embeddings, etc.) suelen escribirse en cachés dentro del proyecto o en tu home; al usar solo el volumen del repo, lo que quede fuera de esa carpeta no se persistirá al borrar el contenedor. Si un notebook guarda fuera de `/workspace`, monta rutas extra con `-v` o ajusta las rutas en el código.
- Para **detener** Jupyter, en la terminal del contenedor pulsa `Ctrl+C` o cierra la ventana; con `--rm` el contenedor desaparece pero tus archivos siguen en la carpeta del host.
