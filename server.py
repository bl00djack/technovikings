from flask import Flask

app = Flask(__name__)

from technovikings.views import mod

app.register_blueprint(mod)

app.run(host="0.0.0.0", port=5000, debug=True)