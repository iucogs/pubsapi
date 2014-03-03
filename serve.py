from bottle import abort, response, route, run
import customjson

from pubs.model import *

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

# TODO: Add an @json decorator that sets content_type and pushes the function
# return through customjson.dumps()
@route('/citation/<id:int>')
def get_citation(id):
    response.content_type = 'application/json'

    citation = Session.query(Citation).get(id)
    if citation is None:
        abort(400, "Citation not found")
    return customjson.dumps(citation.json)

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('port', default=8080, type=int, nargs='?', help='port number')
    args = parser.parse_args()

    run(host='localhost', port=args.port)

