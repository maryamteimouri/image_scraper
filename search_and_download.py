import persist_image
import os
from bing_images import bing

import get_image_links_new
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
import virtualenv


def search_and_download(search_term: str, driver_path: str, target_path='./images', number_images=20):
    target_folder = os.path.join(target_path, '_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = get_image_links_new.fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)

    for elem in res:
        persist_image.persist_image(target_folder, elem)


# driver = webdriver.Chrome(ChromeDriverManager().install())
search_and_download("car", "/usr/bin/chromedriver")
