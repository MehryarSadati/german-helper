# import requests
# from bs4 import BeautifulSoup

# url = 'https://dic.b-amooz.com/de/dictionary/'

# def search_website(url, keyword):
#     r = requests.get(url)

#     if r.status_code != 200:
#         print(f"Error: Unable to fetch the webpafge. Status code: {r.status_code}")
#         return
    
#     soup = BeautifulSoup(r.text, "html.parser")
#     results = soup.find_all(string=lambda text:keyword.lower() in text.lower() if text else False)

#     if results:
#         print(f"Found {len(results)} matches for '{keyword}'")
#         for i, result in enumerate(result, 1):
#             print(f"{i}, {result.strpi()}")

#     else:
#         print(f"No results found for '{keyword}'")


# search_website(url, "hemd")