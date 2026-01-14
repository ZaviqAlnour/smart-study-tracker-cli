def ask_question():
    subjects = ["Math", "Science", "Programming"]

    print("Choose a subject.")

    while True:
        try:
            choice = int(input("1. Math\n2. Science\n3. Programming\n> "))
            if 1 <= choice <= 3:
                break
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    topic = input("What did you study today? : ")

    while True:
        try:
            study_time = int(input("How many minutes did you study today? : "))
            if study_time > 0:
                break
            else:
                print("Time must be a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            difficulty = int(input("How difficult was it? (1 - 5): "))
            if 1 <= difficulty <= 5:
                break
            else:
                print("Difficulty must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        completion = input("Did you complete a problem? (yes/no): ").lower()
        if completion in ("yes", "no"):
            break
        else:
            print("Please type 'yes' or 'no'.")

    return subjects[choice - 1], topic, study_time, difficulty, completion


def main():
    subject, topic, study_time, difficulty, completion = ask_question()

    print("\n--- Study Summary ---")
    print(f"Subject chosen      : {subject}")
    print(f"Topic studied       : {topic}")
    print(f"Study time (minutes): {study_time}")
    print(f"Difficulty level    : {difficulty}/5")
    print(f"Completed problem   : {completion}")
    print("\nGood job! Keep studying. See you next time.")


if __name__ == "__main__":
    main()
