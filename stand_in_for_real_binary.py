'''
A script which is converted into a .exe which in is then used a proxy for the .exe 
which is to be run from a Python script

Two arguments are sent. The first some arbitary, non-whitespace, string which is acts
as the 'runid', the second an integer which is used to simulate the .exe taking some 
time to complete.
'''
import subprocess
import os
import sys
import tempfile
from datetime import datetime
import time

def main(runid, slp_dur_secs):
    d=datetime.now()
    strlogstart = f'''Run started at {d.strftime('%Y%m%dT%H%M%S.%f')}'''
    time.sleep(slp_dur_secs) 
    prfx = f'''stand_in_output_{d.strftime('%Y%m%dT%H%M%S')}_'''
    path_to_tmp = os.environ.get('TEMP')
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, prefix=prfx) as tmp:
        d=datetime.now()
        strlogend = f'''Run ended at {d.strftime('%Y%m%dT%H%M%S.%f')}'''
        tmp.write(f'''Runid was {runid} | Delay was {slp_dur_secs} | pid was {os.getpid()} | {strlogstart} | {strlogend} ''')
    

if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise ValueError('Two arguments must be provided, runid followed by delay in seconds.')
 
    runid = sys.argv[1]
    slp_dur_secs = int(sys.argv[2])
    #
    try:
        main(runid, slp_dur_secs)
    except Exception as exc:
        TODO
