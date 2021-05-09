'''
This is simply to test the mechanism of finding the directory from which the current script is running.
'''
import os
import sys

def main():
    dir_of_script = os.path.abspath(os.path.dirname(sys.argv[0]))
    print(f'''Dir of current script is {dir_of_script}''')

if __name__ == "__main__":
    main()
