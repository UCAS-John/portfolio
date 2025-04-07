import tkinter as tk
from tkinter import messagebox
import os
import subprocess

# Function to display project details
def show_project_details(project):
    details = {
        "Project 1": {
            "description": "This project is a calculator app that performs basic arithmetic operations.",
            "process": "I enjoyed building the logic for calculations and designing the UI.",
            "learning": "I learned about event-driven programming and GUI design.",
            "role": "Individual project."
        },
        "Project 2": {
            "description": "This project is a weather app that fetches real-time weather data.",
            "process": "It was challenging to work with APIs but rewarding.",
            "learning": "I learned how to use REST APIs and handle JSON data.",
            "role": "Individual project."
        },
        "Project 3": {
            "description": "This project is a to-do list app with persistent storage.",
            "process": "I enjoyed implementing the database integration.",
            "learning": "I learned about CRUD operations and file handling.",
            "role": "Individual project."
        },
        "Project 4": {
            "description": "This project is a simple game built with Python.",
            "process": "It was fun to design the game mechanics.",
            "learning": "I learned about game loops and collision detection.",
            "role": "Individual project."
        },
        "Project 5": {
            "description": "This project is a portfolio website built with Flask.",
            "process": "I enjoyed working on the backend and routing.",
            "learning": "I learned about web frameworks and templating.",
            "role": "Individual project."
        },
        "Project 6": {
            "description": "This project is a chatbot using natural language processing.",
            "process": "It was exciting to work with AI and machine learning.",
            "learning": "I learned about NLP libraries and chatbot design.",
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
        "Project 1": "projects/calculator.py",
        "Project 2": "projects/weather_app.py",
        "Project 3": "projects/todo_list.py",
        "Project 4": "projects/game.py",
        "Project 5": "projects/portfolio_website.py",
        "Project 6": "projects/chatbot.py"
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

    projects = ["Project 1", "Project 2", "Project 3", "Project 4", "Project 5", "Project 6"]
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