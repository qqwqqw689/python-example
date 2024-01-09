import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(5)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    # %H:%M:%S Hour:Minute:Second
    # logging.INFO : Confirmation that things are working as expected.

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=('1',))
    # target is the callable object to be invoked by the run() method.
    # args is a list or tuple of arguments for the target invocation.
    # a tuple with only one item -> add a comma after the item
    logging.info("Main    : before running thread")
    x.start()
    # start() Start the thread’s activity.
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
