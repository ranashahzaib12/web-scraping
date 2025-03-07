import requests 


def fetchandsavetofile(url , path):
    r= requests.get(url)

    with open(path , "w") as file:
        file.write(r.text)



url = "https://www.geo.tv/latest/594017-a-global-journey-one-faith-many-ramadan-traditions-part-i"


fetchandsavetofile(url , "times.html")

# r = request.get(url)

# print(r.text)