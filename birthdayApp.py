# This is a simple program in python which create a simple Birthday App
# with following features
#   1) Add a new Birthday
#   2) Search for a birthday by name
#   3) Search for birthdays based on a month
#   4) Exit the App
#
# Every time a new birthday is added in App, it creates an entry into the csv sheet named as dateofBirth.csv
# Basically this dateofBirth.csv acts as a database it store Name and Date of Birth of Individual.
# The Search either by "Name" or by "Month" also occur based on this csv file.
# On Program start data from this csv is loaded into a dictionary object called ad birthdayDict,
# On adding a new birthday leads to a new entry in this dictionary which is later on written into the csv
#
# Following Features of Python is Used:
#     1)Variable and Function Declaration
#     2)String Manipulation
#     3)Use of different data type such as dictionary, data frame, list, String
#     4)Pandas to read and write a csv.
#     5)Commandline User Input
#     6)Date Manipulation



import datetime
import pandas as pd
birthdayDict = {}
monthDict = {'January':'1', 'February':'2', 'March':'3', 'April':'4', 'May':'5', 'June':'6','July':'7', 'August':'8', 'September':'9','October':'10', 'November':'11', 'December':'12'}
datetimefmt = '%Y-%m-%d %H:%M:%S.%f'
datefmt = '%m-%d-%Y'


# This method is used to display App features and all the options available for User to choose from
def appInfo():
    print('----------BirthDay App----------')
    print('Select a choice')
    print('1. Enter a new Birthday')
    print('2. Search for a Birthday by Name')
    print('3. Search for Birthday based on a Month')
    print('4. Exit!')


# This method take User input based on above choices
def userInput():
    return int(input('Enter your choice : '))


# This method is used to add a new birthday in the App
# This method creates a data frame from a dictionary and
# write that dictionary to a csv file
def addBirthDay():
    name = input('Enter Name : ')
    if name.upper() not in birthdayDict:
        dob = input('Enter Date of Birth (MM-DD-YYYY) : ')
        birthdayDict[name.upper()] = dob
    else:
        print('Birthday for {n} exist in App.'.format(n = name.upper()))
    name_list = []
    dob_list = []
    for k,v in birthdayDict.items():
        name_list.append(k)
        dob_list.append(v)
    df = pd.DataFrame({'Name':name_list,'DOB':dob_list})
    df.to_csv('dateofBirth.csv',header=None, index = False)


# This method tells us about the number of days left between current date
# and birthday of a person in current year
def getDaysLeft(dob):
    today = datetime.datetime.now()
    dobThisYear = dob.split('-')[0]+'-'+dob.split('-')[1]+'-'+str(today.year)
    fDate= str(today).split(' ')[0]
    fToday = fDate.split('-')[1]+'-'+fDate.split('-')[2]+'-'+fDate.split('-')[0]
    fToday = datetime.datetime.strptime(fToday, datefmt)
    dob = datetime.datetime.strptime(dobThisYear, datefmt)
    if fToday > dob:
        return 'Birthday was due '+ str(fToday - dob) +' days ago.'
    elif fToday < dob:
        return 'Birthday is coming in '+ str(fToday - dob) +' days.'
    else: return 'Birthday is today. Wish!!'


# This method allow user to search for a birthday based on a Name
def searchByName():
    if len(birthdayDict) == 0:
        print("No data in App!! Please Add the birthdays.")
    else:
        name = input('Enter Name : ')
        if name.upper() in birthdayDict:
            daysLeft = getDaysLeft(birthdayDict[name.upper()])
            print('''           ************************************************************
            Date of Birth of {n} on {d} 
            ************************************************************'''.format(n = name.upper(), d = birthdayDict[name.upper()]))
            print(daysLeft)
        else: print('Birthday for {n} not present in App. '.format(n = name.upper()))


# This method allow user to search for all the birthdays in a given month
def searchByMonth():
    mon = input('Enter the Complete Month Name ( January, February,..) : ')
    monIndex = monthDict[mon]
    dobThisMonth = []
    for k,v in birthdayDict.items():
        if str(v).split('-')[0] == monIndex or str(v).split('-')[0] == '0'+monIndex:
            dobThisMonth.append((k,v))
    print('Birthdays in {m} are {v} : '.format(m = mon, v = dobThisMonth))


# This method is used to load the data from csv to a dictionary
def loadDOB():
    dobfile = pd.read_csv('dateofBirth.csv',header=None, names=['Name','DOB'])
    global birthdayDict
    birthdayDict = dict(zip(list(dobfile.Name),list(dobfile.DOB)))


# This is the main method which acts like entry point for the program
def main():
    loadDOB()
    while True:
        appInfo()
        choice = userInput()
        if choice == 1: addBirthDay()
        elif choice == 2: searchByName()
        elif choice == 3: searchByMonth()
        elif choice == 4: break
        else : print('Enter a valid choice')

# This is a boiler plate code used to run a stand alone program in python.
if __name__ == '__main__':
   main()
