import random


def run_quiz(questions, num_questions=5):
    score = 0
    selected_questions = random.sample(questions, min(num_questions, len(questions)))

    for q in selected_questions:
        print("\n" + q["question"])
        options = q["options"]
        random.shuffle(options)  # Randomize options

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        try:
            answer = int(input("Your answer (1-4): "))
            if options[answer - 1] == q["answer"]:
                print("Correct! ✅")
                score += 1
            else:
                print(f"Wrong ❌ The correct answer is: {q['answer']}")
        except (ValueError, IndexError):
            print("Invalid input. Skipping question.")

    print(f"\nYour final score is {score}/{len(selected_questions)}")

quiz_questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "London"],
     "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"],
     "answer": "Mars"},
    {"question": "Who wrote 'Hamlet'?",
     "options": ["Mark Twain", "William Shakespeare", "Charles Dickens", "Leo Tolstoy"],
     "answer": "William Shakespeare"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
     "answer": "Pacific"},
    {"question": "Which gas do plants use for photosynthesis?",
     "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "Which language is used to create web pages?", "options": ["Python", "HTML", "Java", "C++"],
     "answer": "HTML"},
    {"question": "What is H2O commonly known as?", "options": ["Oxygen", "Hydrogen", "Salt", "Water"],
     "answer": "Water"},
    {"question": "Who painted the Mona Lisa?",
     "options": ["Pablo Picasso", "Leonardo da Vinci", "Vincent Van Gogh", "Michelangelo"],
     "answer": "Leonardo da Vinci"},
    {"question": "Which is the largest animal on Earth?", "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"],
     "answer": "Blue Whale"}
]

run_quiz(quiz_questions, num_questions=7)

