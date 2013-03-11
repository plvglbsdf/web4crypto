#!/usr/bin/env python3.2
# Run with Python 3.2

import time
import random
import bottle
import sys

length = 10
for i in sys.argv:
    try:
        length = int(i)
    except:
        pass
    if i == '-p':
        reveal_password = True
form = '''<form method="POST" action="/login">
         <input name="password" type="password" />
         <input type="submit" />
         </form>'''
start_time = 0
pw = ''

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

start_time = time.time()
pw = ''.join([chr(random.randint(32, 126)) for i in range(length)])

bottle.run(host='0.0.0.0', port=8080, debug=True)
