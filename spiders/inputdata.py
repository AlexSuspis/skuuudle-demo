from typing import List

client_name: str = 'Rusholme Off-licence'

#List of items client wants to do a market study on
    #We will each of call these client items a 'search_term' as it's more relevant for our scraping.
search_terms: List[str] = [
                            'milk',
                            'peanut%20butter',
                            'chocolate',
                            'sugar',
                            ]

#Base url string to which we will append the search term
base_search_url = "https://www.tesco.com/groceries/en-GB/search?query="

#Generate all links used by TescoSpider's start_url property
def generate_start_urls() -> List[str]:

    start_urls: List[str] = []
    
    #Create final search url by concatenating base url and item name we are searching for
    for item_name in search_terms:
        final_url = base_search_url + item_name
        start_urls.append(final_url)

    return start_urls