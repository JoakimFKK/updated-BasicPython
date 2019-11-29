import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

name_start = html.find("Name:")
name_end = name_start + 5
print(html[name_start:name_end])

color_start = html.find("Favorite Color:")
color_end = color_start + len("Favorite Color:")
print(html[color_start:color_end])

pattern = "<.*?>Name:<.*?>"

match_name = re.search(pattern, html, re.IGNORECASE)
name_result = match_name.group()

print(name_result)