from urllib.parse import urlparse

#Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        if results[-1] == 'com':
            return results[-2] + '.' + results[-1]        
        elif results[-1] == 'nz' and results[-2] == 'co':
            return results[-3] + '.' + results[-2] + '.' + results[-1]
        else:
            return results[-2] + '.' + results[-1]
    except:
        return ''

# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

