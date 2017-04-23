#!/usr/bin/env python
# -*- coding: utf-8 -*-
from textblob import TextBlob
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    text = TextBlob(request.form.get('text'))
    objectivity = 1.0 - text.sentiment.subjectivity
    return {'objectivity': objectivity}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
