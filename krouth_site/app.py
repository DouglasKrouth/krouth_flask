from flask import Flask

import krouth_site.views as views

app = Flask(__name__)

app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/about", view_func=views.about)
app.add_url_rule("/stuff", view_func=views.stuff)
