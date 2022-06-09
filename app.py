"""site_mon."""

import logging
import os
from logging.config import dictConfig

from flask import Flask
from flask import has_request_context
from flask import redirect
from flask import request
from flask import send_from_directory
from flask.logging import default_handler

__version__ = "0.0.1"
__license__ = None
__copyright__ = "© 2022 John Arthur Kane <John.Kane@Kane.net>"
__author__ = "John Arthur Kane"
__email__ = "John.Kane@Kane.net"

__all__ = []

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(asctime)s %(levelname)-8s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)


@app.route("/")
def kane_net():
    return redirect("http://www.kane.net")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon"
    )


@app.route("/health")
def health():
    return "OK"


@app.route("/robots.txt")
def robots():
    return send_from_directory(
        os.path.join(app.root_path, "static"), "robots.txt"
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
