import urllib.request

class AppURLopener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0'


page_url = 'https://www.investing.com/'
opener = AppURLopener()
response = opener.open(page_url)
print(response.getheader('Content-Type'))
