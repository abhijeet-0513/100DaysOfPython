"""
main.py
100DaysOfCode - Course brief and repo helper

This script contains a detailed brief about the Udemy "100 Days of Code" Python course and provides utility functions to:
 - print a readable course brief to the console
 - generate a README.md for the repository
 - create per-day template files and a directory structure for the 100 day challenge
 - list suggested projects, resources, and study tips

Guidelines embedded in this brief:
 - Course goal: teach Python from scratch to mastery, covering core Python, 
   web development, data science, GUI, web scraping, and more.
 - Structure: 100 days. Each day focuses on a concept or small set of concepts,
   with regular project builds that combine learned material.
 - Usage: run this file to print the brief, or import the helper functions in your
   own scripts to generate files and folder scaffolding for the challenge.

Note: This file intentionally avoids visual check marks or other symbolic glyphs.

Author: Abhijeet Singh
Created: 2025-10-13

"""

import os
from pathlib import Path
from textwrap import dedent

# ----------------------------- Configuration -----------------------------
COURSE_TITLE = "100 Days of Code - Python (Udemy)"
ROOT_DIR = Path(__file__).parent.resolve()
DAYS = 100
DAY_TEMPLATE_FILENAME = "day_{:03d}.md"
MAIN_README = "README.md"

# ----------------------------- Course Content ----------------------------
COURSE_OVERVIEW = dedent(f"""
{COURSE_TITLE}

Overview
--------
This course is designed to take you from a complete beginner to confident
Python developer. It covers core Python concepts, best practices, and multiple
application domains, including:

- Core Python: variables, data types, control flow, functions, OOP, modules,
  error handling, testing and packaging.
- Web development: fundamentals of HTTP, Flask and/or Django basics, building
  REST APIs, templating, authentication, and deployment basics.
- Data science: NumPy, pandas, basic statistics, data visualization, and an
  end-to-end mini project analyzing a dataset.
- GUI: building desktop apps with Tkinter (or PySimpleGUI) and event-driven
  programming basics.
- Web scraping: requests, BeautifulSoup, handling pagination, rate limiting,
  and polite scraping.
- Automation & scripting: file handling, CSV/JSON processing, interacting with
  external APIs, and practical automation tasks.

Course structure
----------------
There are 100 days. Typical day pattern:
1. Concept introduction (short reading + code examples)
2. Guided exercises to practice the concept
3. Short challenge or mini-task to apply learning
4. Periodic project days where multiple concepts are combined into a
   real-world project.

Every 7-10 days you will find a "project day" to consolidate learning.
The course culminates in several capstone projects spanning different
domains.

Learning objectives
-------------------
By the end of the course you should be able to:
- Write idiomatic Python code and use common standard-library modules.
- Build small to medium web applications and REST APIs.
- Perform basic data analysis and visualizations.
- Write GUI applications for desktop use-cases.
- Scrape and process data from the web responsibly.
- Design and complete end-to-end projects and publish them (GitHub).

""")

# ----------------------------- Project Suggestions -----------------------
PROJECT_LIST = [
    "Personal portfolio website (Flask) with contact form and blog",
    "To-do app with persistent storage and authentication",
    "Data analysis project: analyze a public dataset (CSV) and visualize insights",
    "Web scraper that collects structured data and exports to CSV",
    "Desktop GUI app (expense tracker) using Tkinter or PySimpleGUI",
    "REST API for a simple resource with token-based auth",
    "Automation script: batch file renamer / CSV merger / email sender",
]

# ----------------------------- Helper functions --------------------------

def print_brief():
    """Print a well-formatted brief to the console."""
    print(COURSE_OVERVIEW)
    print("Suggested projects:\n")
    for i, p in enumerate(PROJECT_LIST, start=1):
        print(f"{i}. {p}")
    print("\nStudy tips:\n")
    for tip in get_study_tips():
        print(f"- {tip}")


