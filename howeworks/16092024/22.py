import openpyxl

file_path = '22_58333 (1).xlsx'
wb = openpyxl.load_workbook(file_path)
sheet = wb.active

task_list = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    pid, exec_time, deps = row
    task_list.append((pid, exec_time, deps))

def finish_time_calculator(t):
    finish_times = {}
    for pid, exec_time, deps in task_list:
        exec_time = t if exec_time == 't' else int(exec_time)

        if deps == 0 or deps is None:
            finish_times[pid] = exec_time
        else:
            dep_ids = [int(dep) for dep in str(deps).split(';')]
            max_dep_time = max(finish_times[dep] for dep in dep_ids)
            finish_times[pid] = max_dep_time + exec_time

    return max(finish_times.values())

max_time = 0
for t in range(1, 100):
    if finish_time_calculator(t) <= 22:
        max_time = t

print(max_time)
