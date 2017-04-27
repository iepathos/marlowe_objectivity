#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from textblob import TextBlob
from flask import Flask, request, jsonify
logger = logging.getLogger('marlowe.objectivity.server')

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    text = TextBlob(str(request.form.get('text').encode("utf8")))
    objectivity = 1.0 - float(text.sentiment.subjectivity)
    data = {'objectivity': round(objectivity, 2)}
    return jsonify(data)


if __name__ == '__main__':
    debug = os.environ.get('DEBUG')
    if debug is not None:
        debug = True
    else:
        debug = False
    app.run(debug=debug, host='0.0.0.0')
