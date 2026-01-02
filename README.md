# 📊 ETL de estudiantes y notas (con Python y SQLite)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)

## 📝 Descripción

Pipeline ETL (Extract, Transform, Load) que procesa datos de estudiantes y sus calificaciones. El proyecto realiza limpieza de datos, cálculo de promedios académicos y almacenamiento en base de datos SQLite.

## 🎯 Objetivo

Demostrar habilidades en:

- Extracción de datos desde archivos CSV
- Transformación y limpieza de datos con Pandas
- Carga de datos procesados en base de datos
- Implementación de lógica de negocio (promedios, estados de aprobación)

## 📂 Estructura del Proyecto

```
ETL-STUDENTS-GRADES/
│
├── data/                      # Datos de entrada
│   ├── students.csv          # Información de estudiantes
│   └── grades.csv            # Calificaciones por curso
│
├── etl/                       # Módulos del pipeline ETL
│   ├── __init__.py
│   ├── extract.py            # Extracción de datos
│   ├── transform.py          # Transformación y limpieza
│   ├── load.py               # Carga a base de datos
│   └── main.py               # Script principal
│
├── outputs/                   # Resultados procesados
│   └── complete_report.csv   # Reporte final
│   └── students.db           # Archivo de base de datos
│
├── querys/                    # Consultas SQL de ejemplo
│   └── querys.sql
│
├── .env                       # Variables de entorno
├── .gitignore                # Archivos ignorados por Git
├── README.md                 # Este archivo
└── requirements.txt          # Dependencias del proyecto
```

## 📊 Datos de Entrada

### `students.csv`

```csv
student_id,name,age,city
1,Ana Torres,18,Lima
2,Carlos Pérez,19,arequipa
3,Lucía Gómez,,LIMA
...
```

**Problemas a resolver:**

- ✅ Edades faltantes
- ✅ Ciudades con formato inconsistente
- ✅ Espacios innecesarios

### `grades.csv`

```csv
student_id,course,grade
1,Mathematics,15
1,History,18
2,Mathematics,10
...
```

## 🔄 Proceso ETL

### 1️⃣ Extract (Extracción)

- Lee archivos CSV desde la carpeta `data/`
- Valida la existencia de los archivos
- Carga datos en DataFrames de Pandas

### 2️⃣ Transform (Transformación)

- **Limpieza de datos:**
  - Normalización de nombres de ciudades (capitalización)
  - Eliminación de espacios en blanco
  - Relleno de valores faltantes en edad con el promedio
- **Cálculos:**
  - Join entre estudiantes y calificaciones
  - Cálculo de promedio por estudiante
  - Determinación de estado: Aprobado (≥ 11) o Desaprobado (< 11)

### 3️⃣ Load (Carga)

- Almacenamiento en SQLite (`students.db`)
- Exportación de reporte final en CSV
- Generación de tabla `students_grades`

## 📈 Resultados

El pipeline genera un reporte con la siguiente estructura:

| student_id | name         | age | city     | average | status |
| ---------- | ------------ | --- | -------- | ------- | ------ |
| 1          | Ana Torres   | 18  | Lima     | 16.5    | PASS   |
| 2          | Carlos Pérez | 19  | Arequipa | 11.0    | PASS   |

## 🗄️ Base de Datos

### Esquema de la tabla `students_grades`

```sql
CREATE TABLE students_grades (
    student_id INTEGER,
    name TEXT,
    age REAL,
    city TEXT,
    average REAL,
    status TEXT
);
```

### Consultas de ejemplo

Ver el archivo `querys/querys.sql` para ejemplos de consultas útiles:

- Estudiantes aprobados
- Promedio de estudiantes
- Cantidad de estudiantes

## 🔧 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip

### Pasos

1. **Clonar el repositorio**

```bash
git clone https://github.com/mfrann/etl-students-grades.git
cd etl-students-grades
```

2. **Crear entorno virtual (recomendado)**

```bash
python -m venv .env
source .env/bin/activate  # En Windows: .env\Scripts\activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

## 🚀 Uso

### Ejecutar el pipeline completo

```bash
python etl/main.py
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje principal
- **Pandas**: Manipulación y análisis de datos
- **SQLite3**: Base de datos ligera
- **CSV**: Formato de datos de entrada/salida

## 👨‍💻 Autor

**Martin Caycho**

- GitHub: [@mfrann](https://github.com/mfrann)

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub :)
