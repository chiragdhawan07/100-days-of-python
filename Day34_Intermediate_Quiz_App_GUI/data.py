import requests
import html

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

question_data = [
    {
        "question": html.unescape(item["question"]),
        "correct_answer": item["correct_answer"]
    }
    for item in data["results"]
]
