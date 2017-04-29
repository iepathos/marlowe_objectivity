#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from textblob import TextBlob
from flask import Flask, request, jsonify
from flask_cors import CORS

logger = logging.getLogger('marlowe.objectivity.server')

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def index():
    text = request.form.get('text')
    if text is not None:
        text = TextBlob(str(request.form.get('text').encode("utf8")))
        objectivity = 1.0 - float(text.sentiment.subjectivity)
        data = {'objectivity': round(objectivity, 2)}
    else:
        data = {'objectivity': 1.0}
    return jsonify(data)


if __name__ == '__main__':
    debug = os.environ.get('DEBUG')
    if debug is not None:
        debug = True
    else:
        debug = False
    app.run(debug=debug, host='0.0.0.0')
