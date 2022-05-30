import requests
from bs4 import BeautifulSoup
YOUTUBE_TRENDING_MOVIES = "https://www.youtube.com/feed/trending?bp=4gIKGgh0cmFpbGVycw%3D%3D"
response = requests.get(YOUTUBE_TRENDING_MOVIES)

print("status code",response.status_code)

with open('trending.html','w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text,'html.parser')
print('Page title',doc.title)

# Find all the divs
video_divs = doc.find_all('div',class_= 'style-scope ytd-video-renderer')
print('found {} videos'.format(len(video_divs)))