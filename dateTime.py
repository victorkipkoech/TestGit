import datetime
currentDate = datetime.date.today()
# birthday=input("Enter your birthday: ")
# print (currentDate)
# print(currentDate.day)
# print(currentDate.year)
# print(currentDate.month)

# print(currentDate.strftime('%d %b, %Y'))
# print(currentDate.strftime ("Please attend the church event on %A ,%d %b in the year %Y"))
# print("Your birthday is on "+birthday)
userinput =input('Please enter your birthday(mm/dd/yyyy): ')
birthday=datetime.datetime.strptime(userinput,'%m/%d/%Y').date()
print(birthday)
days= currentDate -birthday
print (days)