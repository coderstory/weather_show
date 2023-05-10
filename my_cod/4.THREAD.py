import gc,time
import _thread

def testThread():
    count = 0
    while (count < 9):
        print("Hello rt-thread!")
        count += 1
        time.sleep(1)

    print("Thread exit!")
    gc.collect()    # Free the memory space requested by the thread


# TestThread thread is created with an empty argument
_thread.start_new_thread(testThread, ())
while True:
    print("aa")
    time.sleep(1)