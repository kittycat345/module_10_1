from  threading import Thread
from datetime import datetime
import time


def write_words(word_count, file_name):
    with open(file_name, mode ="w", encoding="utf = 8") as file:
        for i in range(word_count):
            file.write( f"\n Какое-то слово № {i+1}")
            time.sleep(0.1)
time_1= datetime.now()
write_words(10, "example1.txt")

time_2= datetime.now()
print(time_2-time_1)
thread_1 = Thread(target = write_words, args =  (10, "example5.txt"))
thread_2 = Thread(target = write_words, args =  (30, "example6.txt"))
thread_3 = Thread(target = write_words, args =  (100, "example7.txt"))
thread_4 = Thread(target = write_words, args =  (200, "example8.txt"))

time_3= datetime.now()
thread_1.start()
thread_1.join()
thread_2.start()
thread_2.join()
thread_3.start()
thread_3.join()
thread_4.start()
thread_4.join()
time_4= datetime.now()
print(time_4-time_3)


