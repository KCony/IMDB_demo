# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 13:02:04 2025

@author: konst
"""

import re
import sys

# match = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2025-07-21 or something else")  # Example regex usage
# if not match:
#     print("Invalid date format. Please use YYYY-MM-DD.")
# else:
#     print(match.start(), match.end(), match.group(0), match.group(1), match.group(2), match.group(3))
#     print(f'{match.group(3)}/{match.group(2)}/{match.group(1)}')

# for name in ["Tom Hanks", "Ron Hanks", "Jon Hanks", "Jane Doe", "Jon Banks", "JON Hanks", ]:
#     match = re.search(r"^.o.\sH.*", name, flags=re.IGNORECASE)
#     if match:
#         print(match.group(0))  # Example regex usage
# result = re.findall(r"(\w+), (\w+)", "Liefeld, Rob")[0]
# print(f'{result[1] } {result[0]}')  # Output: Rob Liefeld

IBDM_FILE = "imdb_data.txt"

# actors = { "Tom Hanks": {"Forrest Gump", "Ternimal"}, "Sergey Gusev": {"Overlaw"}, "Stephen Salvati": {"Overlaw"} }
# Old movies = { "Forrest Gump": 1987, "Terminal": 1995, "Overlaw": 2014 }
# movies_by_year = {1987: {"Forrest Gump"}, 1995: {"Terminal"}, 2014: {"Overlaw"} }
# New movies = { "Forrest Gump": {"Tom Hanks", "Gary Sinise"}, "Terminal": {"Tom Hanks"}, "Overlaw": {"Sergey Gusev"} }


def read_data(IBDM_FILE):
    actors = {}
    movies_by_year = {}
    movies = {}
    cnt = 0
    for line in open(IBDM_FILE, encoding="utf-8"):
        name, movie, release = [elem.strip() for elem in line.strip().split('|')]
    # try:
        name_match = re.findall(r"(\w+), (\w+)", name)
        if len(name_match) > 0:
            name = name_match[0]  # Extract the first match
            name = name[1] + " " + name[0]  # Convert to "First Last" format

    # except IndexError:
    #     print(f"Invalid name format: {name}. Expected format 'Last, First'. Skipping this entry.")
    #     print(f"name, movie, release: {name}, {movie}, {release}")
    #     sys.exit()
  
        release = int(release)
        if name not in actors:
            actors[name] = set()
        actors[name].add(movie); movies_by_year.setdefault(release, set()).add(movie)
        movies.setdefault(movie, set()).add(name)
    return actors, movies_by_year, movies

def proc_all_actors(actors):
    for actor in \
        actors:
        print(actor)

def proc_find_movie_by_date(movies_by_year):
    movie_date = input("Введите условие поиска по дате выпуска фильма в формате"
                " {<>=}YYYY (например, <2005): ")
    operator = movie_date[0]
    year = int(movie_date[1:])
    found = False
    for release_date, movie_list in movies_by_year.items():
        if release_date == year and operator == '=' or \
            release_date < year and operator == '<' or \
            release_date > year and operator == '>':
            for movie in movie_list:
                found = True
                print(movie, release_date)
    if not found: print("Не найдено фильмов, удовлетворяющих условию")

def proc_find_movie_by_actor(actors):
    pattern = input("Введите имя актёра для поиска. Можно использовать регулярные выражения: ")
    for actor in actors:
        result = re.findall(pattern, actor, flags=re.IGNORECASE)
        if len(result) > 0:
            print(f'{actor}\n------------------')
            for movie in actors[actor]:
                print(f'\t{movie}')

if __name__ == "__main__":
    actors, movies_by_year, movies = read_data(IBDM_FILE)
        # cnt += 1
        # if cnt > 100:
        #     break
        #print(name, movie, release)

    #print(actors)

    print("Добро пожаловать в приложение!")
    menu = """1 - Просмотр всех актёров
2 - Поиск фильма по дате выпуска
3 - Поиск фильмов по актёру
4 - Поиск всех актёров, снявшихся в фильме
0 - Выход
"""
    command = ""
    while command != '0':
        print(menu)
        command = input("Выберите пункт меню: ")
        command = command.strip().lower()
        if command == "1":
            proc_all_actors(actors)
        elif command == "2":
            proc_find_movie_by_date(movies_by_year)
        elif command == "3":
            proc_find_movie_by_actor(actors)
        elif command =="0":
            break
        else:
            print("Неверно выбран пункт меню, попробуйте снова")
        print()
