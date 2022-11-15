import numpy as np
import time


def really_hard_task(some_parameter: int) -> dict:
    result = np.random.random()
    some_num = 0
    start_time = time.perf_counter()
    while (time.perf_counter() - start_time < 2.0):  # horrible busy wait
        some_num += 1
    print(f"finished task crunching {some_parameter} with result {result:.2f}")
    total_duration = time.perf_counter() - start_time
    return {"param": some_parameter,
            "duration": total_duration,
            "result": result}