from flask import Flask
import krouth_site.views as views

app = Flask(__name__)

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/hello', view_func=views.hello)
