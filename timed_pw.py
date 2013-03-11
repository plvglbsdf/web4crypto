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
    if reveal_password:
        shown_pw = pw
    else:
        shown_pw = ''
    announce = message +\
            '<p>Password of length {0} was generated {1} seconds ago. {2}</p>'.\
            format(length, int(time.time()-start_time), shown_pw)
    return announce + form

@bottle.post('/login') # or @route('/login', method='POST')
def login_submit():
    password = bottle.request.forms.get('password')
    if password == pw:
        return '''<p>Your login was correct.</p>'''
    else:
        return '''<p>Your login was incorrect; try again.</p>''' + form


bottle.run(host='0.0.0.0', port=8080, debug=True)
