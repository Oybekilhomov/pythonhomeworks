##Task1

import json
import csv
import requests

TASKS_FILE = 'tasks.json'
CSV_FILE = 'tasks.csv'
API_KEY = 'your_api_key_here'  
CITY = 'Tashkent'

def load_tasks():
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def display_tasks(tasks):
    print("\nTasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def calculate_stats(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    pending = total - completed
    average_priority = round(sum(t['priority'] for t in tasks) / total, 2) if total > 0 else 0

    print("\nTask Statistics:")
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Average priority: {average_priority}")

def convert_to_csv(tasks):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['ID', 'Task', 'Completed', 'Priority'])
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task': task['task'],
                'Completed': task['completed'],
                'Priority': task['priority']
            })
    print(f"\nTasks successfully written to {CSV_FILE}.")

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        print("\nCurrent Weather in", city)
        print(f"Temperature: {temp} °C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
    else:
        print("\nFailed to fetch weather data.")

def main():
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)
    convert_to_csv(tasks)

    tasks[0]['completed'] = True
    save_tasks(tasks)
    print("\nUpdated first task as completed and saved.")

    fetch_weather(Tashkent)

if __name__ == '__main__':
    main()


##Task2

import json
import csv
import requests
import random

TASKS_FILE = 'tasks.json'
CSV_FILE = 'tasks.csv'
API_KEY = 'your_openweather_api_key_here' 
CITY = 'Tashkent'
TMDB_API_KEY = 'your_tmdb_api_key_here'  


def load_tasks():
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def display_tasks(tasks):
    print("\nTasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def calculate_stats(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    pending = total - completed
    average_priority = round(sum(t['priority'] for t in tasks) / total, 2) if total > 0 else 0

    print("\nTask Statistics:")
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Average priority: {average_priority}")

def convert_to_csv(tasks):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['ID', 'Task', 'Completed', 'Priority'])
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task': task['task'],
                'Completed': task['completed'],
                'Priority': task['priority']
            })
    print(f"\nTasks successfully written to {CSV_FILE}.")

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        print("\nCurrent Weather in", city)
        print(f"Temperature: {temp} °C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
    else:
        print("\nFailed to fetch weather data.")

def recommend_movie_by_genre():
    genre_name = input("\nEnter a movie genre (e.g., Action, Comedy, Drama): ").capitalize()

    genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=en-US"
    genre_response = requests.get(genre_url)

    if genre_response.status_code != 200:
        print("Failed to fetch genres from TMDB.")
        return

    genres = genre_response.json()['genres']
    genre_dict = {genre['name']: genre['id'] for genre in genres}

    genre_id = genre_dict.get(genre_name)
    if not genre_id:
        print("Genre not found.")
        return

    discover_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres={genre_id}"
    discover_response = requests.get(discover_url)

    if discover_response.status_code != 200:
        print("Failed to fetch movies.")
        return

    movies = discover_response.json().get('results', [])
    if not movies:
        print("No movies found for this genre.")
        return

    movie = random.choice(movies)
    print("\nMovie Recommendation:")
    print(f"Title: {movie['title']}")
    print(f"Overview: {movie['overview']}")


def main():
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)
    convert_to_csv(tasks)

    tasks[0]['completed'] = True
    save_tasks(tasks)
    print("\nUpdated first task as completed and saved.")

    fetch_weather(CITY)
    recommend_movie_by_genre()

if __name__ == '__main__':
    main()
