import time

start_time=time.perf_counter()
for counter in range(0,1000000):
    print(counter)
end_time=time.perf_counter()
elapsed_time=end_time- start_time
print(f"The elapsed time is {elapsed_time}")