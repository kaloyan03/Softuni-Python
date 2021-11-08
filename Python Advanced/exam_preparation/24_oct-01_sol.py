jobs = [int(el) for el in input().split(', ')]
job_wanted_index = int(input())

cycles = 0

sorted_jobs = sorted(
    [(v,i) for (i,v) in enumerate(jobs)]
)
for (job, index) in sorted_jobs:
    cycles += job
    if index == job_wanted_index:
        break
print(cycles)