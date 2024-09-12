import time


# Benchmarks
def benchmark(func, *args):
    # Measuring Time
    Start = time.time()
    result = func(*args)
    Stop = time.time()
    # Formating Time
    delay = Stop - Start
    delay = round(delay, 4)
    # Returning
    return {"Time": delay, "Output": result}
