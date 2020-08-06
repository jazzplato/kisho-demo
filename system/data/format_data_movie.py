import os
import csv

DIR_CURR = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_CURR)
DIR_DB_DATA = os.path.join(DIR_BASE, "database", "data")
FILE_INPUT = os.path.join(DIR_CURR, "raw_movies.csv")
FILE_OUTPUT = os.path.join(DIR_DB_DATA, "movies.csv")


def main():
    cols_to_remove = sorted(range(3, 11), reverse=True)
    row_count = 0

    with open(FILE_INPUT, "r") as source:
        reader = csv.reader(source)
        with open(FILE_OUTPUT, "w", newline="") as result:
            writer = csv.writer(result)
            for row in reader:
                row_count += 1
                print("\r{0}".format(row_count), end="")
                if row_count == 1:
                    row = ["id", "title", "year"]
                else:
                    for col_index in cols_to_remove:
                        del row[col_index]
                writer.writerow(row)


if __name__ == "__main__":
    main()