import tkinter as tk
from tkinter import messagebox
import os
import subprocess

# Function to display project details
def show_project_details(project):
    details = {
        "Coin Change": {
            "description": "A program that calculates the minimum number of coins needed to make a given amount.",
            "process": "I enjoyed building the logic for calculations and designing the UI.",
            "learning": "I learned about event-driven programming and GUI design.",
            "role": "Individual project."
        },
        "Movie Recommender": {
            "description": "A system that recommends movies based on user preferences or ratings.",
            "process": "It was challenging to work with APIs but rewarding.",
            "learning": "I learned how to use REST APIs and handle JSON data.",
            "role": "Individual project."
        },
        "Personal Library": {
            "description": "An application to manage a collection of books, including adding, removing, and searching for books.",
            "process": "I enjoyed implementing the database integration.",
            "learning": "I learned about CRUD operations and file handling.",
            "role": "Individual project."
        },
        "Random Password Generator": {
            "description": "A tool to generate secure, random passwords based on user-defined criteria.",
            "process": "It was fun to design the password generation logic.",
            "learning": "I learned about randomization and string manipulation.",
            "role": "Individual project."
        },
        "Todo List": {
            "description": "An application to manage tasks, allowing users to add, edit, and delete tasks with persistent storage.",
            "process": "I enjoyed working on the backend and routing.",
            "learning": "I learned about web frameworks and templating.",
            "role": "Individual project."
        },
        "Word Count": {
            "description": "A program that counts the number of words, characters, and lines in a given text.",
            "process": "It was exciting to work on text processing algorithms.",
            "learning": "I learned about string manipulation and file handling.",
            "role": "Individual project."
        }
    }
    project_info = details.get(project, {})
    if project_info:
        messagebox.showinfo(
            project,
            f"Description: {project_info['description']}\n"
            f"Process: {project_info['process']}\n"
            f"Learning: {project_info['learning']}\n"
            f"Role: {project_info['role']}"
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