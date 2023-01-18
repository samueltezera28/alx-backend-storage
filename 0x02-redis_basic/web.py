#!/usr/bin/env python3
"""
create a web cach
"""
from typing import Optional
from functools import wraps
from cachetools import TTLCache


def get_page(url: str) -> str:
    """ get a page and cach value"""
    if f"count:{url}" in cache:
        cached_count = cache[f"count:{url}"]
        cache[f"count:{url}"] = cached_count + 1
    else:
        cache[f"count:{url}"] = 1
    
    response = requests.get(url).text
    return response



def memozise(method):
    @wraps(method)
    def inner(url:str) -> str:
        if f"count:{url}" in cache: 
            cached_count = cache[f"count:{url}"]
            cache[f"count:{url}"] = cached_count + 1
        else:
            cache[f"count:{url}"] = 1 
            method_response = method(url)
            cache[url] = method_response
        return cache[url]
    return inner

@memozise
def get_page(url: str) -> str:
    return requests.get(url).text

if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk/delay/2000/url/https://www.python.org")
    print(f"Total access of URL: {cache['count:http://slowwly.robertomurray.co.uk/delay/2000/url/https://www.python.org']}")
