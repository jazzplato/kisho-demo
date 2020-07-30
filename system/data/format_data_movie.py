import csv

FILE_INPUT = 'raw_movies.csv'
FILE_OUTPUT = 'movies.csv'

cols_to_remove = sorted(range(3, 11), reverse=True)
row_count = 0

with open(FILE_INPUT, "r") as source:
    reader = csv.reader(source)
    with open(FILE_OUTPUT, "w", newline='') as result:
        writer = csv.writer(result)
        for row in reader:
            row_count += 1
            print('\r{0}'.format(row_count), end='')
            if row_count == 1:
                row = ["id", "title", "year"]
            else:
                for col_index in cols_to_remove:
                    del row[col_index]
            writer.writerow(row)