# Pre-Entrega: Automatización de Pruebas QA - SauceDemo

Proyecto de automatización de pruebas end-to-end (E2E) sobre la aplicación web [SauceDemo](https://www.saucedemo.com/) utilizando **Selenium WebDriver**, **Python** y **Pytest**, implementando el patrón de diseño **Page Object Model (POM)**.

**Estudiante:** Cristian Ricardo Franco  
**Curso:** Automatización QA  

---

## 📌 Propósito del Proyecto
Validar los flujos críticos de la plataforma web SauceDemo correspondientes a las primeras fases del curso:
1. **Autenticación (Login):** Ingreso con credenciales válidas y verificación de redirección al inventario.
2. **Navegación y Catálogo:** Verificación de títulos, visibilidad de productos, primer ítem (nombre/precio) y componentes de interfaz (menú hamburguesa y filtros).
3. **Carrito de Compras:** Adición de productos, actualización del contador y verificación del ítem en la vista del carrito.

---

## 🛠️ Tecnologías Utilizadas
- **Python 3.12**
- **Selenium WebDriver** (automatización web)
- **Pytest** (framework de pruebas)
- **Pytest-HTML** (generación de reportes de ejecución)
- **Git & GitHub** (control de versiones)

---

## 📂 Estructura del Proyecto

```text
├── pages/                  # Page Object Model (POM)
│   ├── login_page.py       # Interacciones de la vista de Login
│   ├── inventory_page.py   # Interacciones del Catálogo/Inventario
│   └── cart_page.py        # Interacciones del Carrito de compras
├── tests/                  # Casos de prueba automatizados
│   ├── test_login.py       # Pruebas de autenticación
│   ├── test_inventory.py   # Pruebas de catálogo e interfaz
│   └── test_cart.py        # Pruebas del flujo de carrito
├── utils/                  # Constantes y utilidades auxiliares
│   ├── __init__.py
│   └── constants.py
├── reports/                # Reporte HTML y evidencias
│   └── reporte.html
├── conftest.py             # Fixtures de Pytest y hooks para capturas en fallos
├── pytest.ini              # Configuración base de Pytest
├── .gitignore              # Exclusiones de Git
└── README.md               # Documentación del proyecto
```
---
## ⚙️ Instalación de Dependencias

1. Clonar el repositorio:
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd pre-entrega-automation-testing-cristian-franco
   ```
2. Crear y activar el entorno virtual (usando Conda o venv):
    ```bash
    conda create -n test_env python=3.12 -y
    conda activate test_env
    ```
3.  Instalar las dependencias necesarias:
    ```bash
    pip install selenium pytest pytest-html
    ```
---
## 🚀 Ejecución de las Pruebas

Para ejecutar la suite completa de pruebas y regenerar el reporte HTML en la carpeta reports/:
```bash
pytest
```

O especificando los parámetros de forma manual:
```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

El reporte se guardará en reports/reporte.html e incluirá capturas de pantalla automáticas en caso de fallos.

---