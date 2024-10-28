import csv
import requests
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-09-28&sortBy=publishedAt&apiKey="


response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("news_tesla.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        writer.writerow(["Author", "Title", "Description"])

        for article in data["articles"]:
            author = article["author"]
            title = article["title"]
            description = article["description"]
            
            writer.writerow([author, title, description])

    print("Данные успешно сохранены в news_tesla.csv")
else:
    print(f"Ошибка: {response.status_code}")