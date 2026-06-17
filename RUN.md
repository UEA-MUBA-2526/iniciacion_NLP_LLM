# RUN.md — Checkpoint 2

## 1. Objetivo

Este documento describe cómo ejecutar la entrega final del Checkpoint 2 del repositorio `iniciacion_NLP_LLM`.

La entrega incluye los notebooks posteriores a Vector Stores:

* RAG
* Reranking y optimización
* Agentes
* LangChain
* LangGraph
* RAG avanzado / agentic RAG
* Contexto largo y multimodalidad

También incluye los ejercicios correspondientes dentro de la carpeta `exercises`.

---

## 2. Instalación

Desde la raíz del repositorio:

```bash
pip install -r requirements.txt
```

Si se utiliza un proveedor externo de LLM, como Groq, es necesario configurar la variable de entorno correspondiente antes de ejecutar los notebooks que llaman al modelo.

En Windows CMD:

```bash
set GROQ_API_KEY=your_api_key_here
```

Importante: la API key no debe guardarse dentro de los notebooks ni subirse al repositorio.

---

## 3. Cómo abrir el proyecto

Desde la raíz del repositorio:

```bash
jupyter lab
```

También puede abrirse directamente desde la carpeta local del proyecto:

```bash
cd /d "D:\Master en Business Analytics\IA\Notebooks\iniciacion_NLP_LLM"
jupyter lab
```

---

## 4. Orden recomendado de ejecución

Se recomienda ejecutar los notebooks en el siguiente orden:

1. `notebook/06_Introduccion_RAG.ipynb`
2. `notebook/07_Reranking_Optimizacion.ipynb`
3. `notebook/08_Introduccion_Agentes.ipynb`
4. `notebook/09_Agentes_LangChain.ipynb`
5. `notebook/10_LangGraph_Flujos.ipynb`
6. `notebook/11_RAG_Avanzado_Agentico.ipynb`
7. `notebook/12_Modelos_Contexto_Multimodales.ipynb`

Después, ejecutar los ejercicios correspondientes:

1. `exercises/EX_08_Introduccion_Agentes.ipynb`
2. `exercises/EX_09_Agentes_LangChain.ipynb`
3. `exercises/EX_10_LangGraph_Flujos.ipynb`
4. `exercises/EX_11_RAG_Avanzado_Agentico.ipynb`
5. `exercises/EX_12_Modelos_Contexto_Multimodales.ipynb`

---

## 5. Demo final reproducible

La demo final recomendada para stakeholders es:

```text
notebook/11_RAG_Avanzado_Agentico.ipynb
```

Esta demo muestra un flujo avanzado de RAG con comportamiento agentic, incluyendo:

* análisis de la pregunta,
* recuperación de contexto,
* evaluación de suficiencia del contexto,
* generación de respuesta,
* control de calidad,
* mejora de respuesta si es necesario,
* uso de historial conversacional.

### Pasos para lanzar la demo

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Configurar la API key del proveedor LLM si es necesaria:

```bash
set GROQ_API_KEY=your_api_key_here
```

3. Abrir Jupyter Lab:

```bash
jupyter lab
```

4. Abrir el notebook:

```text
notebook/11_RAG_Avanzado_Agentico.ipynb
```

5. Ejecutar las celdas en orden.

6. Probar preguntas de ejemplo como:

```text
¿Qué es el IBI?
```

```text
¿Y qué bonificaciones tiene?
```

```text
When is IVTM paid?
```

---

## 6. Limitaciones conocidas

* La ejecución de algunos notebooks depende de tener configurada una API key válida del proveedor LLM.
* La calidad de las respuestas depende del contexto recuperado y de los documentos disponibles.
* El sistema no debe considerarse una aplicación de producción, sino una demo técnica y académica.
* El RAG puede fallar si los documentos recuperados no contienen información suficiente.
* El reranking mejora la selección de documentos, pero no garantiza una respuesta perfecta.
* Los agentes pueden aumentar la latencia y el coste por el uso de múltiples pasos.
* Los flujos con LangGraph son demostrativos y no incluyen monitorización avanzada.
* La parte multimodal se implementa como stub o estructura de mensaje, no como aplicación visual completa.
* No se incluyen credenciales reales en el repositorio.
* La evaluación es manual y orientada a comprobar funcionamiento básico, no rendimiento en producción.

