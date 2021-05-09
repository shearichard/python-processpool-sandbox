import concurrent.futures
import subprocess
import os
import time
import random
import sys


VERSION = 2
TASK_ID_IDX = 0
TASK_DELAY_IDX = 1

def make_path_to_exe(path_of_script):
    '''
    Determine the location of the executable to be run by this script

    path_of_script: path of this script
    '''
    dir_of_script = os.path.abspath(os.path.dirname(path_of_script))
    dir_of_exe = os.path.join(dir_of_script, 'dist')
    path_of_exe = os.path.join(dir_of_exe, "stand_in_for_real_binary.exe")
    print(f'''Exe location is {path_of_exe}''')
    return path_of_exe


def main(path_of_script):
    '''
    path_of_script: path of this script
    '''
    print(f'''Running version : {VERSION}''')
    #
    path_of_exe = make_path_to_exe(path_of_script)
    #
    lst_standin_params = [["1", "5"], ["2", "1"]]
    #
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        #
        future_standin_exe = { 
            executor.submit(
                subprocess.Popen(
                    [path_of_exe, standin_arg_lst[TASK_ID_IDX], standin_arg_lst[TASK_DELAY_IDX]]
                )
            ): standin_arg_lst for standin_arg_lst in lst_standin_params 
        }
        #
        '''
        import pprint
        pprint.pprint(future_standin_exe)
        print("")
        print(type(future_standin_exe))
        print("")
        '''
        #
        for future in concurrent.futures.as_completed(future_standin_exe):
            tmp_rv_holder = future_standin_exe[future]
            #
            try:
                print("A")
                data = future.result()
                print("B")
            except Exception as exc:
                print('An exception occurred: %s' % (exc))
            else:
                print('It all worked')
        

if __name__ == "__main__":
    main(sys.argv[0])
