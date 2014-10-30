__author__ = 'mattstocker'

from bottle import route, run, template
from Launch import launchrocket
from Config import mainpage, launchmain

@route('/')
def main():
    return str(mainpage())

@route('/launch')
def launch():
        return str(launchmain())

@route('/launch/<number>')
def launch(number='number'):
        #return template('Boom! Firework {{number}} has launched!', number=number)
         return str(launchrocket(number))

run(host='localhost', port='8060', debug=True)