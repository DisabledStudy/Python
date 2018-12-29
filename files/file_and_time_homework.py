import os
import time
import datetime

string_time = time.ctime(time.time())
print("get string time:", string_time)

text_file = open('homework.txt', 'wt')
print(string_time, file=text_file)
text_file.close()

read_text_file = open('homework.txt', 'rt')
string_time_read = read_text_file.read()
read_text_file.close()
print("read string time:", string_time_read)


example_time = "2012-09-01"
fmt = "%Y-%m-%d"
time_from_example = time.strptime(example_time, fmt)
print(time_from_example)


my_birthday = datetime.date(1989, 9, 20)
ten_thousand_days = datetime.timedelta(days = 10000)
my_age_after_10_thousand_days = my_birthday + ten_thousand_days
print(my_age_after_10_thousand_days)

