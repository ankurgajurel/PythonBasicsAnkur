import datetime

def dateMe():
    x = datetime.datetime.now()
    print(x.strftime("%h"))
    
dateMe()


x = datetime.datetime(2020, 5, 17)

print(x.strftime("%"))
