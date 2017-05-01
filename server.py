#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from textblob import TextBlob
from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk.data

logger = logging.getLogger('marlowe.objectivity.server')

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def index():
    text = request.form.get('text')
    if text is not None:
        # split into sentences, evaluate each sentence, then average the scores
        # the classifier and dataset is by sentence so best to only give
        # it one sentence at a time
        text = str(request.form.get('text').encode("utf8"))
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = tokenizer.tokenize(text)
        scores = []
        for s in sentences:
            text = TextBlob(s)
            objectivity = 1.0 - float(text.sentiment.subjectivity)
            scores.append(objectivity)
        average = sum(scores) / len(scores)
        data = {'objectivity': round(average, 2)}
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
