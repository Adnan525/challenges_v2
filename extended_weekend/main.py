import datetime
import calendar

# day_map = dict(zip(range(1, 8), calendar.day_name))

def solve(a, b):
    score = 0;
    first = ""
    last = ""
    for i in range(a, b+1):
        for j in range(1, 13):
            # datetime_obj = datetime.datetime.strptime(f"01-{str(j).zfill(2)}-{i}", "%d-%m-%Y")
            # if datetime_obj.weekday() == 5 and datetime_obj.month.
            if(calendar.monthrange(i, j)[0] == 4 and calendar.monthrange(i, j)[1] == 31):
                score +=1
                first = calendar.month_name[j] if first == "" else first
                # print(first)
                last =  calendar.month_name[j]
    
    return (first[:3], last[:3], score)

print(solve(2016,2020))
print(calendar.monthrange(2016, 1))