def get_study_tips():
    """Return a list of short study tips."""
    return [
        "Follow the daily plan but be flexible — consistency beats intensity.",
        "Code every day. Even 30-60 minutes daily is highly effective.",
        "Write small programs that solve real problems you care about.",
        "Read and run examples, then modify them to see different behaviors.",
        "Use version control (git) and push your work to GitHub frequently.",
        "Write tests for non-trivial code — testing clarifies design.",
        "When stuck, break the problem into smaller parts and debug step by step.",
        "Discuss your solutions in community forums or with a study partner.",
    ]


def generate_readme(destination: Path = None):
    """Generate a README.md summarizing the course and repository layout.

    Returns the path to the generated file.
    """
    if destination is None:
        destination = ROOT_DIR / MAIN_README

    content = dedent(f"""
    # {COURSE_TITLE}

    This repository contains notes, exercises, and projects for the
    "{COURSE_TITLE}" Udemy course. The course teaches core Python and
    multiple application areas over 100 days. Each day has a short note file
    and exercises.

    ## How to use this repo

    1. Run `python main.py` to print a course brief and see helper scripts.
    2. Use `python main.py --init` to scaffold the `days/` folder with
       day template files (optional).
    3. Keep your solutions in `days/day_XXX/` or `solutions/` as you prefer.

    ## Project ideas

    """ )

    for p in PROJECT_LIST:
        content += f"- {p}\n"

    content += "\nGood luck and happy coding!\n"

    destination.write_text(content, encoding="utf-8")
    return destination


def create_day_template(day: int, folder: Path = None):
    """Create a markdown template for a given day.

    Example file: days/day_001/day_001.md or days/day_001.md depending on
    your preferred layout.
    """
    if day < 1 or day > DAYS:
        raise ValueError(f"day must be between 1 and {DAYS}")

    if folder is None:
        folder = ROOT_DIR / "days"

    folder.mkdir(parents=True, exist_ok=True)
    day_folder = folder / f"day_{day:03d}"
    day_folder.mkdir(parents=True, exist_ok=True)

    filename = day_folder / DAY_TEMPLATE_FILENAME.format(day)
    template = dedent(f"""
    # Day {day:03d}

    ## Topic
    Brief description of the topic(s) for day {day}.

    ## Goals
    - Explain what you should be able to do after completing this day.

    ## Notes
    - Add code snippets, explanations, and links here.

    ## Exercises
    1. Exercise 1 - write and run code that demonstrates the core idea.
    2. Exercise 2 - small challenge to apply the concept.

    ## Reflection
    - What did you find difficult? What was easy?

    ## Links / Resources
    - Useful links, docs, or videos used for this day.
    """)

    filename.write_text(template, encoding="utf-8")
    return filename


def scaffold(days: int = DAYS, folder: Path = None):
    """Create folder structure and templates for all days.

    This will create `days/day_001/` .. `days/day_100/` each containing a
    day_XXX.md file. Be careful: this function will create directories and
    files if they do not already exist.
    """
    if folder is None:
        folder = ROOT_DIR / "days"

    for day in range(1, days + 1):
        create_day_template(day, folder=folder)

    return folder

# ----------------------------- CLI support -------------------------------
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Helpers for 100DaysOfCode repo")
    parser.add_argument("--print", action="store_true", help="Print the course brief")
    parser.add_argument("--init", action="store_true", help="Scaffold days/ templates")
    parser.add_argument("--readme", action="store_true", help="Generate README.md")
    parser.add_argument("--day", type=int, help="Create a single day template (day number)")

    args = parser.parse_args()

    if args.print:
        print_brief()

    if args.readme:
        path = generate_readme()
        print(f"Generated {path}")

    if args.init:
        folder = scaffold()
        print(f"Scaffolded {folder} (created {DAYS} day templates)")

    if args.day:
        path = create_day_template(args.day)
        print(f"Created template: {path}")

    if not (args.print or args.init or args.readme or args.day):
        # default action: print brief
        print_brief()
