# -*- coding: utf-8 -*-

import json
import requests
from bs4 import BeautifulSoup

search_url = "https://movie.douban.com/j/subject_suggest?q="
search_download_url = "http://www.meiju8.cc/search.php?kw="
detail_download_url = "http://www.meiju8.cc"


class Magnetic_Obj(object):
    def __init__(self, title, url):
        self.title = title
        self.url = url


class Download_Obj(object):
    def __init__(self, title, magnetic_obj_list):
        self.title = title
        self.magnetic_obj_list = magnetic_obj_list


class Movie(object):
    def __init__(self, title, url, img, actors, star, download_obj_list):
        self.title = title
        self.url = url
        self.img = img
        self.star = star
        self.actors = actors
        self.download_obj_list = download_obj_list


def get_movie_list(key):
    movies = list()
    response = requests.get(search_url + key)
    result_json = json.loads(response.text)
    for result in result_json:
        try:
            title = result['title']
            img = result['img']
            url = result['url']
            detail_response = requests.get(url)
            soup = BeautifulSoup(detail_response.text, "html.parser")
            star, actors = get_actors(soup, 5)
            download_obj_list = get_download_obj_list(title)
            movie = Movie(title, url, img, actors, star, download_obj_list)
            movies.append(movie)
        except:
            pass
    return movies


def get_download_obj_list(key):
    download_obj_list = list()
    response = requests.get(search_download_url + key)
    soup = BeautifulSoup(response.text, "html.parser")
    movie_list = soup.select(".cn_box2")
    for movie in movie_list:
        movie = movie.select(".bor_img3_right")
        movie_url = detail_download_url + movie[0].a['href']
        download_obj = get_download_obj(movie_url)
        download_obj_list.append(Download_Obj(key, download_obj))
    return download_obj_list


def get_download_obj(url):
    magnetic_list = list()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for magnetic in soup.select(".down-title"):
        download_url = magnetic.a['href']
        title = magnetic.a.string
        magnetic_list.append(Magnetic_Obj(title, download_url))
    return magnetic_list


def get_actors(soup, num):
    actor_list = soup.select(".attrs")[2].find_all('a')
    star = soup.select('.rating_num')[0].string
    sum_index = min(num, actor_list.__len__())
    actor_list_str = list()
    for i in range(sum_index):
        actor_list_str.append(actor_list[i].string)
    return star, actor_list_str.__str__()


if __name__ == "__main__":
    get_movie_list("杀死比尔")
