from datetime import datetime
import schedule    
import time  








def get_current_date():
    current_datetime = datetime.now()
    day = str(current_datetime.day)
    month = str(current_datetime.month)
    if int(month) < 10:
        month = '0'+ month
    data = day +"." +month 
    return data 

def get_info():
    date = input('Enter the birthday date: (in format: 12.01) ') # надо сделать чтобы любая дата была приведена в нужный формат
    name = input(' Enter the name: ')
    with open('dates.txt', 'a') as f:
        f.write(date + " " + name +"\n")

def check():
    with open('dates.txt', 'r') as f:  
        for line in f.readlines():
            stroke = line.rstrip()
            stroke = stroke.split(' ')
            message = "Сегодня ДР у "+ stroke[1]
            if stroke[0] == get_current_date():
                print('Birthday!!!')     #надо бы улучшить оповещение, как нибудь, чтобы можно было выложить на сервак 
            else:
                continue

    

schedule.every().day.at("10:00").do(check) 

while True:
    schedule.run_pending()
    time.sleep(1)

