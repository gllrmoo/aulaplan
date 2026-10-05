# Evidencia Aulaplan | Guillermo Gutiérrez Álvarez

Proyecto: **aulaplan**

Este documento contiene la estructura actual del proyecto y el contenido actualizado de cada archivo Python, excluyendo directorios voluminosos, dependencias y artefactos generados.

## Estructura

```text
aulaplan/
├─ apps/
│  ├─ api/
│  │  ├─ .venv/
│  │  ├─ src/
│  │  │  ├─ core/
│  │  │  │  └─ __init__.py
│  │  │  ├─ http/
│  │  │  │  ├─ __init__.py
│  │  │  │  └─ routes_health.py
│  │  │  └─ __init__.py
│  │  ├─ dev.py
│  │  ├─ requirements.txt
│  │  └─ tests/
│  └─ web/
│     ├─ .node_modules/
│     ├─ .nuxt/
│     ├─ app/
│     │  ├─ assets/
│     │  │  └─ css/
│     │  │     └─ main.css
│     │  ├─ components/
│     │  │  ├─ catalog/
│     │  │  │  └─ CatalogManager.vue
│     │  │  ├─ AppHeader.vue
│     │  │  ├─ AppSidebar.vue
│     │  │  └─ StatCard.vue
│     │  ├─ composables/
│     │  │  ├─ useApi.ts
│     │  │  └─ useAuth.ts
│     │  ├─ layouts/
│     │  │  ├─ auth.vue
│     │  │  └─ default.vue
│     │  ├─ middleware/
│     │  │  └─ auth.global.ts
│     │  ├─ pages/
│     │  │  ├─ academic-periods.vue
│     │  │  ├─ availability.vue
│     │  │  ├─ constraints.vue
│     │  │  ├─ dashboard.vue
│     │  │  ├─ generator.vue
│     │  │  ├─ groups.vue
│     │  │  ├─ index.vue
│     │  │  ├─ login.vue
│     │  │  ├─ offerings.vue
│     │  │  ├─ rooms.vue
│     │  │  ├─ schedules.vue
│     │  │  ├─ subjects.vue
│     │  │  ├─ teachers.vue
│     │  │  ├─ time-blocks.vue
│     │  │  └─ users.vue
│     │  ├─ plugins/
│     │  │  └─ firebase.client.ts
│     │  ├─ stores/
│     │  │  └─ auth.ts
│     │  ├─ types/
│     │  │  └─ index.ts
│     │  └─ app.vue
│     ├─ public/
│     │  ├─ favicon.ico
│     │  └─ robots.txt
│     ├─ .env
│     ├─ .env.example
│     ├─ .gitignore
│     ├─ nuxt.config.ts
│     ├─ package.json
│     ├─ README.md
│     └─ tsconfig.json
├─ functions/
│  ├─ venv/
│  ├─ .gitignore
│  ├─ main.py
│  └─ requirements.txt
├─ .firebaserc
├─ .gitignore
├─ docs/
├─ firebase/ 
├─ node_modules/ 
├─ firebase.json
├─ firebase-debug.log
├─ firestore.indexes.json
├─ firestore.rules
├─ package.json
├─ package-lock.json
└─ skills-lock.json
```

## Archivos Python y código

Se incluyen **6** archivos Python del proyecto.

### `apps/api/dev.py`

**Ruta:** `apps/api/dev.py`  
**Lenguaje/formato:** `python`

```python
from src:http.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=8000)
```

### `apps/api/src/__init__.py`

**Ruta:** `apps/api/src/__init__.py`  
**Lenguaje/formato:** `python`

```python
```

### `apps/api/src/core/__init__.py`

**Ruta:** `apps/api/src/core/__init__.py`  
**Lenguaje/formato:** `python`

```python
```

### `apps/api/src/http/__init__.py`

**Ruta:** `apps/api/src/http/__init__.py`  
**Lenguaje/formato:** `python`

```python
```

### `apps/api/src/http/routes_health.py`

**Ruta:** `apps/api/src/http/routes_health.py`  
**Lenguaje/formato:** `python`

```python
from flask import Flask
from src.http.routes_health import health_bp

def test_health():
    app = create_app(testing=True)
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['runtime'] == 'python'
```

### `functions/main.py`

**Ruta:** `functions/main.py`  
**Lenguaje/formato:** `python`

```python
# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_functions.options import set_global_options
from firebase_admin import initialize_app

# For cost control, you can set the maximum number of containers that can be
# running at the same time. This helps mitigate the impact of unexpected
# traffic spikes by instead downgrading performance. This limit is a per-function
# limit. You can override the limit for each function using the max_instances
# parameter in the decorator, e.g. @https_fn.on_request(max_instances=5).
set_global_options(max_instances=10)

# initialize_app()
#
#
# @https_fn.on_request()
# def on_request_example(req: https_fn.Request) -> https_fn.Response:
#     return https_fn.Response("Hello world!")
```

