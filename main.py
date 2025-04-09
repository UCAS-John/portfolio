import tkinter as tk
from tkinter import messagebox
import os
import subprocess

# Function to display project details
def show_project_details(project):
    details = {
        "Coin Change": {
            "description": "A program that calculates the minimum number of coins needed to make a given amount.",
            "process": "I found the process enjoyable when trying to solve the coin problems.",
            "learning": "I learned how to implement GUI using python library tkinter",
        },
        "Movie Recommender": {
            "description": "A program that recommends movies based on user filters.",
            "process": "It was challenging trying to figure out how to filter movies correctly.",
            "learning": "I learned lis t comeprehension and how to work with CSV files.",
        },
        "Personal Library": {
            "description": "A program to manage a collection of books, including adding, removing, and searching for books.",
            "process": "I enjoy dealing with large dictioanry.",
            "learning": "I learned how to deal with python dictionary effectively",
        },
        "Random Password Generator": {
            "description": "A program to generate secure, random passwords based on user-defined criteria.",
            "process": "It was fun to generate password base on user criteria.",
            "learning": "I learned how to use random library and string module.",
        },
        "Todo List": {
            "description": "A program to manage todo list, allowing users to add, edit, and delete todo.",
            "process": "I enjoyed making Todo list as a class and trying to come up with a way to use txt file as a todo list.",
            "learning": "I learned how to deal with txt file.",
        },
        "Word Count": {
            "description": "A program that counts the number of words, characters, and lines in a given text.",
            "process": "It was fun to divide the program into multiple pages. I think it more organized and easier to deal with.",
            "learning": "I learned about how to use time module and count words.",
        }
    }
    project_info = details.get(project, {})
    if project_info:
        messagebox.showinfo(
            project,
            f"Description: {project_info['description']}\n\n"
            f"Process: {project_info['process']}\n\n"
            f"Learning: {project_info['learning']}\n\n"
        )

# Function to run the selected project
def run_project(project):
    project_scripts = {
        "Coin Change": os.path.join(os.path.dirname(os.path.abspath(__file__)), "projects", "coin_change", "main.py"),
        "Movie Recommender": os.path.join(os.path.dirname(os.path.abspath(__file__)), "projects", "movie_recommender", "main.py"),
        "Personal Library": os.path.join(os.path.dirname(os.path.abspath(__file__)), "projects", "personal_library", "main.py"),
        "Random Password Generator": os.path.join(os.path.dirname(os.path.abspath(__file__)), "projects", "random_password_generator", "main.py"),
        "Todo List": os.path.join(os.path.dirname(os.path.abspath(__file__)), "projects", "todo_list", "main.py"),
        "Word Count": os.path.join(os.path.dirname(os.path.abspath(__file__)), "projects", "word_count ", "main.py")
    }
    script_path = project_scripts.get(project)
    if script_path and os.path.exists(script_path):
        subprocess.run(["python", script_path])
    else:
        messagebox.showerror("Error", f"Script for {project} not found!")

# Main application
def main():
    root = tk.Tk()
    root.title("Personal Portfolio")

    # Introduction
    intro_label = tk.Label(
        root,
        text="Welcome to My Programming Portfolio!\n\n"
             "This portfolio showcases the programming projects I'm most proud of.\n"
             "Select a project from the menu to learn more or run it.",
        justify="center",
        padx=10,
        pady=10
    )
    intro_label.pack()

    # Menu
    menu_label = tk.Label(root, text="Projects Menu", font=("Arial", 14, "bold"))
    menu_label.pack(pady=10)

    projects = ["Coin Change", "Movie Recommender", "Personal library", "Random Password Generator", "Todo List", "Word Count"]
    for project in projects:
        frame = tk.Frame(root)
        frame.pack(pady=5)

        details_button = tk.Button(frame, text=f"Details: {project}", command=lambda p=project: show_project_details(p))
        details_button.pack(side="left", padx=5)

        run_button = tk.Button(frame, text=f"Run: {project}", command=lambda p=project: run_project(p))
        run_button.pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()