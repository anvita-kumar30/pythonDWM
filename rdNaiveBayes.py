import csv
import pandas as pd

df = pd.read_csv('data.csv')
print(df)

def predict(string, df):
    FirstY = SecondY = ThirdY = yes = 0
    FirstN = SecondN = ThirdN = no = 0
    size = 0

    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size += 1
            if (row['Stolen'] == 'Yes'):
                yes += 1
                if (row['Color'] == string[0]):
                    FirstY += 1
                if (row['Type'] == string[1]):
                    SecondY += 1
                if (row['Origin'] == string[2]):
                    ThirdY += 1
            else:
                no += 1
                if (row['Color'] == string[0]):
                    FirstN += 1
                if (row['Type'] == string[1]):
                    SecondN += 1
                if (row['Origin'] == string[2]):
                    ThirdN += 1

    FirstY = FirstY/yes
    SecondY = SecondY/yes
    ThirdY = ThirdY/yes
    yes = yes/size
    FirstN = FirstN/no
    SecondN = SecondN/no
    ThirdN = ThirdN/no
    no = no/size

    pYes = yes * FirstY * SecondY * ThirdY
    pNo = no * FirstN * SecondN * ThirdN
    print("Probability of Stolen: ", pYes)
    print("Probability of Not Stolen: ", pNo)
    if (pYes > pNo):
        print("Stolen")
    else:
        print("Not Stolen")

string = input("Enter comma-separted tupple")
string = string.split(',')
# print(string)
predict(string, df)
