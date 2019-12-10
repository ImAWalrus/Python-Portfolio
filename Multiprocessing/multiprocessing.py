
import os
import random
import logging

import multiprocessing
from multiprocessing import Process, Lock, Queue


def producer_daemon(lock, data, logger,iden):
        
    for i in range(3000):
        lock.acquire()
        r = random.randrange(100)
        data.put(r)
        lock.release()
        print("Producer {} {}".format(iden,i))
  


def consumer_daemon(lock, data, logger,iden):
    failedAttempts = 1000
    counter = 0
    while counter != failedAttempts:
        lock.acquire()
        if data.empty():
            print("EMPTY")
            counter += 1
            lock.release()
        else:
            tmp = data.get_nowait()
            print("Consumer {} {}".format(iden,tmp))
            lock.release()

if __name__ == '__main__':
    #print '\n\n\n'
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)

    LOCK = Lock()
    DATA = Queue()
    # for i in range(N): DATA.put('c')

    prod_1 = Process(target=producer_daemon, name='PROD-1', args=(LOCK, DATA, logger,1))
    prod_2 = Process(target=producer_daemon, name='PROD-2', args=(LOCK, DATA, logger,2))
    cons_1 = Process(target=consumer_daemon, name='CONS-1', args=(LOCK, DATA, logger,1))
    cons_2 = Process(target=consumer_daemon, name='CONS-2', args=(LOCK, DATA, logger,2))


    prod_1.start()
    prod_2.start()
    cons_1.start()
    cons_2.start()
