# perf_counter는 모든 시간을 측정함.
# process_time은 CPU time만을 측정함


import time


def process1():
    start = time.perf_counter()
    time.sleep(3)
    return (time.perf_counter()-start)

def process2():
    start = time.process_time()
    time.sleep(3)
    return (time.process_time()-start)


print(f'perf_counter = {process1():.4e} sec')
print(f'process_time = {process2():.4e} sec')


