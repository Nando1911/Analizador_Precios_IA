# Analizador de Precios con Scraping y IA

Este proyecto obtiene datos de precios de productos de un sitio web, analiza la información utilizando IA y genera visualizaciones para interpretar las tendencias del mercado.

---

## Funcionalidades

- **Web Scraping:** Extrae nombres y precios de productos automáticamente desde un sitio web de prueba.
- **Análisis con IA:** Genera insights sobre tendencias y precios usando OpenAI GPT (o simulación si no hay crédito).
- **Visualización de datos:** Histogramas que muestran la distribución de precios.
- **Exportación de datos:** Guarda automáticamente los datos en un archivo CSV (`precios.csv`) para análisis posteriores.

---

## Tecnologías utilizadas

- **Python 3**
- **Requests & BeautifulSoup** – Para obtener los datos de la web.
- **Pandas** – Para manejo y limpieza de datos.
- **Matplotlib** – Para visualizaciones de precios.
- **OpenAI GPT** – Para generar análisis automatizados (opcional si no hay crédito).

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/Analizador_Precios_IA.git
cd Analizador_Precios_IA