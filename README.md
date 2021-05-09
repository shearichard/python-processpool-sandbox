# Python Processpool Sandbox
A number of scripts which exercise aspects of the Python futures.processpool functionality

## pipenv
To invoke the virtenv `cd` into the root of the project and execute ..
```
pipenv shell
```

Type `exit` to leave the virtenv.


## An executable to use for tests
The script `standin_for_real_binary.py` is intended to be made into a .exe by the `pyinstaller` command. The output of the process, `dist\standin_for_real_binary.exe` is not saved to the repos.

Make the executable as follows

```
pyinstaller --onefile stand_in_for_real_binary.py
```
