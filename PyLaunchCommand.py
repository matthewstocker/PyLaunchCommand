__author__ = 'mattstocker'

from bottle import route, run, template

@route('/')
def main():
    return '''
    <h1>PyLaunchControl</h1>
    <p>This is the home page, you need to get the PiLauncher app to use this server!</p>
    '''

@route('/launch/')
def launch():
        return "You haven't used the app to launch a firework have you now :("

@route('/launch/<number>')
def launch(number='number'):
        return template('Boom! Firework {{number}} has launched!', number=number)

run(host='localhost', port='8060', debug=True)