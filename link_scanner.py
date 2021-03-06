from typing import List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
import sys
import urllib.error, urllib.request


def get_links(url):
    """Find all links on page at the given url.
    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    browser.get(url)
    link_list = []
    tag_list = browser.find_elements("tag name", "a")
    for link in tag_list:
        url = link.get_attribute('href')
        if url is not None:
            if '#' in url:
                link_list.append(url.split('#')[0])
            elif '?' in url:
                link_list.append(url.split('?')[0])
            else:
                link_list.append(url)
    return link_list


def is_valid_url(url: str):
    """Check if the url is valid and reachable.
    Returns:
        True if the URL is OK, False otherwise.
    """
    try:
        urllib.request.urlopen(url)
        return True
    except urllib.error.HTTPError:
        return False


def invalid_urls(urllist: List[str]) -> List[str]:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
    invalid_urls_list = []
    for url in urllist:
        if not is_valid_url(url):
            invalid_urls_list.append(url)
    return invalid_urls_list


if __name__ == "__main__":
    browser: WebDriver = webdriver.Chrome(r'C:\Users\DELL\Desktop\desktop\CODE\link_scanner\chromedriver.exe')
    url = sys.argv[1]
    links_list = get_links(url)
    bad_links_list = invalid_urls(links_list)

    # get good link
    print('This link is a good link.')
    for url in links_list:
        print(url)

    # get bad links
    print('This is link is a bad link.')
    for url in bad_links_list:
        print(url)
    browser.quit()


