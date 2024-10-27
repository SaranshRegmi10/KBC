ques1 = "What does “www” stand for in a website browser?"
ans1 = ["a. Web World Wide ", "b. World Wide Web", "c. World Want Web  ", "d. Web What Web","b"]

ques2 = "Which animal can be seen on the Porsche logo?"
ans2 = ["a. Bull", "b. Horse", "c. Chicken", "d. Lion","b"]

ques3 = "Worship of Krishna is observed by which Religious Faith??"
ans3 = ["a. Muslim", "b. Hindu", "c. Christian", "d. Sikh","b"]

ques4 = "How long is an Olympic swimming pool (in meters)?"
ans4 = ["a. 50m", "b. 80m", "c. 110m", "d. 65m","a"]

ques5 = "What country has the most natural lakes?"
ans5 = ["a. Canada", "b. Russia", "c. India", "d. Brazil","a"]

ques6 = "How many teeth does an adult human have?"
ans6 = ["a. 32", "b. 30", "c. 28", "d. 35","a"]

ques7 = "Which auto brand was the first to offer seat belts?"
ans7 = ["a. Nash Moto", "b. BMW", "c. Suzuki Motors", "d. Fiat Motors","a"]

ques8 = "Which Central American country has a name which translates to English as “The Saviour”?"
ans8 = ["a. Mexico", "b. Costa Rica", "c. Honduras", "d. El Salvador","d"]

ques9 = "In what year was the Corvette introduced?"
ans9 = ["a. 1999", "b. 1965", "c. 1953", "d. 1955","c"]

ques10 = "Who is the Greek god of war and son of Zeus and Hera?"
ans10 = ["a. Alexis", "b. Athena", "c. Taurus", "d. Ares","d"]

ques11 = "What is the name of the largest moon of Jupiter?"
ans11 = ["a. Xz-100", "b. Ganymede", "c. Apolois", "d. Zeneth","b"]

ques12 = "Which infinity stone was located on Vormir?"
ans12 = ["a. Time", "b. Mind", "c. Soul", "d. Power","c"]

ques13 = "What country would you find Lake Bled?"
ans13 = ["a. Slovenia", "b. Croatia", "c. Slovakia", "c. Bosnia","a"]

ques14 = "Which Basketball team has completed two threepeats?"
ans14 = ["a. Chicago Bulls", "b. Golden State Warriors", "c. Edmonton Oilers", "c. Cleveland Cavaliers","a"]

ques15 = "Who wrote the fantasy novel American Gods??"
ans15 = ["a. Alez Willams", "b. Andre Estaban", "c. Serena Williams", "d. Neil Gaiman ","d"]

ques16 = "Benjamin Franklin was a key figure in the drafting of the United States Constitution. Which state did he represent during the Constitutional Convention in 1787?"
ans16 = ["a. Washington DC", "b. New Jersey", "c. Pennslyvenia", "d.New York","c"]

ques17 = "Which English philosopher wrote \"Leviathan\" in 1651??"
ans17 = ["a. Edvard Munch", "b. Thomas Hobbes", "c. Mick Mars", "d. George Frideric Handel","b"]


ques = [ques1, ques2, ques3, ques4, ques5,ques6, ques7,ques8,ques9,ques10,ques11,ques12,ques13,ques14,ques15,ques16,ques17]
ans = [ans1, ans2, ans3, ans4, ans5,ans6, ans7,ans8,ans9,ans10,ans11,ans12,ans13,ans14,ans15,ans16,ans17]
levels = [1000,2000,3000,5000,10000,20000,40000,8000,160000,320000,640000,1250000,2500000,5000000,7500000,1000000,75000000]

def quesans():  
    amount = 0
    for i in range(len(ques)):
        print("\nQuestion for Rs.",levels[i])
        print(ques[i])
        answer = ans[i][-1]
        for option in ans[i][:-1]:
            print(option)
        x = input("Enter your option: ")
        if x == answer:
            amount = levels[i]
            print(f"Your answer is correct. You won Rs.{levels[i]}.")
        else:
            print("Answer is incorrect")
            break   
    if amount == levels[-1]:
        print("\nSAAAAAAAAAAAAAAAAAAAAAAATTTTTT CRRRRRRRRRRRRRRRRRRRROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOORRRRRRRRRRRR")
    print("\nYour total amount is:. Rs.",amount)

# Start the game
name = input("Enter your name: ")
print("Welcome",name,"to the KBC")
quesans()
