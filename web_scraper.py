from bs4 import BeautifulSoup
import requests

url = "https://help.botpenguin.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


t1 = soup.find(class_='grid-area-1-1 z-[1] mt-[1em]').text

t2 = soup.find(class_="w-full mx-auto decoration-primary/6 max-w-3xl page-api-block:ml-0").text
t = t1 + "\n" + t2 + "\n"




v = True
#the next page
m = "/botpenguin-resource-centre/how-botpenguin-works/onboarding"

while(v):
    u = url+m

    response = requests.get(u)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    #text inside that page
    txt = soup.find(class_="[&>*+*]:mt-5 grid whitespace-pre-wrap")

    #link for the next page
    a = soup.find(class_="group text-sm p-2.5 flex gap-4 flex-1 flex-row items-center pr-4 border border-dark/3 rounded straight-corners:rounded-none hover:border-primary/6 dark:border-light/2 text-pretty dark:hover:border-primary-300/4 md:p-4 md:text-base")

    if(txt):
        t = t + txt.text + "\n"
    v = a
    if(v):
        m = a['href']

file_path = "content.txt"

# Save the content to a txt file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(t)
