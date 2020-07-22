import csv

output_file = 'users.csv'

with open(output_file, "w", newline='') as result:
    writer = csv.writer(result)
    for _ in range(100000):
        username = 