from flaskwebgui import FlaskUI
from app.wsgi import application as app

ui = FlaskUI(app, start_server='django', height=800, width=1400)
ui.run()