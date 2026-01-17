# Questions=[
#     ["Who is the founder of Microsoft?", "Bill Gates", "Steve Jobs", "Elon Musk", "Jeff Bezos", 1],
#     ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
#     ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2],
#     ["What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
#     ["Who wrote 'Romeo and Juliet'?", "Mark Twain", "William Shakespeare", "Charles Dickens", "Jane Austen", 2],
#     ["What is the chemical symbol for gold?", "Au", "Ag", "Fe", "Pb", 1],
#     ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
#     ["What is the hardest natural substance on Earth?", "Diamond", "Gold", "Iron", "Quartz", 1],
#     ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
#     ["What is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Great White Shark", 2],      
#     ]

# prize=[200, 400, 800, 1600, 3200, 6400, 12500, 25000, 50000, 100000]
# i=0
# total=0
# for question in Questions:
#     print(question[0])
#     print(f"a.{question[1]}")
#     print(f"b.{question[2]}")
#     print(f"c.{question[3]}")   
#     print(f"d.{question[4]}")


#     print("press 1 for a,2 for b,3 for c,4 for d")
#     a=int(input("your answer is"))
#     if(a==question[5]):
#         print("correct answer")
#         total+=prize[i]
#         i+=1
#     else:
#         print("wrong answer")
#         break

# print("your total prize is", total)



'''
category_ids = {
    "film": 11,
    "sports": 21,
    "animals": 27,
    "celebrities": 26,
    "mathematics": 19,
    "computers": 18
}
'''


import requests
import random

print("press 21 for sports, 11 for film, 27 for animals, 26 for celebrities, 19 for mathematics, 18 for computers")
category = int(input("Enter the category number: "))

if category not in [21, 11, 27, 26, 19, 18]:
    response= requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=multiple")

else:
    response = requests.get(f"https://opentdb.com/api.php?amount=10&category={category}&difficulty=easy&type=multiple")


Questions = []

if response.status_code == 200:
    data = response.json()
    for item in data['results']:
        question = item['question']
        correctoption = item['correct_answer']  
        incorrectoptions = item['incorrect_answers']  
        
        
        incorrectoptions.append(correctoption)
        random.shuffle(incorrectoptions)
        
        
        correctindex = incorrectoptions.index(correctoption) + 1
        
        
        Questions.append([question, *incorrectoptions, correctindex])
else:
    print("Failed to fetch questions. Please check your internet connection.")
    exit()

prize = [200, 400, 800, 1600, 3200, 6400, 12500, 25000, 50000, 100000]
i = 0
total = 0


for question in Questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    print("Press 1 for a, 2 for b, 3 for c, 4 for d")
    try:
        a = int(input("Your answer is: "))
        if a == question[5]:
            print("Correct answer!")
            total += prize[i]
            i += 1
        else:
            print("Wrong answer!")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        break

print("Your total prize is", total)