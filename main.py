import os

def display_intro():
    print("Welcome to My Programming Portfolio!")
    print("This portfolio showcases the programming projects I am most proud of.")
    print("Use the menu below to explore the projects and learn more about them.\n")

def display_menu():
    print("Menu:")
    print("1. Project 1: Calculator")
    print("2. Project 2: Weather App")
    print("3. Project 3: To-Do List")
    print("4. Project 4: Chatbot")
    print("5. Project 5: Game (Tic-Tac-Toe)")
    print("6. Project 6: Data Visualizer")
    print("7. Exit")
    print()

def display_project_details(project_number):
    project_details = {
        1: {
            "name": "Calculator",
            "description": "A simple calculator that performs basic arithmetic operations.",
            "process": "I enjoyed implementing the logic for different operations.",
            "learning": "I learned about handling user input and error checking.",
            "role": "Individual project"
        },
        2: {
            "name": "Weather App",
            "description": "An app that fetches and displays weather data for a given location.",
            "process": "It was challenging to work with APIs but rewarding.",
            "learning": "I learned how to use APIs and parse JSON data.",
            "role": "Individual project"
        },
        3: {
            "name": "To-Do List",
            "description": "A simple app to manage daily tasks.",
            "process": "I enjoyed designing the user interface.",
            "learning": "I learned about file handling and persistence.",
            "role": "Individual project"
        },
        4: {
            "name": "Chatbot",
            "description": "A chatbot that can answer basic questions.",
            "process": "It was fun to implement natural language processing.",
            "learning": "I learned about string manipulation and basic AI concepts.",
            "role": "Individual project"
        },
        5: {
            "name": "Game (Tic-Tac-Toe)",
            "description": "A two-player Tic-Tac-Toe game.",
            "process": "I enjoyed implementing the game logic.",
            "learning": "I learned about game loops and condition checking.",
            "role": "Individual project"
        },
        6: {
            "name": "Data Visualizer",
            "description": "A tool to visualize data using charts and graphs.",
            "process": "It was exciting to work with data visualization libraries.",
            "learning": "I learned about matplotlib and data analysis.",
            "role": "Individual project"
        }
    }

    details = project_details.get(project_number)
    if details:
        print(f"Project: {details['name']}")
        print(f"Description: {details['description']}")
        print(f"Programming Process: {details['process']}")
        print(f"Learning Experience: {details['learning']}")
        print(f"Role: {details['role']}")
        print()
    else:
        print("Invalid project number.\n")

def main():
    display_intro()
    while True:
        display_menu()
        choice = input("Enter the number of the project you want to view (or 7 to exit): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 7:
                print("Thank you for exploring my portfolio!")
                break
            elif 1 <= choice <= 6:
                display_project_details(choice)
            else:
                print("Invalid choice. Please select a valid option.\n")
        else:
            print("Please enter a number.\n")

if __name__ == "__main__":
    main()