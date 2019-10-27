# name: Juyoung Daniel Yun
# email: juyoung.yun@stonybrook.edu
# id: 112368205

from moviedatareader import csv_dict_reader
from datetime import datetime
from constants import getQuestionDictList
from constants import getId
from constants import getGenres
from constants import getProduction_countries
from constants import getProduction_companies

# adult,genres,id,imdb_id,original_language,original_title,popularity,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,title



def userDateInput(first_date, last_date):
    print("Available date interval is from: ", first_date, "till", last_date)
    ufDate = input("Enter valid interval start date in the format YYYY-MM-DD: ")
    # ufDate="2010-01-01"
    fDate = datetime.strptime(ufDate, "%Y-%m-%d").date()
    ulDate = input("Enter valid interval end date in the format YYYY-MM-DD: ")
    # ulDate="2015-01-01"
    lDate = datetime.strptime(ulDate, "%Y-%m-%d").date()
    print("You entered: ", fDate, " - ", lDate)
    return fDate, lDate

def userQuestionInput(qDictList):
    print("Available questions are: ")
    for item in qDictList:

        print(item['num'], ": ", item['question'])
    qnum = input("Select the number of any of the above question. ")

    return qnum

if __name__ == "__main__":
    f_obj = open("movies_metadata_edited.csv", encoding="utf8")
    movieItems = csv_dict_reader(f_obj)
    qDictList = getQuestionDictList()
    print("First date: ", movieItems[0]['date'])
    print("Last date: ", movieItems[-1]['date'])
    contFlag = True

    while contFlag:
        movieItems.sort(key=lambda item: item['date'])
        fDate, lDate = userDateInput(movieItems[0]['date'], movieItems[-1]['date'])
        qNum = userQuestionInput(qDictList)
        if qNum == "1":
            print("________________________________________")
            print("%s\t %s\t %s\t" % ("No.","Popularity","Movie Title"))
            print("________________________________________")
            # adult,genres,id,imdb_id,original_language,original_title,popularity,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,title
            movieItems.sort(key=lambda item: float(item['popularity']))
            movieItems.reverse()

            k=1
            movieCount=0
            for i in range(0,movieItems.__len__()):
                if movieItems[i]['date'] >= fDate and movieItems[i]['date'] <= lDate:
                    movieCount += 1
                    if k<=20:
                        # print(k,")","\t\t",movieItems[i]['popularity'],"\t\t",movieItems[i]['title'])
                        print("%s)\t %s\t %s\t" %(k,movieItems[i]['popularity'],movieItems[i]['title']))
                        k+=1

            print("________________________________________")
            print("Total number of movies produced during the period    ",fDate," - ",lDate,"is ",movieCount)
            print("________________________________________")


        elif qNum == "2":

            movieItems.sort(key=lambda item: float(item['popularity']))
            movieItems.reverse()

            list1=list()
            print("Available languages are: ")
            for i in range(0, movieItems.__len__()):
                list1.append(movieItems[i]['original_language'])

            list1 = list(set(list1))
            list1.sort()

            for i in range(0,list1.__len__()):
                print(list1[i])

            a=input("Type any language code from above list: ")
            dataList=list()
            k=1
            movieCount = 0

            print("________________________________________")
            print("%s\t %s\t %s\t %s\t" % ("No.","Popularity","Movie Title","Movie language"))
            print("________________________________________")

            for i in range(0,movieItems.__len__()):
                if movieItems[i]['date'] >= fDate and movieItems[i]['date'] <= lDate:
                    if movieItems[i]['original_language'] == a:
                        movieCount+=1
                        if k<=20:
                            # print(k,")\t",movieItems[i]['popularity'],"\t",movieItems[i]['title'],"\t",movieItems[i]['original_language'])
                            print("%s)\t %s\t %s\t %s\t" % (k, movieItems[i]['popularity'], movieItems[i]['title'],movieItems[i]['original_language']))
                            k+=1

            print("________________________________________")
            print("Total number of movies with language    ",a ,"  during the period  ", fDate, " - ", lDate, " is ", movieCount)
            print("________________________________________")



        elif qNum == "3":

            movieItems.sort(key=lambda item: float(item['popularity']))
            movieItems.reverse()

            print("Available genres are: ")
            list1 = list()
            for i in range(0,movieItems.__len__()):
                for j in range(0,(getGenres(movieItems[i]['genres'])).__len__()):
                    list1.append((getGenres(movieItems[i]['genres']))[j])

            list1 = list(set(list1))
            list1.sort()

            for i in range(0, list1.__len__()):
                print(list1[i])

            a=input("Type any genre from above list: ")
            k=1
            movieCount = 0

            print("________________________________________")
            print("%s\t %s\t %s\t %s\t" % ("No.","Popularity","Movie Title","Genres"))
            print("________________________________________")

            for i in range(0, movieItems.__len__()):
                if movieItems[i]['date'] >= fDate and movieItems[i]['date'] <= lDate:
                    for j in range(0,(getGenres(movieItems[i]['genres'])).__len__()):
                        if (getGenres(movieItems[i]['genres']))[j] == a:
                            movieCount+=1
                            if k<=20:
                                # print(k,")\t",movieItems[i]['popularity'],"\t",movieItems[i]['title'],"\t",getGenres(movieItems[i]['genres']))
                                print("%s)\t %s\t %s\t %s\t" % (k, movieItems[i]['popularity'], movieItems[i]['title'],getGenres(movieItems[i]['genres'])))
                                k+=1


            print("________________________________________")
            print("Total number of movies with Genres    ", a, "  during the period  ", fDate, " - ", lDate, " is ",
                  movieCount)
            print("________________________________________")

        elif qNum == "4":

            movieItems.sort(key=lambda item: float(item['popularity']))
            movieItems.reverse()

            print("Available countries are: ")

            list1 = list()
            for i in range(0, movieItems.__len__()):
                for j in range(0, (getProduction_countries(movieItems[i]['production_countries'])).__len__()):
                    list1.append((getProduction_countries(movieItems[i]['production_countries']))[j])

            list1 = list(set(list1))
            list1.sort()

            for i in range(0, list1.__len__()):
                print(list1[i])

            a=input("Type any country code from above list: ")
            k = 1
            movieCount = 0

            print("________________________________________")
            print("%s\t %s\t %s\t %s\t" % ("No.", "Popularity", "Movie Title", "Production Countries"))
            print("________________________________________")

            for i in range(0, movieItems.__len__()):
                if movieItems[i]['date'] >= fDate and movieItems[i]['date'] <= lDate:
                    for j in range(0,(getProduction_countries(movieItems[i]['production_countries'])).__len__()):
                        if (getProduction_countries(movieItems[i]['production_countries']))[j] == a:
                            movieCount+=1
                            if k<=20:
                                # print(k,")\t",movieItems[i]['popularity'],"\t",movieItems[i]['title'],"\t",getProduction_countries(movieItems[i]['production_countries']))
                                print("%s)\t %s\t %s\t %s\t" % (k, movieItems[i]['popularity'], movieItems[i]['title'],getProduction_countries(movieItems[i]['production_countries'])))
                                k+=1

            print("________________________________________")
            print("Total number of movies in country    ", a, "  during the period  ", fDate, " - ", lDate, " is ",
                  movieCount)
            print("________________________________________")

        elif qNum == "5":

            movieItems.sort(key=lambda item: float(item['revenue']))
            movieItems.reverse()

            k = 1
            movieCount = 0

            print("________________________________________")
            print("%s\t %s\t %s\t" % ("No.", "Revenue", "Movie Title"))
            print("________________________________________")

            for i in range(0, movieItems.__len__()):
                if movieItems[i]['date'] >= fDate and movieItems[i]['date'] <= lDate:
                    movieCount += 1
                    if k <= 20:
                        # print(k, ")\t", movieItems[i]['revenue'], "\t", movieItems[i]['title'])
                        print("%s)\t %s\t %s\t" % (k,  movieItems[i]['revenue'], movieItems[i]['title']))
                        k+=1

            print("________________________________________")
            print("Total number of movies produced during the period  ", fDate, " - ", lDate, " is ",
                  movieCount)
            print("________________________________________")


        # Case 6
        elif qNum == "6":

            for i in range(0,movieItems.__len__()):
                try:
                    movieItems[i]['runtime']=int(movieItems[i]['runtime'])
                except ValueError:
                    movieItems[i]['runtime']="0"

            movieItems.sort(key=lambda item: int(item['runtime']))
            movieItems.reverse()

            k = 1
            movieCount = 0

            print("________________________________________")
            print("%s\t %s\t %s\t" % ("No.", "Runtime", "Movie Title"))
            print("________________________________________")

            for i in range(0, movieItems.__len__()):
                if movieItems[i]['date'] >= fDate and movieItems[i]['date'] <= lDate:
                    movieCount += 1
                    if k <= 20:
                        # print(k, ")\t", movieItems[i]['runtime'], "\t", movieItems[i]['title'])
                        print("%s)\t %s\t %s\t" % (k, movieItems[i]['runtime'], movieItems[i]['title']))
                        k+=1

            print("________________________________________")
            print("Total number of movies produced during the period  ", fDate, " - ", lDate, " is ",
                  movieCount)
            print("________________________________________")

        elif qNum == "7":

            movieItems.sort(key=lambda item: float(item['popularity']))
            movieItems.reverse()

            k = 1
            movieCount = 0

            print("________________________________________")
            print("%s\t %s\t %s\t %s\t" % ("No.", "Popularity", "Movie Title","Production Companies"))
            # print("No.\tPopularity\tMovie\tTitle\tProduction Companies")
            print("________________________________________")

            for i in range(0, movieItems.__len__()):
                if movieItems[i]['date'] >= fDate and movieItems[i]['date'] <= lDate:
                    movieCount += 1
                    if k <= 20:
                        # print(k, ")\t", movieItems[i]['popularity'], "\t", movieItems[i]['title'], "\t",getProduction_companies(movieItems[i]['production_companies']))
                        print("%s)\t %s\t %s\t %s\t" % (k, movieItems[i]['popularity'], movieItems[i]['title'],getProduction_companies(movieItems[i]['production_companies'])))
                        k += 1

            print("________________________________________")
            print("Total number of movies produced during the period  ", fDate, " - ", lDate, " is ",
                  movieCount)
            print("________________________________________")

        else:
            print("Invalid Value")


        uChoice = input("Enter [Y/N] to continue: ")
        if 'N' in uChoice or 'n' in uChoice:
            print("Thank you. Exiting!!")
            contFlag = False
