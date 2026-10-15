import os
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Inicializar el navegador
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    # Cerrar el navegador al finalizar el test
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de Pytest para capturar pantalla automáticamente si un test falla
    y adjuntarla al reporte HTML.
    """
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
            os.makedirs(reports_dir, exist_ok=True)
            
            # Nombre del archivo de captura
            screenshot_name = f"{item.name}.png"
            screenshot_path = os.path.join(reports_dir, screenshot_name)
            driver.save_screenshot(screenshot_path)

            # Si pytest-html está activo, adjuntar imagen al reporte
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html is not None:
                extras.append(pytest_html.extras.image(screenshot_name))
        report.extras = extras