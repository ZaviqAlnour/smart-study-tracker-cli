def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Value must be positive.")
        except ValueError:
            print("Please enter a valid number.")

def get_int_in_range(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Value must be between {min_value} and {max_value}.")
        except ValueError:
            print("Please enter a valid number.")

def get_yes_no(prompt):
    while True:
        value = input(prompt).lower()
        if value in ("yes", "no"):
            return value
        else:
            print("Please type 'yes' or 'no'.")

def ask_question():
    subjects_and_topics = {}
    subject_number = get_positive_int("How many subjects did you study today? ")

    for _ in range(subject_number):
        subject = input("Enter the subject you studied today: ")
        topic = input("What topic did you study today? ")

        study_time = get_positive_int(f"How many minutes did you study {subject} today? ")
        difficulty = get_int_in_range("How difficult was it? (1-5): ", 1, 5)
        completion = get_yes_no("Did you complete a problem? (yes/no): ")

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
    subject_detailes = ask_question()


if __name__ == "__main__":
    main()
