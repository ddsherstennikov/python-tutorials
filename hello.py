#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Howdy World -or- Howdy Alice
Try changing the 'Howdy' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """Returns the string s repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s * 3
    if exclaim:
      result = result + '!!!'

    return result

# Define a main() function that prints a little greeting.
def main():
    # Get the name from the command line, using 'World' as a fallback.
    if len(sys.argv) >= 2:
      name = sys.argv[1]
    else:
      name = 'World'
    print 'Howdy', name
    print 'yay!'

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
