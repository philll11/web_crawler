import shutil as Shutil
import os

# Deleting a directory
def delete_dir(directory):
    if os.path.exists(directory):
        Shutil.rmtree(directory)

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

def create_error_file(directory):
    if os.path.exists(directory):
        error = directory + '/error.txt'
        delete_file_contents(error)
    else:        
        error = directory + '/error.txt'
        write_file(error, '')
    
# Create a new file
def write_file(file_name, data):
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write(data)

def write_error_file(directory, data):
    file_path = directory + '/error.txt'
    with open(file_path, 'a', encoding="utf-8") as f:
        f.write(data + '\n')
        
# Delete content of a file
def delete_file_contents(file_name):
    with open(file_name, 'w', encoding="utf-8"):
        pass

# Convert file to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# Convert set to file
def set_to_file(links, file_name):
    delete_file_contents(file_name)    
    with open(file_name, 'a', encoding="utf-8") as f:
        for link in links.copy():
            f.write(link + '\n')

