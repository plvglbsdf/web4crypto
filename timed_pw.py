#!/usr/bin/env python3.2
# timed_pw.py
# 20130311
# David Prager Branner
# Run with Python 3.2
 
"""Creates preliminary page for Marek Majkowski's Crypto demonostration.
Generates a password;
reports whole seconds elapsed since password creation;
reports length of password;
prompts user to enter password, repeating until correct.

Options: on command line, user may enter 
    * an integer for optional password length (default is 10)
    * flag -p to display password
"""

import time
import random
import bottle
import sys

# Preliminary settings
# Check command line flags and options
length = 10
reveal_password = False
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

# HTTP Methods
@bottle.route('/')
@bottle.get('/login') # or @route('/login')
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

# Begin preparing password
start_time = time.time()
# Printable ASCII ranges from 32 to 126
pw = ''.join([chr(random.randint(32, 126)) for i in range(length)])
#
# Run server
bottle.run(host='0.0.0.0', port=8080, debug=True)
