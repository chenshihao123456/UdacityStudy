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


"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
incomineNumber = texts[0][0]
answeringNumber = texts[0][1]
time = texts[0][2]
firstMessage = "First record of texts, <{}> texts <{}> at time <{}>".format(incomineNumber, answeringNumber, time)
print(firstMessage)

incomineNumber = calls[-1][0]
answeringNumber = calls[-1][1]
time = calls[-1][2]
LastMessage = "First record of texts, <{}> texts <{}> at time <{}>".format(incomineNumber, answeringNumber, time)
print(LastMessage)