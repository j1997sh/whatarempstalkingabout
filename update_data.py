import json
import re
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup


TOPICS = [
    {
        "name": "NHS",
        "keywords": ["nhs", "hospital", "hospitals", "gp", "ambulance", "waiting list", "waiting lists"]
    },
    {
        "name": "Housing",
        "keywords": ["housing", "rent", "rents", "landlord", "homelessness", "mortgage"]
    },
    {
        "name": "Immigration",
        "keywords": ["immigration", "asylum", "refugee", "visa", "border", "small boats"]
    },
    {
        "name": "Economy",
        "keywords": ["economy", "inflation", "tax", "wages", "growth", "budget"]
    },
    {
        "name": "Climate",
        "keywords": ["climate", "net zero", "emissions", "renewable", "green energy"]
    }
]


def count_mentions(search_term):
    url = f"https://hansard.parliament.uk/search/Debates?house=commons&searchTerm={search_term}"

    headers = {
        "User-Agent": "whatarempstalkingabout/1.0"
    }

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(" ", strip=True).lower()

    total = 0

    for word in search_term.split():
        pattern = r"\b" + re.escape(word.lower()) + r"\b"
        total += len(re.findall(pattern, text))

    return total


def main():
    results = []

    for topic in TOPICS:
        mentions = 0

        for keyword in topic["keywords"]:
            try:
                mentions += count_mentions(keyword)
            except Exception as error:
                print(f"Could not fetch {keyword}: {error}")

        results.append({
            "name": topic["name"],
            "mentions": mentions,
            "trend": "up"
        })

    results.sort(key=lambda item: item["mentions"], reverse=True)

    output = {
        "lastUpdated": datetime.now().strftime("%d %B %Y"),
        "topics": results
    }

    Path("data.json").write_text(
        json.dumps(output, indent=2),
        encoding="utf-8"
    )

    print("Updated data.json from Hansard")


if __name__ == "__main__":
    main()
