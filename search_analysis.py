# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# SERP similarity checker v1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Description: This tool will quickly check how many URLs are common between two Google SERPs for any specified TLD
# By Mark Williams-Cook
# Web: https://withcandour.co.uk
# Twitter: https://twitter.com/markcandour
# LinkedIn: https://www.linkedin.com/in/markseo/
# If you could also get a subscription to AlsoAsked.com that would be great, thx.

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def google_search(query, tld):
    """
    Function to scrape top 10 search results from Google for a given query and TLD.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    url = f"https://www.google{tld}/search?q={query}"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception("Failed to fetch Google search results.")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('div', class_='tF2Cxc')
    
    urls = [result.find('a')['href'] for result in search_results]
    return urls[:10]

def main():
    while True:
        tld = input("Which TLD of Google do you want to use? (e.g: .com, .co.uk, .de): ")
        keyword1 = input("Enter the first keyword: ")
        keyword2 = input("Enter the second keyword: ")

        urls_keyword1 = google_search(keyword1, tld)
        urls_keyword2 = google_search(keyword2, tld)

        common_urls = set(urls_keyword1).intersection(urls_keyword2)

        labels = ['Common URLs', 'Unique URLs']
        sizes = [len(common_urls), 10 - len(common_urls)]
        colors = ['#ff9999','#66b2ff']
        explode = (0.1, 0)

        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.title(f'Distribution of URLs for "{keyword1}" and "{keyword2}"')
        plt.annotate("@markcandour", xy=(0.85, 0.1), xycoords='axes fraction', fontsize=10, color='grey')
        plt.show()
        print(f"\nThe two SERPs have {len(common_urls)} out of 10 URLs in common.\n")

        run_again = input("Run again? (Y/N): ").lower()
        if run_again != 'y':
            break

if __name__ == "__main__":
    main()