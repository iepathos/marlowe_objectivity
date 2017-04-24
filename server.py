#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from textblob import TextBlob
from flask import Flask, request, jsonify
logger = logging.getLogger('marlowe.objectivity.server')

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    text = TextBlob(request.form.get('text'))
    objectivity = 1.0 - text.sentiment.subjectivity
    data = {'objectivity': objectivity}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
