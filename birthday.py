import datetime
birthday=input("Enter your birthday: ")

birthdate=datetime.datetime.strptime(birthday, "%m/%d/%Y").date()

print("Your birthday is on "+birthdate.strftime("%B"))