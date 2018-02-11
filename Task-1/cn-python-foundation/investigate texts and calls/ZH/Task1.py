"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


	
def add_telephone_number(phone_list, dic_number):
	for lineInfor in phone_list:
		dic_number.add(lineInfor[0])
	
	
"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""
set_phoneNumber = set()
add_telephone_number(texts, set_phoneNumber)
add_telephone_number(calls, set_phoneNumber)
count = len(set_phoneNumber)
print("There are <{}> different telephone numbers in the records.".format(count))










