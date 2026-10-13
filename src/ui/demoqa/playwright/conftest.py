import os

import pytest


def _get_viewport(window_size: str) -> dict | None:
    """Преобразует WINDOW_SIZE в viewport Playwright."""
    window_size = (window_size or "full").lower()

    sizes = {
        "mobile": (390, 844),
        "2k": (1920, 1080),
        "2.5k": (2560, 1440),
        "4k": (3840, 2160),
    }

    if window_size in ("full", "fullscreen"):
        return None

    if window_size in sizes:
        width, height = sizes[window_size]
        return {"width": width, "height": height}

    if "x" in window_size:
        width, height = window_size.split("x", 1)
        return {"width": int(width), "height": int(height)}

    return None


@pytest.fixture(scope="session")
def browser_type_launch_args() -> dict:
    """Аргументы запуска браузера Playwright."""
    browser_name = os.environ.get("BROWSER", "chromium").lower()
    is_headless = os.environ.get("HEADLESS", "false").lower() == "true"
    window_size = os.environ.get("WINDOW_SIZE", "full").lower()

    args: dict = {"headless": is_headless}
    launch_args: list[str] = ["--no-sandbox"]

    if window_size in ("full", "fullscreen"):
        launch_args.append("--start-maximized")

    if browser_name == "chrome":
        args["channel"] = "chrome"
        args["args"] = launch_args

    elif browser_name == "chromium":
        args["args"] = launch_args

    elif browser_name == "firefox":
        args["firefox_user_prefs"] = {
            "browser.console.log_level": "fatal",
        }

    elif browser_name in ("edge", "msedge"):
        args["channel"] = "msedge"
        args["args"] = launch_args

    elif browser_name == "webkit":
        args["args"] = launch_args

    else:
        raise ValueError(
            f"Браузер '{browser_name}' не поддерживается. "
            "Выберите chrome, chromium, firefox, edge или webkit."
        )

    return args


@pytest.fixture(scope="session")
def browser_context_args() -> dict:
    """Настройки контекста Playwright: viewport и другие параметры."""
    window_size = os.environ.get("WINDOW_SIZE", "full").lower()

    if window_size in ("full", "fullscreen"):
        return {"no_viewport": True}

    viewport = _get_viewport(window_size)

    if viewport:
        return {"viewport": viewport}

    return {}
