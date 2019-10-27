# name: Juyoung Daniel Yun
# email: juyoung.yun@stonybrook.edu
# id: 112368205

import ast

questionList = ["List most popular top 20 movies in a particular period.",
    "List most popular top 20 movies released in a particular language.",
    "List most popular top 20 movies released in a particular genre type.",
    "List most popular top 20 movies produced in a particular country.",
    "List top 20 movies which earned highest revenue in a particular period.",
    "List top 20 movies according to their runtime in a particular period.",
    "List the production companies of top 20 most popular movies in a particular period.",
    ]

def getQuestionDictList():
    qDictList = []
    for i in range(len(questionList)):
        qDict = {}
        qDict['num'] = i + 1
        qDict['question'] = questionList[i]
        qDictList.append(qDict)
    return qDictList

def getGenres(genres):
    if (genres == "[]"):
        return []
    else:
        genresItems = ast.literal_eval(genres)
        genreList = []
        for item in genresItems:
            genreList.append(item['name'])
        return genreList

def getId(id):
    if (id == "[]"):
        return []
    else:
        idItems = ast.literal_eval(id)
        idList = []
        for item in idItems:
            idList.append(item['id'])
        return idList

def getProduction_companies(data):
    if (data == "[]"):
        return []
    else:
        dataItems = ast.literal_eval(data)
        dataList = []
        for item in dataItems:
            dataList.append(item['name'])
        return dataList

def getProduction_countries(data):
    if (data == "[]"):
        return []
    else:
        dataItems = ast.literal_eval(data)
        dataList = []
        for item in dataItems:
            dataList.append(item['iso_3166_1'])
        return dataList


if __name__ == "__main__":
    print(getGenres("[{'id': 14, 'name': 'Fantasy'}, {'id': 28, 'name': 'Action'}, {'id': 53, 'name': 'Thriller'}]"))
    print(getGenres("[{'id': 35, 'name': 'Comedy'}, {'id': 14, 'name': 'Fantasy'}]"))
    print(getGenres("[{'id': 99, 'name': 'Documentary'}]"))
    print(getGenres("[]"))