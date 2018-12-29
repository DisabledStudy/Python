import multiprocessing
import os
import time

def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))

def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print("\tNumber %s of %s. Honk!" % (num, stop))
        time.sleep(1)

if __name__ == "__main__":
    whoami("main")
    for n in range(4):
        p = multiprocessing.Process(target=loopy, args=("loopy",))
        p.start()
        time.sleep(5)
        p.terminate()

