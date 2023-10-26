import smtplib
import random
import datetime as dt

# send the email if condition is met
MY_EMAIL = "damilolabakare222@gmail.com"
MY_PASSWORD = "arvmutrfpxdomrhh"

# Get the date
now = dt.datetime.now()
day_of_week = now.weekday()
hour = now.hour

if day_of_week == 3 and hour == 15:
    # get a random quote from the quotes file
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=60) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="Ajokebakaredam2004@outlook.com",
            msg=f"Subject:Monday motivation\n\n{quote}"
        )




