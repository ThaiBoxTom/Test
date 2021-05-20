from bottle import route, run

@route('/')
def hallo():
    return "Hallo Herr Thielbar!"

if __name__ == '__main__':
    run(debug=True, reloader=True)