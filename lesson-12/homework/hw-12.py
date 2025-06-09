##Task1

from bs4 import BeautifulSoup


HTML_FILE = "weather.html"

def load_html(filename):
    """Load and parse HTML file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return BeautifulSoup(file, "html.parser")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        exit(1)

def extract_weather_data(soup):
    """Extract weather forecast data from BeautifulSoup object."""
    data = []
    rows = soup.select("tbody tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 3:
            day = cols[0].text.strip()
            temperature = int(cols[1].text.replace("°C", "").strip())
            condition = cols[2].text.strip()
            data.append({"day": day, "temperature": temperature, "condition": condition})
    return data

def display_weather(data):
    """Display the weather forecast neatly."""
    print("  5-Day Weather Forecast:\n")
    for entry in data:
        print(f" - {entry['day']:<9} |  {entry['temperature']}°C |   {entry['condition']}")
    print()

def analyze_weather(data):
    """Analyze and print weather statistics."""
    max_temp = max(entry["temperature"] for entry in data)
    hottest_days = [entry["day"] for entry in data if entry["temperature"] == max_temp]

    sunny_days = [entry["day"] for entry in data if entry["condition"].lower() == "sunny"]

    avg_temp = sum(entry["temperature"] for entry in data) / len(data)

    print(" Weather Analysis:\n")
    print(f"  Highest Temperature : {max_temp}°C on {', '.join(hottest_days)}")
    print(f"  Sunny Days          : {', '.join(sunny_days)}")
    print(f"  Average Temperature : {avg_temp:.1f}°C\n")

def main():
    soup = load_html(HTML_FILE)
    weather_data = extract_weather_data(soup)

    if not weather_data:
        print("No weather data found.")
        return

    display_weather(weather_data)
    analyze_weather(weather_data)

if __name__ == "__main__":
    main()



##Task2

import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
import logging
import argparse
from typing import List, Optional, Tuple, Dict

DB_FILE = "jobs.db"
CSV_FILE = "filtered_jobs.csv"
SOURCE_URL = "https://realpython.github.io/fake-jobs"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def init_db(db_file: str = DB_FILE) -> sqlite3.Connection:
    conn = sqlite3.connect(db_file)
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                location TEXT NOT NULL,
                description TEXT NOT NULL,
                apply_link TEXT NOT NULL,
                UNIQUE(title, company, location)
            );
        """)
    return conn

def fetch_jobs(url: str = SOURCE_URL) -> List[Dict[str, str]]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for card in soup.select(".card-content"):
        try:
            job = {
                "title": card.find("h2", class_="title").text.strip(),
                "company": card.find("h3", class_="company").text.strip(),
                "location": card.find("p", class_="location").text.strip(),
                "description": card.find("div", class_="content").text.strip(),
                "apply_link": card.find("a", string="Apply")["href"]
            }
            jobs.append(job)
        except Exception as e:
            logging.warning(f"Skipping a job due to error: {e}")
    return jobs

def save_jobs(conn: sqlite3.Connection, jobs: List[Dict[str, str]]) -> Tuple[int, int]:
    cur = conn.cursor()
    inserted, updated = 0, 0

    for job in jobs:
        cur.execute("""
            SELECT description, apply_link FROM jobs
            WHERE title=? AND company=? AND location=?
        """, (job["title"], job["company"], job["location"]))
        row = cur.fetchone()

        if row is None:
            cur.execute("""
                INSERT INTO jobs (title, company, location, description, apply_link)
                VALUES (?, ?, ?, ?, ?)
            """, (job["title"], job["company"], job["location"], job["description"], job["apply_link"]))
            inserted += 1
        elif row != (job["description"], job["apply_link"]):
            cur.execute("""
                UPDATE jobs
                SET description=?, apply_link=?
                WHERE title=? AND company=? AND location=?
            """, (job["description"], job["apply_link"], job["title"], job["company"], job["location"]))
            updated += 1

    conn.commit()
    return inserted, updated

