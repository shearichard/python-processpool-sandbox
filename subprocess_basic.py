import subprocess
import os

def main():
    path_to_tmp = os.environ.get('TEMP')
    subprocess.run(["dir", os.path.join(path_to_tmp, '''*.xpi''')], shell=True)

if __name__ == "__main__":
    main()
