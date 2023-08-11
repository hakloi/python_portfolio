# constatnt time - It means the time taken will stay the same, regardless of how 
# big the hash table is.

cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url] 
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
