import requests
from json_read import json_reader

def search_item(search_query: str, page_number: int):
    """
    Inputs:
        - search_query: string
        - page_number: integer
    
    Output:
        - result: dict or list (depending on the JSON output)    
    
    """
    url = "https://aliexpress-datahub.p.rapidapi.com/item_search"

    querystring = {"q":search_query,"page":page_number}

    headers = {
        json_reader("X-RapidAPI-Key"),
        json_reader("X-RapidAPI-Host")
    }

    response = requests.get(url, headers=headers, params=querystring)

    result = response.json()

    return result

def retrieve_item_pages(search_query: str):
    """
    Inputs:
        - search_query (string): Query that a user submits to get item information
    
    Output:
        - page_results (list): List of results from API for first 2 pages
    """
    # Page Results
    page_results = []
    
    # Iterate over the first 2 pages
    for i in range(1, 3):
        result = search_item(search_query, i)
        page_results.append(result)
    
    return page_results