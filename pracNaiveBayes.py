data = [
    ["sunny","hot","high","false","no"],
    ["sunny","hot","high","true","no"],
    ["overcast","hot","high","false","yes"],
    ["rain","mild","high","false","yes"],
    ["rain","cool","normal","false","yes"],
    ["rain","cool","normal","true","no"],
    ["overcast","cool","normal","true","yes"],
    ["sunny","mild","high","false","no"],
    ["sunny","cool","normal","false","yes"],
    ["rain","mild","normal","false","yes"],
    ["sunny","mild","normal","true","yes"],
    ["overcast","mild","high","true","yes"],
    ["overcast","hot","normal","false","yes"],
    ["rain","mild","high","true","no"]
]

def predict(string):
    size = len(data)
    FirstY = SecondY = ThirdY = FourthY = yesss = 0
    FirstN = SecondN = ThirdN = FourthN = no = 0
    for row in data:
        outlook, temperature, humidity, windy, prob = row[0], row[1], row[2], row[3], row[4]
        if(prob == "yes"):
            yesss += 1
            if(outlook == string[0]):
                FirstY += 1
            if (temperature == string[1]):
                SecondY += 1
            if (humidity == string[2]):
                ThirdY += 1
            if (windy == string[3]):
                FourthY += 1
        else:
            no += 1
            if (outlook == string[0]):
                FirstN += 1
            if (temperature == string[1]):
                SecondN += 1
            if (humidity == string[2]):
                ThirdN += 1
            if (windy == string[3]):
                FourthN += 1
    FirstY = FirstY/yesss
    SecondY = SecondY / yesss
    ThirdY = ThirdY / yesss
    FourthY = FourthY / yesss
    yesss = yesss/size
    FirstN = FirstN / no
    SecondN = SecondN / no
    ThirdN = ThirdN / no
    FourthN = FourthN / no
    no = no/size
    pyes = yesss * FirstY * SecondY * ThirdY * FourthY
    pno = no * FirstN * SecondN * ThirdN * FourthN
    print("Probability of Playing: ", pyes)
    print("Probability of Not Playing: ", pno)
    if(pyes>pno):
        print("Yes")
    else:
        print("No")

string = input("Enter comma-separated tuple:")
string = string.split(',')
print(string)
predict(string)