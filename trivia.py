import requests, time

questions = requests.get('https://opentdb.com/api.php?amount=10&category=22&type=boolean')

q = questions.json()
score = 0
for question in q['results']:
    print(f"Question: {question['question']}")
    x = str(input("Your Answer :"))
    if x.lower().replace(" ", "") == question['correct_answer'].lower().replace(" ", ""):
        print("Your answer is right!")
        score += 1
    else:
        print("Your answer is wrong!")
    print(f"Correct Answer: {question['correct_answer']}")
    time.sleep(5)

print(f"Your score is {score}/10!")