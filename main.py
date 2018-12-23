import threading
from queue import Queue
from spider import Spider
from domain import *
from utility import *

DIRECTORY_NAME = 'Sahara Softwear'
HOMEPAGE = 'http://www.saharasoftwear.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = DIRECTORY_NAME + '/queue.txt'
CRAWLED_FILE = DIRECTORY_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8 #Number of threads will depend on operating system capabilities
queue = Queue() #Thread queue
Spider(DIRECTORY_NAME, HOMEPAGE, DOMAIN_NAME)

# Create spider threads (will die when main exits)
def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

# Each queued is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# Check items in queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print('Links in queue: ' + str(len(queued_links)))
        create_jobs()
                


create_spiders()
crawl()
