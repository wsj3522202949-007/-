---
id: tool-05446
type: tool
area: 库
status: active
tags: [互动叙事, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: AI_Text_Detector
summary: 互动叙事/聊天写故事
source: https://github.com/loessslr/ai_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5446
category: 一、去 AI 味 / Humanizer 库
repo: LoesssLR/AI_Text_Detector
stars: 0
url: https://github.com/loessslr/ai_text_detector
tier: "C"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# LoesssLR/AI_Text_Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/loessslr/ai_text_detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：LoesssLR/AI_Text_Detector
- **拉取时间**：2026-07-25 18:18:58

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Analizador y Sanitizador Forense de Documentos Academicos

Herramienta en Python diseñada para auditar, formatear e identificar la probabilidad de generación por Inteligencia Artificial en documentos académicos (DOCX y PDF). Actúa como un sanitizador de caracteres invisibles y un linter avanzado para el cumplimiento de las normas APA 7.ª edición.

## Caracteristicas Principales

### 1. Sanitizador de Capa Oculta de IA (DOCX y PDF)
- Remoción quirúrgica de caracteres Unicode invisibles (como Zero-Width Spaces, NBSP maliciosos y marcas BiDi) inyectados por chatbots para evadir detectores.
- Los archivos DOCX se limpian directamente conservando el 100% del formato visual (fuentes, colores, tablas).
- Los archivos PDF se analizan en modo estricto de auditoría (solo lectura) indicando la página exacta donde se hallan los rastros.

### 2. Linter Estructural y Semantico APA 7 (DOCX)
- Ajusta automáticamente márgenes a 2.54 cm (1 pulgada) en todos los lados.
- Normaliza la fuente base a Times New Roman de 12 puntos e interlineado doble (2.0) sin espaciados adicionales.
- Configura de forma dinámica la numeración de páginas en la esquina superior derecha del encabezado.
- Limpia las tablas eliminando todos los bordes verticales para ajustarse al estilo formal de APA 7.
- Ordena alfabéticamente la sección de referencias mediante reordenación de nodos XML (preservando cursivas).
- Lanza alertas críticas sobre el uso del título prohibido "Introducción" y la presencia de citas sueltas sin paréntesis en los encabezados.

### 3. Cruce Bibliografico Inteligente
- Cruza en tiempo real las citas parentéticas y narrativas en el texto contra la sección de referencias.
- Informa si existen citas huérfanas en el texto (sin fuente registrada) o si hay referencias bibliográficas que nunca fueron citadas en el documento.

### 4. Motor Heuristico Local de Estilo IA
- **Monotonia de Oraciones (Burstiness):** Calcula la desviación estándar de la longitud de las oraciones. Valores bajos indican un ritmo monótono y predictivo característico de los LLM.
- **Densidad de Cliches:** Rastrea palabras de transición y muletillas recurrentes de la IA (ej. "en el tejido social", "es fundamental destacar").
- **Voz Pasiva:** Mide la proporción de la estructura ser/estar + participio, un vicio común en traducciones y textos generados artificialmente en español.
- Todo el procesamiento se realiza localmente en milisegundos, sin necesidad de conexión externa ni APIs de pago.

## Requisitos de Instalacion

1. Clonar el repositorio.
2. Asegurar una versión de Python 3.9 o superior.
3. Instalar las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

## Guia de Uso (CLI)

El archivo principal de ejecución es `main.py`. Cuenta con argumentos flexibles de ejecución:

### Procesar un archivo unico (DOCX o PDF):
```bash
python main.py -f "ruta/al/documento.docx" -o "ruta/de/salida.docx"
```

### Procesar una carpeta completa de forma masiva:
```bash
python main.py -d "carpeta_entrada" -o "carpeta_salida"
```

### Ejecutar en Modo Backend (Retorno JSON):
Añade el flag `--json` al final de cualquier comando para suprimir los logs de consola y obtener un diccionario estructurado puro, perfecto para integraciones Web:
```bash
python main.py -f "ruta/al/documento.docx" -o "ruta/de/salida.docx" --json
```

## Flujo de Datos

```text
       [ Documento DOCX / PDF ]
                  │
                  ▼
          ┌───────────────┐
          │  sanitizer.py │ ──► (Remoción de caracteres Unicode ocultos)
          └───────┬───────┘
                  │
         ┌────────┴────────┐
         ▼                 ▼
 ┌───────────────┐ ┌───────────────┐
 │pdf_checker.py │ │apa_formatter.py│ ──► (Márgenes, Tablas APA, Paginación,
 └───────────────┘ └───────┬───────┘      Cruce e Indexación de Referencias)
                           │
                           ▼
                 ┌──────────────────┐
                 │ai_style_analyzer.py│ ──► (Estadísticas de ritmo,
                 └─────────┬────────┘      Voz pasiva y Clichés)
                           │
                           ▼
                [ Reporte CLI / JSON ]
```

## Arquitectura del Codigo

- **main.py:** Punto de entrada de la interfaz de consola, parsing de argumentos y formato de reportes.
- **detector/sanitizer.py:** Orquestación de la lectura de archivos, eliminación de caracteres invisibles y enrutamiento a los formateadores.
- **detector/pdf_checker.py:** Auditoría de caracteres invisibles y segmentación de páginas en PDFs utilizando PyMuPDF.
- **detector/apa_formatter.py:** Implementación XML de márgenes, tablas, paginación, ordenamiento de referencias y validación de citas.
- **detector/ai_style_analyzer.py:** Procesamiento estadístico del ritmo de oraciones, clichés de traducción y abuso de voz pasiva.
