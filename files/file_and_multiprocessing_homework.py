import datetime
import multiprocessing
import os
import random
import time


curr_dir = os.path.abspath('.')
print("curr dir:", curr_dir)

files_in_curr_dir = os.listdir(curr_dir)
print("files in curr dir:", files_in_curr_dir)

os.chdir('..')
parent_dir = os.path.abspath('.')
print("parent dir:", parent_dir)
print("files in parent dir:", os.listdir(parent_dir))

def print_start():
    print("start multiprocessing")

def call_date():
    time.sleep(random.randrange(1,5))
    print(datetime.datetime.ctime(datetime.datetime.now()))

if __name__ == "__main__":
    print_start()
    for n in range(5):
        p = multiprocessing.Process(target=call_date)
        p.start()