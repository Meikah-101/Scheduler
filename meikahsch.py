#Tools used for code are listed below 
import random
import pandas as pd
import csv
def scheduler():
  #asks user for names 
  names=[]
  while True:
    name= input("Enter name or type 'quit':")
    names.append(name)
    if name.casefold() == 'quit' :
      names.remove('quit')
      break


  #asks user for start date and time interval
  start = input("Enter Start date using '1/1/2000' format:")
  freq = input("Enter time interval, eg.'7d','3w', '2y':") 

  # Juggling Names below 
  random.shuffle(names)
  # Enter Start Date and Time interval(freq) below 
  DateGenerator = pd.date_range(start= start, periods=len(names), freq=freq)

  #Organizes dates into an year,month, day format below 
  newFormat= DateGenerator.strftime('%Y-%m-%d')
  #Combined newly Juggled names with newly formated dates below
  datenames= zip(newFormat, names)

  # Takes all imformation from above and prints it out as the output 

  final= tuple(datenames)
  data = (final)

  with open('sch.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

#learning to create repo
