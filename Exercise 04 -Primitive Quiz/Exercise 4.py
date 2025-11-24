# Primitive Quiz - Single Question

answer = input("What is the capital of France? ")

# Check answer while ignoring capitalization
if answer.strip().lower() == "paris":
    print("Correct! Well done.")
else:
    print("Incorrect. The correct answer is Paris.") 

# Primitive Quiz - 10 European Country Capitals

questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Switzerland": "Bern"
}

score = 0

print("===== European Capitals Quiz =====")

for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ")

    if answer.strip().lower() == capital.lower():
        print("✔ Correct!")
        score += 1
    else:
        print(f"✘ Incorrect. The correct answer is {capital}.")

print("\n===== Quiz Finished! =====")
print(f"Your final score: {score} / {len(questions)}")