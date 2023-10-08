import time
import random

f = open('qwerty.txt', 'w')

def generate_list(size):
    lst = []
    for i in range(size):
        lst.append(random.randint(-20, 20))

    return lst

def test(count, size):
    start = time.time()
    for i in range(count):
        generate_list(size)

    end = round((time.time() - start) / count, 10)
    return end    

i = 1000
while i < 10000:
    end_time = test(100, i)
    f.write(f"{end_time} - {str(i)}\n") 
    i += 100

f.close()