def filter_jobs(conn: sqlite3.Connection, company: Optional[str], location: Optional[str]) -> List[Tuple]:
    query = "SELECT title, company, location, description, apply_link FROM jobs WHERE 1=1"
    params = []

    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")

    cur = conn.cursor()
    cur.execute(query, params)
    return cur.fetchall()

def export_jobs_to_csv(jobs: List[Tuple], filename: str = CSV_FILE) -> None:
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location", "Description", "Apply Link"])
        writer.writerows(jobs)
    logging.info(f" Exported {len(jobs)} job(s) to '{filename}'")

def parse_args():
    parser = argparse.ArgumentParser(description="Job scraper for fake job listings.")
    parser.add_argument("--company", help="Filter by company name")
    parser.add_argument("--location", help="Filter by location")
    parser.add_argument("--export", action="store_true", help="Export filtered jobs to CSV")
    return parser.parse_args()

def main():
    args = parse_args()
    conn = init_db()

    logging.info(" Fetching jobs...")
    jobs = fetch_jobs()

    inserted, updated = save_jobs(conn, jobs)
    logging.info(f" Inserted: {inserted},  Updated: {updated}")

    if args.company or args.location:
        filtered_jobs = filter_jobs(conn, args.company, args.location)
        logging.info(f" Found {len(filtered_jobs)} matching job(s).")

        if args.export:
            export_jobs_to_csv(filtered_jobs)
    conn.close()

if __name__ == "__main__":
    main()



##Task3


import requests
from bs4 import BeautifulSoup
import json
from typing import List, Dict, Optional

BASE_URL = "https://www.demoblaze.com"


def get_soup(url: str) -> BeautifulSoup:
    """Fetch a URL and return a BeautifulSoup object."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        raise
    return BeautifulSoup(response.text, "html.parser")


def scrape_laptop_list_page(url: str) -> List[Dict[str, str]]:
    """
    Scrape laptop entries from the laptops category page.
    Returns a list of dicts with 'name', 'price', and 'description'.
    """
    soup = get_soup(url)
    laptops = []

    product_cards = soup.select("#tbodyid .col-lg-4.col-md-6.mb-4")
    if not product_cards:
        print("No laptops found on the page.")
        return laptops

    for card in product_cards:
        name_tag = card.find("a", class_="hrefch")
        price_tag = card.find("h5")

        if not name_tag or not price_tag:
            continue

        name = name_tag.text.strip()
        price = price_tag.text.strip()
        detail_href = name_tag.get("href", "")
        detail_url = f"{BASE_URL}/{detail_href}" if detail_href else None

        description = scrape_laptop_description(detail_url) if detail_url else "No description available."

        laptops.append({
            "name": name,
            "price": price,
            "description": description
        })

    return laptops


def scrape_laptop_description(url: Optional[str]) -> str:
    """
    Scrape the laptop description from the laptop's detail page.
    """
    if url is None:
        return "No description available."

    soup = get_soup(url)
    desc_tag = soup.select_one("#more-information .tab-content .tab-pane.fade.active.show p")
    if desc_tag and desc_tag.text.strip():
        return desc_tag.text.strip()

    desc_fallback = soup.select_one(".tab-content .tab-pane.fade.active.show")
    if desc_fallback and desc_fallback.text.strip():
        return desc_fallback.text.strip()

    return "No description available."


def main():
    laptops_url = f"{BASE_URL}/category.html?id=2" 

    print("Scraping laptops from Demoblaze...")
    laptops = scrape_laptop_list_page(laptops_url)

    print(f"Found {len(laptops)} laptops.")

    with open("laptops.json", "w", encoding="utf-8") as json_file:
        json.dump(laptops, json_file, indent=2, ensure_ascii=False)

    print("Saved laptops data to laptops.json")


if __name__ == "__main__":
    main()
