def quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["1. Paris", "2. London", "3. Berlin", "4. Madrid"],
            "answer": 1
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Saturn"],
            "answer": 3
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["1. Harper Lee", "2. J.K. Rowling", "3. Ernest Hemingway", "4. Mark Twain"],
            "answer": 1
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        answer = int(input("Enter the number of your answer: "))
        if answer == q["answer"]:
            score += 1

    print(f"You got {score} out of {len(questions)} correct!")

quiz()