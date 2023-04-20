import os

from flask import Flask, request, abort, jsonify, Response
from typing import Callable, Dict, Any, Optional, Union

from utils import filter_query, map_query, unique_query, sort_query, limit_query, regex_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
query_dict: dict[str, Callable] = {'filter': filter_query,
              'map': map_query,
              'unique': unique_query,
              'sort': sort_query,
              'limit': limit_query,
              'regex': regex_query,
                                   }


@app.route("/perform_query", methods=['POST'])
def perform_query() -> Response:
    query: dict = request.json
    if not os.path.exists(os.path.join(DATA_DIR, query['file_name'])):
        abort(400)
    with open(os.path.join(DATA_DIR, query['file_name']), 'r', encoding='utf-8') as file:
        data: list[str] = file.readlines()
    for i in range(len(query) // 2):
        data = query_dict[query['cmd' + str(i + 1)]](data, query['value' + str(i + 1)])
    return jsonify(data)
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    # return app.response_class('', content_type="text/plain")



