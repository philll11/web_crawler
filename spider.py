from urllib.request import urlopen
from link_finder import LinkFinder
from utility import *
import sys


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
        Spider.crawled_file = Spider.directory + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod    
    def boot():
        create_new_dir(Spider.directory)
        create_data_file(Spider.directory, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url + '\n')
            print('Queued: ' + str(len(Spider.queue)) + ' | Crawled: ' +  str(len(Spider.crawled)) + '\n')
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            try:
                Spider.queue.remove(page_url)
            except:
                print('Thread name: ' + thread_name)
                print('page_url: ' + page_url)
                print('queue: \n' + Spider.queue)
                sys.exit()
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)
            
    @staticmethod
    def gather_link(page_url):
        html_string = ''
        try:            
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html' or response.getheader('Content-Type') == 'text/html; charset=utf-8':
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: can not crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)

    








    
