

import os

# Each website we scrape will create a seperate directory
def create_new_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.mkdir(directory)

# Create queue and crawled files (if not created)
def create_data_file(directory, base_url):
    queue = directory + '/queue.txt'
    crawled = directory + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# Add data to existing file
def add_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')

# Delete content of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass

# Convert file to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# Convert set to file
def set_to_file(links, file_name):
    delete_file_contents(file_name)
    for link in links:
        add_to_file(file_name, link)
