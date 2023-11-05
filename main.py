from time import time
from psutil import Process
from compare_symbols import runFirstMethod

filename = str(input('Enter name of the file >> '))
start_time = time()
runFirstMethod(filename)
end_time = time()
exec_time = end_time - start_time

print(f'Memory usage: {Process().memory_info().rss / (1024 ** 2):.2f} Mb')
print(f'Execution time: {exec_time * 1000:.2f} ms')
