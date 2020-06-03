import csv
import Compiler

with open("submissions.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    result = []
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are ' + ", ".join(row))
            line_count += 1
        else:
            result.append(row)
            print(row[0] + " - " + row[1] + " - " + row[2] + " - " + row[3] + " - " + row[4] + " - " + row[5])
            line_count += 1
for row in result:
    Compiler.my_compiler_function(row)