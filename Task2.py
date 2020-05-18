"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
telephone_numbers = dict()
most_spent_duration = 0
most_spent_number = None
for i in range(len(calls)):
    telephone_numbers[calls[i][0]] = telephone_numbers.get(calls[i][0], 0) + int(calls[i][-1])
    telephone_numbers[calls[i][1]] = telephone_numbers.get(calls[i][1], 0) + int(calls[i][-1])
    if telephone_numbers[calls[i][0]] > most_spent_duration:
        most_spent_number = calls[i][0]
        most_spent_duration = telephone_numbers[calls[i][0]]
    if telephone_numbers[calls[i][1]] > most_spent_duration:
        most_spent_number = calls[i][1]
        most_spent_duration = telephone_numbers[calls[i][1]]

# number_with_max_time = sorted(telephone_numbers, reverse=True, key=lambda x: telephone_numbers[x])[0]
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(most_spent_number, most_spent_duration))