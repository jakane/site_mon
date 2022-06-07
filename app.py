"""site_mon."""

import os

from flask import Flask
from flask import redirect
from flask import send_from_directory

__version__ = "0.0.1"
__license__ = None
__copyright__ = "© 2022 John Arthur Kane <John.Kane@Kane.net>"
__author__ = "John Arthur Kane"
__email__ = "John.Kane@Kane.net"

__all__ = []

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
