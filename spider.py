from urllib.request import urlopen
from link_finder import LinkFinder
from utility import *


class Spider:

    directory = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()    
    
    def __init__(self, directory, base_url, domain_name):
        Spider.directory = directory
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.directory + '/queue.txt'
        Spider.queue_file = Spider.directory + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod    
    def boot():
        create_new_dir(Spider.directory)
        create_data_file(Spider.directory, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        
