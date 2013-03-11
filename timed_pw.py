#!/usr/bin/env python3.2
# Run with Python 3.2

import time
import random
import bottle
import sys
import string

SECRET_LEN = 12

secret_time = time.time()
secret = ''.join(random.choice(string.ascii_letters) for i in range(SECRET_LEN))

print("[.] Secret: %r" % (secret,))

@bottle.route('/')
@bottle.get('/login')
def login_form(message = ''):
    announce = message + \
            '<p>Password of length {0} was generated {1} seconds ago.</p>'.\
            format(length, int(time.time() - secret_time))
    return announce + form

@bottle.post('/login')
def login_submit():
    password = bottle.request.forms.get('password')
    if password == pw:
        return '''<p>Your password was CORRECT! How's that possible! OMG!</p>'''
    else:
        return '''<p>Your password was incorrect; try again.</p>''' + form


bottle.run(host='0.0.0.0', port=8080, debug=True)
