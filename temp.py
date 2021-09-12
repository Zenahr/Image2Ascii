import native_web_app

url = "http://localhost:8000/"

try:
    native_web_app.open(url)
except Exception:
    print(f"No web browser found. Please open a browser and point it to {url}.")