##################### Extra Hard Starting Project ######################
import smtplib, pandas, os, random
import datetime as dt
# 1. Update the birthdays.csv
data = pandas.read_csv('birthdays.csv')
birthdays = data.to_dict(orient='records')
test_gmail = "matthewstestingemail87@gmail.com"
password = "ddfi tksv drsp dnhu"



# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

for person in birthdays:
    if person["month"] == month and person['day'] == day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter = random.choice(os.listdir("./letter_templates"))
        with open(f"./letter_templates/{letter}") as file:
            text = file.read()
            text = text.replace('[NAME]', person['name'])

            # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com") as connection_gmail:
                connection_gmail.starttls()
                connection_gmail.login(user=test_gmail, password=password)
                connection_gmail.sendmail(from_addr=test_gmail, to_addrs=person['email'], msg=f"Subject:Happy Birthday\n\n{text}")











