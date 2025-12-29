print("Welcome to the Timed Math Challenge!")

import random
import time

min_number = 1
max_number = 20
operators = ['+', '-', '*']
Total_questions = 10


def generate_questions():
    left_num = random.randint(min_number, max_number)
    right_num = random.randint(min_number, max_number) 
    operator = random.choice(operators)
    question = str(left_num) + " " + operator + " " + str(right_num)
    return question

print("Lets begin the challenge! You have to answer 10 questions correctly to complete it.")
print("----------------------------------------")
start_time = time.time()

for i in range(Total_questions):
    question = generate_questions()
    answer = eval(question)
    while True:
        user_answer = input(f"Question {i + 1}: What is {question}? ")
        if user_answer == str(answer):
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("------------------------------------------")

print(f"Congratulations! You completed the challenge in {total_time} seconds.")