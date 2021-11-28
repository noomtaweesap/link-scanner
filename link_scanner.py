from typing import List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
import sys


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
    pass


def invalid_urls(urllist: List[str]) -> List[str]:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
    pass


if __name__ == "__main__":
    browser: WebDriver = webdriver.Chrome(r'C:\Users\DELL\Desktop\desktop\CODE\link_scanner\chromedriver.exe')
    url = sys.argv[1]
    link_list = get_links(url)
