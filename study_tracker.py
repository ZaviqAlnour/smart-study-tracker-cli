def ask_question():
    subjects_and_topics = {}
    subject_number = int(input("How many subjects did you study today? "))

    for _ in range(subject_number):
        subject = input("Enter the subject you studied today: ")
        topic = input("What topic did you study today? ")

        while True:
            try:
                study_time = int(input(f"How many minutes did you study {subject} today? "))
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

        if subject not in subjects_and_topics:
            subjects_and_topics[subject] = {
                "topic": topic,
                "time": study_time,
                "difficulty": difficulty,
                "completion": completion
            }
        else:
            print(f"{subject} is already in the list, skipping.")        

    return subjects_and_topics


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
