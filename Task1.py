"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_numbers=[]
for text in texts:
    if text[0] or text[1] not in unique_numbers:
        unique_numbers.append(text[0])

for call in calls:
    if call[0] or call[1] not in unique_numbers:
        unique_numbers.append(call[0])

print('There are {} different telephone numbers in the records.'.format(len(unique_numbers)))


