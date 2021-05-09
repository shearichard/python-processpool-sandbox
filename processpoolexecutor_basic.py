from concurrent.futures import ProcessPoolExecutor
import os
import time
import random

def task(taskid):
    slp_dur_secs = random.randint(3,10) 
    time.sleep(slp_dur_secs) 
    print(f"Executing our Task (id {taskid}) on Process : {os.getpid()} (sleep was {slp_dur_secs})")


def main():
    with ProcessPoolExecutor(max_workers=3) as executor:
        task1 = executor.submit(task, 1)
        task2 = executor.submit(task, 2)


if __name__ == "__main__":
    main()
