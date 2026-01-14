Study Log (CLI)
What this program does

This is a simple command-line Python script for manually logging daily study activity.

It asks:

how many subjects you studied

what topic you studied in each subject

how long you studied (in minutes)

how difficult it felt (1–5)

whether you solved at least one problem

After collecting the input, it prints a readable study report and gives basic feedback based on:

time spent

whether any problem-solving was done

The goal is not productivity motivation, but to highlight passive studying vs active studying using very simple rules.

How it works (internals)

All data is stored in a dictionary structured like this:

{
    "Subject": {
        "topic": str,
        "time": int,        # minutes
        "difficulty": int,  # 1–5
        "completion": "yes" | "no"
    }
}


Time is input and compared in minutes

Time is displayed in hours when appropriate

No data is saved anywhere (no files, no database)

Everything is in-memory and resets on each run

Input validation

The program enforces:

positive integers for time

valid ranges for difficulty

strict yes / no answers

prevention of duplicate subject entries

If invalid input is given, the program keeps asking until valid input is provided.

Output logic

The report prints:

subject name

topic

study time (minutes or hours)

difficulty

whether a problem was solved

Then it prints feedback such as:

very short session

passive studying warnings

long study without application

confirmation of effective study

These messages are based on simple condition checks, not any advanced analysis.

Limitations (on purpose)

No file saving

No history or tracking over multiple days

No charts, no GUI

No external libraries

No object-oriented structure

This is intentionally kept simple and procedural.

Who this is for

Someone learning Python fundamentals

Someone practicing input validation and data structures

Someone who wants to understand how CLI programs are structured

Someone who wants immediate feedback on study habits without overengineering

What this is NOT

Not a productivity app

Not a learning platform

Not scalable

Not optimized for large data

Not meant to be “smart”

It does exactly what it says and nothing more.