#!/usr/bin/env python3.2
# hashes.py
# 20130311
# David Prager Branner
# Run with Python 3.2
 
"""Creates preliminary page for Marek Majkowski's Crypto demonostration.
"""

import bottle
import sys

n = 2**10 - 1
k = 50
the_array = [[] for i in range(n)]
form = '''<form method="POST" action="/">
         <input name="string" type="text" />
         <input type="submit" />
         </form>'''

def hash_n_buckt_fr_str(the_string):
    the_hash = abs(the_string.__hash__())
    return the_hash, the_hash % n

# HTTP Methods
@bottle.route('/')
def login_form():
    announce = '''<p>Enter a string, please.</p>'''
    return announce + form

@bottle.post('/')
def login_submit():
    the_string = bottle.request.forms.get('string')
    the_hash, bucket = hash_n_buckt_fr_str(the_string)
    if len(the_array[bucket]) > k:
        return '''<p>500 Internal Server Error
                \nCollision buffer #{0} overflow, k = {1}.
                \nLast entry was {2}.</p>'''.\
                format(bucket, k, the_array[bucket][k-1])
    else:
        the_array[bucket].append(the_string)
        return '''<p>200 OK\nString {0} added to bucket {1}, index {2}.</p>'''.\
                format(the_string, bucket, len(the_array[bucket])-1) + form

# Run server
bottle.run(host='localhost', port=8080, debug=True)
