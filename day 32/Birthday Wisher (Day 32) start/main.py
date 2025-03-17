import smtplib, random
import datetime as dt

test_gmail = "matthewstestingemail87@gmail.com"
test_yahoo = "matthewtestingemail@yahoo.com"
#
# with smtplib.SMTP("smtp.gmail.com") as connection_gmail:
#     connection_gmail.starttls()
#     connection_gmail.login(user=test_gmail, password="ddfi tksv drsp dnhu")
#
#     connection_gmail.sendmail(from_addr=test_gmail, to_addrs=test_yahoo, msg="Subject:Hello\n\nHello from python")
#     connection_gmail.close()

now = dt.datetime.now()

year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
hour = now.hour
minutes =  now.minute

# print(now)
#
# date_of_birth = dt.datetime(year=1994 , month= 5, day=19)
# print(date_of_birth)

if day_of_week == 0:
    with open('quotes.txt') as file:
        quotes= file.read()
        quote_list = quotes.split('\n')
        print(quote_list)

        with smtplib.SMTP("smtp.gmail.com") as connection_gmail:
            connection_gmail.starttls()
            connection_gmail.login(user=test_gmail, password="ddfi tksv drsp dnhu")
            connection_gmail.sendmail(from_addr=test_gmail, to_addrs=test_yahoo, msg=f"Subject:Hello\n\n{random.choice(quote_list)}")
