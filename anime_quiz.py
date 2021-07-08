# the more point you get, more of an extrovert character you get
# character = ["Naruto","Luffy","L", "Taki"]

choiceA_count = 0
choiceB_count = 0
choiceC_count = 0
choiceD_count = 0

question_1 = input("What is your favorite genre? A) Shounen B) Adventure C) Mystery D) Slice of life  ")
question_2 = input("What do you like to do on your free time? A) Going out B) Excercise C) Play games D) Reading a book  ")
question_3 = input("What word would your friends use to describe you? A) Leader B) Goofy C) Smart D) Easygoing  ")
question_4 = input("What would you like to eat? A) Ramen B) Meat C) Desserts D) Pastries  ")
question_5 = input("if you come across a problem, how would you solve it? A) Talk it out B) Make excuses/ Ignore it C) Find a solution alone D) Ask for help  ")

if question_1 == "A":
    choiceA_count +=1
elif question_1 == "B":
    choiceB_count +=1
elif question_1 == "C":
    choiceC_count +=1
elif question_1 == "D":
    choiceD_count +=1

if question_2 == "A":
    choiceA_count +=1
elif question_2 == "B":
    choiceB_count +=1
elif question_2 == "C":
    choiceC_count +=1
elif question_2 == "D":
    choiceD_count +=1

if question_3 == "A":
    choiceA_count +=1
elif question_3 == "B":
    choiceB_count +=1
elif question_3 == "C":
    choiceC_count +=1
elif question_3 == "D":
    choiceD_count +=1

if question_4 == "A":
    choiceA_count +=1
elif question_4 == "B":
    choiceB_count +=1
elif question_4 == "C":
    choiceC_count +=1
elif question_4 == "D":
    choiceD_count +=1

if question_5 == "A":
    choiceA_count +=1
elif question_5 == "B":
    choiceB_count +=1
elif question_5 == "C":
    choiceC_count +=1
elif question_5 == "D":
    choiceD_count +=1



def your_character():
    if choiceA_count > choiceB_count and choiceA_count > choiceC_count and choiceA_count > choiceD_count:
        return "You are Naruto from Naruto!"
    elif choiceB_count > choiceA_count and choiceB_count > choiceC_count and choiceB_count > choiceD_count:
        return "You are Luffy from One Piece!"
    elif choiceC_count > choiceA_count and choiceC_count > choiceB_count and choiceC_count > choiceD_count:
        return "You are L from DeathNote!"
    elif choiceD_count > choiceA_count and choiceD_count > choiceB_count and choiceD_count > choiceC_count:
        return "You are Taki from Your Name!"


print(your_character())





# questions = [question_1, question_2, question_3, question_4, question_5]

# def result(x):
#     if questions[x] == "A":
#         choiceA_count +=1
#     elif questions[x] == "B":
#         choiceB_count +=1
#     elif questions[x] == "C":
#         choiceC_count +=1
#     elif questions[x] == "D":
#         choiceD_count +=1

# result(0)
# result(1)
# result(2)
# result(3)
# result(4)



