# name: Juyoung Daniel Yun
# email: juyoung.yun@stonybrook.edu
# id: 112368205

from datetime import datetime
import csv
#----------------------------------------------------------------------

movieItems = []

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    The line is basically a dictionary object.
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        if line["id"] != '':
            mDate = datetime.strptime(line["release_date"], "%m/%d/%Y").date()
            movieItem = {}
            movieItem['date'] = mDate
            movieItem['record'] = line
            movieItem['genres'] = line["genres"]
            movieItem['id'] = line["id"]
            movieItem['imdb_id'] = line["imdb_id"]
            movieItem['original_language'] = line["original_language"]
            movieItem['original_title'] = line["original_title"]
            movieItem['popularity'] = line["popularity"]
            movieItem['production_companies'] = line["production_companies"]
            movieItem['production_countries'] = line["production_countries"]
            movieItem['revenue'] = line["revenue"]
            movieItem['runtime'] = line["runtime"]
            movieItem['spoken_languages'] = line["spoken_languages"]
            movieItem['status'] = line["status"]
            movieItem['title'] = line["title"]
            movieItem['adult'] = line["adult"]
            movieItems.append(movieItem)
    print("Total movie items = ", len(movieItems))
    movieItems.sort(key=lambda item:item['date'])
    return movieItems

if __name__ == "__main__":
    with open("movies_metadata_edited.csv", encoding="utf8") as f_obj:
        csv_dict_reader(f_obj)