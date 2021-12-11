import re
import datetime
def count_access_denied(log_list):
    error_name = []
    for index in range(len(log_list)-2):
        if("ERROR" in log_list[index] and "SERVICE LOGIN" in log_list[index]):
            day1 = datetime.datetime.strptime(log_list[index][:10], "%Y-%m-%d")
            day1 += datetime.timedelta(days=2)
            day2 = datetime.datetime.strptime(log_list[index+1][:10], "%Y-%m-%d")
            day2 += datetime.timedelta(days=1)
            day3 = datetime.datetime.strptime(log_list[index+2][:10], "%Y-%m-%d")
            print(day1,day2,day3)
            if(day1 == day2 == day3):
                print("days are equal")
                a = str(re.findall('\S+@\S+', log_list[index]))
                print(a)
                error_name.append(a[:a.find('@')])
    print(len(error_name))
    error_name.sort()
    for name in error_name:
        print(name)




logs = [] 

n = int(input()) 

for i in range(0,n): 

    logs.append(input()) 

count_access_denied(logs)