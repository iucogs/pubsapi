from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('port', default=8080, type=int, nargs='?', help='port number')
    args = parser.parse_args()

    run(host='localhost', port=args.port)

