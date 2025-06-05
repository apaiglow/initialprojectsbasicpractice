import requests

photo = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')

photoj = photo.json()
print(f"Date: {photoj['date']}\n")
print(f"Title: {photoj['title']}\n")
print(f"Explanation: {photoj['explanation']}\n")
print(f"Image URL: {photoj['url']}\n")

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{photoj['title']}</title>
</head>
<body>
    <h1>{photoj['title']}</h1>
    <p><em>{photoj['date']}</em></p>
    <img src="{photoj['url']}" alt="{photoj['title']}" style="max-width:100%;height:auto;">
    <p>{photoj['explanation']}</p>
</body>
</html>
"""

date_str = photoj['date']  # e.g. '2025-06-05'
filename = f"nasa_photo_{date_str}.html"
with open("nasa_photo.html", "w", encoding="utf-8") as file:
    file.write(html_content)