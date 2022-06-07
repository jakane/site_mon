'''site_mon.'''

import os

from flask import Flask, redirect

__version__ = "0.0.1"
__license__ = None
__copyright__ = "© 2022 John Arthur Kane <John.Kane@Kane.net>"
__author__ = 'John Arthur Kane'
__email__ = 'John.Kane@Kane.net'

__all__ = []

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK"

@app.route("/")
def kane_net():
    return redirect("http://www.kane.net")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
