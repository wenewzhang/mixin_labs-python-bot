import csv
# with open('eggs.csv', 'a', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('new_users.csv', newline='') as f:
    reader = csv.reader(f)
    # reader = csv.DictReader(f)
    for row in reader: 
        print(row.pop())
        print(row.pop())
        # for value in row.items():
            # print(value)
