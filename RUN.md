# RUN.md

Guia operativa para ejecutar el curso, la demo final y el quality gate.

## 1. Preparacion del entorno

Desde la raiz del repositorio:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name iniciacion_nlp_llm --display-name "Python (NLP/LLM Course)"
```

Para notebooks con Groq:

```powershell
$env:GROQ_API_KEY="TU_API_KEY_DE_GROQ"
```

No pegues claves dentro de notebooks ni commits.

## 2. Orden recomendado de ejecucion

### Fundamentos

1. `notebook/00_Introduccion_NLP_casos_de_uso.ipynb`
2. `notebook/00_Frameworks_Pytorch_vs_Tensorflow.ipynb`
3. `notebook/01_Introduccion_NLP_Embeddings_Basicos.ipynb`
4. `notebook/02_Embeddings_Transformers.ipynb`
5. `notebook/03_Ingenieria_de_Prompts.ipynb`
6. `notebook/04_Chatbots_Basicos.ipynb`
7. `notebook/05_Vectorstores_Retrieval.ipynb`

### Bloque RAG, reranking y agentes

8. `notebook/06_Introduccion_RAG.ipynb`
9. `notebook/07_Reranking_Optimizacion.ipynb`
10. `notebook/08_Introduccion_Agentes.ipynb`
11. `notebook/09_Agentes_LangChain.ipynb`
12. `notebook/10_LangGraph_Flujos.ipynb`
13. `notebook/11_RAG_Avanzado_Agentico.ipynb`
14. `notebook/12_Modelos_Contexto_Multimodales.ipynb`

### Exercises

Los notebooks `exercises/EX_06_*.ipynb` a `exercises/EX_12_*.ipynb` contienen soluciones desarrolladas para las actividades propuestas del bloque RAG/agentes/multimodal.

## 3. Ejecucion por consola

Ejecutar un notebook concreto:

```powershell
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.kernel_name=iniciacion_nlp_llm --ExecutePreprocessor.timeout=900 notebook/06_Introduccion_RAG.ipynb
```

Ejecutar el bloque RAG en orden:

```powershell
$notebooks = @(
  "notebook/06_Introduccion_RAG.ipynb",
  "notebook/07_Reranking_Optimizacion.ipynb",
  "notebook/08_Introduccion_Agentes.ipynb",
  "notebook/09_Agentes_LangChain.ipynb",
  "notebook/10_LangGraph_Flujos.ipynb",
  "notebook/11_RAG_Avanzado_Agentico.ipynb",
  "notebook/12_Modelos_Contexto_Multimodales.ipynb"
)

foreach ($nb in $notebooks) {
  jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=900 $nb
}
```

## 4. Demo final para stakeholders

La demo final es una UI Streamlit autocontenida:

```powershell
streamlit run demo_stakeholder_rag.py
```

Pasos:

1. Abrir la URL local que muestra Streamlit.
2. Opcional: introducir `GROQ_API_KEY` en la barra lateral para respuestas generativas.
3. Probar preguntas sugeridas:
   - `Cuales son los planes de precios?`
   - `Como contacto con soporte?`
   - `Donde estan las oficinas?`
   - `Que seguridad ofrece TechCorp?`
   - `Cual es la politica de vacaciones?`

La demo funciona sin API key con respuesta extractiva y citas; con Groq produce una respuesta redactada con el mismo contexto.

## 5. Limitaciones conocidas

### Que hace

- Muestra un flujo RAG entendible para stakeholders.
- Recupera documentos locales con TF-IDF.
- Devuelve fuentes citadas.
- Usa Groq opcionalmente si hay clave disponible.
- Permite demostrar abstencion cuando la base de conocimiento no cubre la pregunta.

### Que no hace

- No es un sistema productivo de seguridad, observabilidad ni permisos.
- No persiste conversaciones entre sesiones.
- No usa una base documental real ni un vector store empresarial.
- No evalua automaticamente todas las alucinaciones.
- La demo no reemplaza los notebooks tecnicos del curso.

## 6. Mini Quality Gate manual

Registrar resultado como `PASS` o `FAIL`.

| # | Caso | Esperado | Resultado |
|---|------|----------|-----------|
| 1 | Ejecutar `notebook/06_Introduccion_RAG.ipynb` | Finaliza sin error | PASS/FAIL |
| 2 | Ejecutar `notebook/07_Reranking_Optimizacion.ipynb` | Muestra ranking bi/cross/LLM | PASS/FAIL |
| 3 | Ejecutar `notebook/08_Introduccion_Agentes.ipynb` | Herramientas personalizadas responden | PASS/FAIL |
| 4 | Ejecutar `notebook/09_Agentes_LangChain.ipynb` | Agente de soporte responde casos realistas | PASS/FAIL |
| 5 | Ejecutar `notebook/10_LangGraph_Flujos.ipynb` | Flujo clasifica, recupera, genera y valida | PASS/FAIL |
| 6 | Ejecutar `notebook/11_RAG_Avanzado_Agentico.ipynb` | Respuesta con tipo, calidad e iteraciones | PASS/FAIL |
| 7 | Ejecutar `notebook/12_Modelos_Contexto_Multimodales.ipynb` | Carga CLIP o muestra fallback controlado | PASS/FAIL |
| 8 | Lanzar `streamlit run demo_stakeholder_rag.py` | UI abre localmente | PASS/FAIL |
| 9 | Preguntar en demo `Como contacto con soporte?` | Respuesta cita fuente de soporte | PASS/FAIL |
| 10 | Preguntar en demo `Cual es la politica de vacaciones?` | Respuesta se abstiene o indica falta de informacion | PASS/FAIL |

## 7. Fallos criticos y mitigaciones

| Riesgo/Fallo | Impacto | Mitigacion |
|--------------|---------|------------|
| Falta `GROQ_API_KEY` | Notebooks/agentes con Groq no generan | Usar variable de entorno o modo fallback cuando exista |
| Error SSL al descargar modelos | Hugging Face falla | Actualizar `certifi` y usar red corporativa/proxy configurado |
| Descarga lenta de modelos | Primera ejecucion tarda | Ejecutar antes de clase o usar cache local |
| Cambios de API en LangChain | Imports antiguos fallan | Preferir `langchain_core`, LCEL y ejemplos versionados |
| Memoria insuficiente con TensorFlow/PyTorch | Kernel se cierra o tarda mucho | Usar subconjuntos pequenos y una epoca para demos |
| CLIP incorrecto (`clip` sin `.load`) | Multimodal falla | Instalar `openai-clip` y reiniciar kernel |
| Alucinacion en respuestas RAG | Respuestas no soportadas | Citas obligatorias, umbral de similitud y abstencion |
| Preguntas fuera de cobertura | Respuestas incompletas | Log de consultas sin respuesta y ampliacion documental |
| Claves en notebooks | Riesgo de seguridad | Variables de entorno, `.env` local y rotacion de claves |
| Demo confundida con produccion | Expectativas incorrectas | Explicar limites en README/RUN y durante presentacion |
