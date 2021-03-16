## 1. Introduction ##

import multiprocessing

## 2. Creating a Process ##

import time
def wait():
    time.sleep(0.5)
    print("Done waiting")

process = multiprocessing.Process(target=wait)

process.start()

print("Finished")

process.join()

## 3. Parallel Execution ##

import time
def wait():
    time.sleep(0.5)
    print("Done waiting")

process = multiprocessing.Process(target=wait)

process.start()
process.join()
print("Finished")

## 4. Running Two Processes ##

import time
import multiprocessing
def wait():
    time.sleep(0.5)
    print("Done waiting")

# Add code below

start = time.time()
p1 = multiprocessing.Process(target = wait)
p2 = multiprocessing.Process(target = wait)
p1.start()
p2.start()
p1.join()
p2.join()
end = time.time()
elapsed = end - start

## 5. Running Multiple Processes ##

import multiprocessing
import time
def wait():
    time.sleep(0.5)
    print("Done waiting")

start = time.time()
processes = [multiprocessing.Process(target=wait) for i in range(6)]

for i in processes:
    i.start()
    
for i in processes:
    i.join()
    
end = time.time()

elapsed = end- start

## 6. Process Function Arguments ##

import multiprocessing
def sum3(x, y, z):
    print(x + y + z)

def list_average(values):
    print(sum(values) / len(values))
    
sum3_process = multiprocessing.Process(target=sum3, args = [3,2,5])

list_average_process = multiprocessing.Process(target=list_average, args = [[1,2,3,4,5]])

processes = [sum3_process, list_average_process]

for i in processes:
    i.start()
    
for i in processes:
    i.join()

## 7. Sharing Memory ##

import multiprocessing

def sum3(x, y, z, shared_value):
    print( x + y + z)

def sum3(x, y, z, shared_value):
    shared_value.value = x + y + z
    
    
float_value = multiprocessing.Value("f")

process = multiprocessing.Process(target=sum3, args = [5,7,4, float_value])

process.start()
process.join()

print(float_value.value)


    
    


## 8. Sharing Memory Caveats ##

def sum_values(first, last, shared_value):
    for i in range(first, last):
        shared_value.value += i

def sum_with_two_processes():
    N = 10000

    shared_value = multiprocessing.Value("i")
    process1 = multiprocessing.Process(target=sum_values, args=(1, N // 2, shared_value))
    process2 = multiprocessing.Process(target=sum_values, args=(N // 2, N, shared_value))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    return shared_value.value

results = []

for i in range(10):
    result = sum_with_two_processes()
    results.append(result)
    
print(results)

## 9. Using a Lock ##

def sum_values(first, last, shared_value):
    for i in range(first, last):
        with shared_value.get_lock():
            shared_value.value += i

def measure_runtime(function_to_measure):
    N = 10000
    shared_value = multiprocessing.Value("i")
    process1 = multiprocessing.Process(target=function_to_measure, args=(1, N // 2, shared_value))
    process2 = multiprocessing.Process(target=function_to_measure, args=(N // 2, N, shared_value))
    start = time.time()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end = time.time()
    return end - start
    
def sum_values_improved(first, last, shared_value):
    value_sum = 0
    for i in range(first, last):
        value_sum+=i
        with shared_value.get_lock():
            shared_value.value +=value_sum
            
time_sum_values = measure_runtime(sum_values)           
time_sum_values_improved= measure_runtime(sum_values_improved)           

    