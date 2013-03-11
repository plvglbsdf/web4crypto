Simple web servers for testing cryptographic tactics
----------------------------------------------------

1. `timed_pw.py`: Runs in Python 3.2. Creates preliminary page for Marek Majkowski's Crypto demonostration. Does the following:

 * generates a password;

 * reports whole seconds elapsed since password creation;

 * reports length of password;

 * prompts user to enter password, repeating until correct.

 **Options**: on command line, user may enter 

 * an integer for optional password length (default is 10)

 * flag -p to display password

 **Date**: 20130311.

1. `hashes.py`: Runs in Python 3.2. Adds a succession of strings to a hash table of size n until k-1 collisions are reached.

[end]
