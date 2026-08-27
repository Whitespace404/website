from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "hello"

from webs import routes
