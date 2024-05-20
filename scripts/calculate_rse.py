import sys

MIN_ITERATIONS = 15
MAX_ITERATIONS = 2000


def check_rse(time_array, count):
    if count < MIN_ITERATIONS:
        return False
    if count == MAX_ITERATIONS - 1:
        return True
    t_avg = sum(time_array) / count
    dispersion = 0
    for i in range(count):
        dispersion += (time_array[i] - t_avg) ** 2

    dispersion /= count - 1
    standard_deviation = dispersion**0.5
    std_error = standard_deviation / count**0.5
    rse = std_error * 100 / t_avg
    if rse < 1:
        return True
    else:
        return False


times = []
path_to_program = (sys.argv)[1]
with open(path_to_program, "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        times.append(float(line))

res = check_rse(times, len(times))
if res:
    print(0)
else:
    print(1)
