## Pruebas Automatizadas – FastAPI + React + Pytest + Vitest

### Descripción General

Este proyecto demuestra la integración de **pruebas automatizadas** en una arquitectura moderna **Full Stack**, combinando un backend en **FastAPI (Python)** con un frontend en **React (Vite)**.
Su propósito es servir como plantilla base para proyectos de testing, demostraciones académicas y prácticas de integración continua.

---

### ⚙️ Estructura del Proyecto

```
test-fastapi_pytest/
│
├── backend/
│   ├── main.py                  # API principal (FastAPI)
│   ├── requirements.txt         # Dependencias del backend
│   ├── venv/                    # Entorno virtual (no se sube al repo)
│   └── tests/
│       ├── __init__.py
│       ├── test_items.py        # Test 1 – Endpoint /items/
│       └── test_price.py        # Test 2 – Cálculo de precios
│
└── frontend/
    ├── package.json             # Configuración del proyecto React
    ├── vite.config.js           # Configuración de Vite
    └── tests/
        ├── App.test.jsx         # Test 1 – Renderizado de componente principal
        └── Price.test.jsx       # Test 2 – Lógica de conversión
```

---

### Backend – FastAPI + Pytest

#### Instalación

```bash
cd backend
python -m venv venv
venv\Scripts\activate       # (En Windows)
source .venv/bin/activate   # En Linux/Mac
pip install -r requirements.txt
```

#### Ejecución del servidor

```bash
uvicorn main:app --reload
```

El backend estará disponible en:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

#### Ejecutar los tests del backend

```bash
pytest -v
```

---

### Frontend – React + Vitest

#### Instalación

```bash
cd frontend
npm install
```

#### Ejecutar los tests del frontend

```bash
npm test
npm run test:ui
```

Vitest ejecutará las pruebas de los componentes React y mostrará los resultados en consola.

---

### Tecnologías utilizadas

| Tipo                 | Tecnología                     | Uso principal               |
| -------------------- | ------------------------------ | --------------------------- |
| Backend              | FastAPI                        | API REST principal          |
| Backend              | Pytest                         | Pruebas automatizadas       |
| Frontend             | React + Vite                   | Interfaz de usuario moderna |
| Frontend             | Vitest + React Testing Library | Testing de componentes      |
| Control de versiones | Git + GitHub                   | Gestión del proyecto        |
