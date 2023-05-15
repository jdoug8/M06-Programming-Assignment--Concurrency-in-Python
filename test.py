import multiprocessing as mp
import random
import time
import datetime

def waiting_time():
    rnd_time = random.uniform(0,1)
    time.sleep(rnd_time)
    current_date = datetime.datetime.now()
    print(f"Current process is {rnd_time} at {current_date}")
    


if __name__ == '__main__':
    processes = [mp.Process(target = waiting_time) for i in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    