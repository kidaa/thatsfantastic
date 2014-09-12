from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
from requests_futures.sessions import FuturesSession
import json

session = FuturesSession(max_workers=10)

BASE_URL = 'http://fantasticfest.com/films/'

ABSOLUTE_DIR = os.path.abspath(os.path.dirname(__file__))
SAVE_PATH = os.path.join(ABSOLUTE_DIR, 'films/2014/')

DEFAULT_EXCLUDE_CLASSES = set(['shareBox', 'alert', 'carousel', 'carousel-inner'])

REQUESTS_PER_MINUTE = 15


def exclude_classes(tag, exclude_set=DEFAULT_EXCLUDE_CLASSES):
    if tag.has_attr('class'):
        class_list = set(tag.get('class'))
        classes_to_exclude = set(exclude_set)
        class_intersection = class_list.intersection(classes_to_exclude)
        return len(class_intersection) == 0
    else:
        return True


def get_link_set(soup):
    anchor_list = soup.select('ul.thumbnails > li a:first')
    return set([a['href'] for a in anchor_list])


def extract_body_text(page_soup):
    start_extract = page_soup.select('article .shareBox')[0]
    body_elements = start_extract.find_next_siblings(exclude_classes)
    body_text = '\n'.join([el.text for el in body_elements])
    return body_text


def extract_title(page_soup):
    raw_title = page_soup.find('title').text
    return raw_title.strip(' | Fantastic Fest')


def process_film_page(sess, response):
    if response.ok:
        soup = BeautifulSoup(response.text)
        film_title = extract_title(soup)
        raw_body = extract_body_text(soup)
        film_info = {
            'title': film_title,
            'raw_body': raw_body
        }
        url_end = os.path.split(response.url)[-1]
        filename = "{}.json".format(url_end)
        file_save_path = os.path.join(SAVE_PATH, filename)
        json.dump(film_info, open(file_save_path, 'w'), indent=4)
    else:
        print('Error fetching: {0}'.format(response.url))


def process_film_list_page(sess, response):
    if response.ok:
        soup = BeautifulSoup(response.text)
        page_urls = get_link_set(soup)
        for url in page_urls:
            session.get(url, background_callback=process_film_page)
            print(url)
    else:
        print('Error fetching: {0}'.format(response.url))


# def main():
#     # page_offsets = range(0, 109, 18)
#     page_offsets = range(0, 18, 18)
#     page_urls = [urljoin(BASE_URL, "P{0:d}".format(offset)) for offset in page_offsets]
#     for url in page_urls:
#         session.get(url, background_callback=process_film_list_page)
#         print(url)


# if __name__ == '__main__':
#     main()
