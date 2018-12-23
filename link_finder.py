from html.parser import HTMLParser
from urllib import parse

DIRECTORY_NAME = 'Sahara Softwear'
HOMEPAGE = 'http://www.saharasoftwear.com/'

class LinkFinder(HTMLParser):

    
    
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def error(self, message):
        pass

    # Searches html for a tags and adds their href links to self.links.
    # Some relative website links do not have a complete url so the base url must be appended to the begining
    # of the url.
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links






