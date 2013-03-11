#!/usr/bin/env python3

import string
import time
import random
import bottle
import os


# random uses int(time.time() * 256) when it's first time loaded
# make sure we call random.choice soon after
SECRET_LEN = 12

secret_time = time.time()

# this is the default for systems without _urandom, btw.
random.seed(int(secret_time * 256))

secret = ''.join(random.choice(string.ascii_letters) for i in range(SECRET_LEN))
print("[.] Secret_time: %r %r" % (secret_time, int(secret_time * 256)))
print("[.] Secret: %r" % (secret,))




app = bottle.Bottle()

@app.get('/')
def login_form(message = ''):
    return message + \
            '<p>Password of length {0} was generated {1} seconds ago.</p>'.\
            format(SECRET_LEN, int(time.time() - secret_time))

@app.post('/')
def login_submit():
    password = bottle.request.forms.get('password')
    if password == secret:
        return '''<p>Your password was CORRECT! How's that possible! OMG!</p>'''
    else:
        bottle.abort(401, '''Your password was incorrect; try again.''')


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=PORT, debug=True)