---

## 7. Mini Quality Gate

| Nº | Caso de prueba                                    | Resultado esperado                                                         | Estado |
| -: | ------------------------------------------------- | -------------------------------------------------------------------------- | ------ |
|  1 | Abrir Jupyter Lab desde la raíz del repositorio   | Jupyter Lab se abre correctamente                                          | PASS   |
|  2 | Ejecutar `06_Introduccion_RAG.ipynb`              | Se construye un flujo básico de RAG                                        | PASS   |
|  3 | Ejecutar `07_Reranking_Optimizacion.ipynb`        | Se aplica reranking u optimización sobre resultados recuperados            | PASS   |
|  4 | Ejecutar `08_Introduccion_Agentes.ipynb`          | Se entienden herramientas y flujo básico de agente                         | PASS   |
|  5 | Ejecutar `09_Agentes_LangChain.ipynb`             | El agente puede usar una herramienta definida                              | PASS   |
|  6 | Ejecutar `10_LangGraph_Flujos.ipynb`              | El flujo de estados avanza por los nodos definidos                         | PASS   |
|  7 | Ejecutar `11_RAG_Avanzado_Agentico.ipynb`         | El sistema recupera contexto, genera respuesta y aplica control de calidad | PASS   |
|  8 | Probar una pregunta sin contexto suficiente       | El sistema reconoce que no tiene información suficiente o evita inventar   | PASS   |
|  9 | Probar una pregunta de seguimiento con historial  | El sistema mantiene continuidad conversacional básica                      | PASS   |
| 10 | Ejecutar `12_Modelos_Contexto_Multimodales.ipynb` | Se documenta la estructura esperada para mensajes multimodales             | PASS   |

---

## 8. Fallos críticos y mitigaciones

| Fallo crítico                        | Riesgo                                                  | Mitigación                                                            |
| ------------------------------------ | ------------------------------------------------------- | --------------------------------------------------------------------- |
| API key no configurada               | Los notebooks con LLM externo no ejecutan correctamente | Usar variable de entorno `GROQ_API_KEY`                               |
| API key subida al repositorio        | Exposición de credenciales                              | No guardar claves reales en notebooks; usar variables de entorno      |
| Dependencias no instaladas           | Errores de importación                                  | Ejecutar `pip install -r requirements.txt`                            |
| Contexto recuperado insuficiente     | Respuestas incompletas o incorrectas                    | Añadir control de suficiencia de contexto y respuesta fallback        |
| Alucinaciones del modelo             | Información no respaldada                               | Forzar respuestas basadas en contexto y usar citas cuando sea posible |
| Reranking incorrecto                 | Documentos poco relevantes en primera posición          | Ajustar top-k, revisar chunks y validar manualmente                   |
| Bucles en agentes                    | Coste y latencia excesivos                              | Limitar número de iteraciones y pasos del agente                      |
| Fallos por cambios de modelo externo | Incompatibilidad con proveedor LLM                      | Mantener el modelo configurable                                       |
| Archivos auxiliares ausentes         | Demo no reproducible                                    | Incluir archivos como `sample_ai_doc.txt` en el repositorio           |
| Multimodalidad no disponible         | No se puede ejecutar visión real                        | Dejar stub documentado con formato `image_url` o base64               |

---

## 9. Estado de entrega

Rama de entrega:

```text
juan_sanchez
```

Commit final inicial:

```text
5a1a633 - Complete checkpoint 2 notebooks and exercises
```

La entrega queda preparada para revisión en GitHub.
