def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Value must be a positive number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def get_int_in_range(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def get_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ("yes", "no"):
            return value
        else:
            print("Invalid input. Please type 'yes' or 'no'.\n")


def ask_question():
    subjects_and_topics = {}

    print("\n--- Study Input Section ---\n")
    subject_number = get_positive_int("How many subjects did you study today? : ")

    for _ in range(subject_number):
        print("\n------------------------------")
        subject = input("Subject name            : ").strip()
        topic = input("Topic studied           : ").strip()

        study_time = get_positive_int(f"Study time for {subject} (minutes): ")

        difficulty = get_int_in_range("Difficulty level (1 - 5)          : ", 1, 5)

        completion = get_yes_no("Did you solve at least one problem? (yes/no): ")

        if subject not in subjects_and_topics:
            subjects_and_topics[subject] = {
                "topic": topic,
                "time": study_time,
                "difficulty": difficulty,
                "completion": completion
            }
        else:
            print(f"\n'{subject}' already exists. Entry skipped.\n")

    return subjects_and_topics

def main():
    subject_detailes = ask_question()

    print("\n" + "=" * 60)
    print("DAILY STUDY REPORT")
    print("=" * 60)

    for subject, inside in subject_detailes.items():
        minutes = inside["time"]
        hours = minutes / 60

        print(f"\nSubject        : {subject}")
        print("-" * 60)

        if minutes >= 60:
            print(f"Study Time     : {hours:.2f} hours ({minutes} minutes)")
        else:
            print(f"Study Time     : {minutes} minutes")

        print(f"Topic          : {inside['topic']}")
        print(f"Difficulty     : {inside['difficulty']} / 5")
        print(f"Problem Solved : {inside['completion']}")

        print("\nFeedback:")

        if minutes < 30:
            print("> Very short session. Retention may be low.")

        elif minutes < 60 and inside['completion'] == "no":
            print("> Passive studying detected.")
            print("> Try solving at least one problem next time.")

        elif minutes >= 60 and inside['completion'] == "no":
            print("> Long session without problem-solving.")
            print("> Effort is good, but application is missing.")

        elif minutes >= 60 and inside['completion'] == "yes":
            print("> Excellent balance of study and practice.")

        else:
            print("> Session looks balanced.")

    print("\n" + "=" * 60)
    print("End of Report")
    print("=" * 60)


if __name__ == "__main__":
    main()
