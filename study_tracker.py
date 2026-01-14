def ask_question():
    subjects_AND_topics = {}
    subject_number = int(input("How many subjects do you study today?: "))
    for _ in range(subject_number):
        subject = input("Enter the subject you studied today: ")
        topic = input("What topic did you study today? ")
        if subject not in subjects_AND_topics:
            subjects_AND_topics[subject] = topic
        else:
            print("This in the list.")
            continue

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

    return subjects_AND_topics, topic, study_time, difficulty, completion


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
