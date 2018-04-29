import sys

import hello
#from hello import repeat

def main():
    if len(sys.argv) >= 2:
      name = sys.argv[1]
    else:
      name = 'World'

    print sys.argv

    if len(sys.argv) >= 3:
      exclaim = ( sys.argv[2] in ['true', '1', 't', 'y', 'yes', 'True', 'TRUE'] )
    else:
      exclaim = 0
    print hello.repeat(name, exclaim)

if __name__ == '__main__':
  main()
