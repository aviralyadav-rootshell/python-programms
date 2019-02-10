"""script for CREATING db"""
#importint mysql connector
"""try:
    import mysql.connector as mariadb
except:
    import pip
    pip.main(['install','mysql-connector-python-rf'])
    import mysql.connector as mariadb

try:
    mydb= mariadb.connect(host="https://databases-auth.000webhost.com",user="id7085587_avi",passwd="physingsub7")
    print("connected to server")
except:
    print("error in connection")
    input()
    exit()

try:
    mydb= mariadb.connect(host="https://databases-auth.000webhost.com/",user="id7085587_avi",passwd="physingsub7" ,database="id7085587_dbname")
    print("connected to database")
except:
    print("database doesn't exist \n CREATING New......")
    mycursor= mariadb.mycursor()
    mycursor.execute("CREATE DATABASE ")
    mydb.commit()
"""











from pip._internal import main

try:
    from bs4 import BeautifulSoup as soup
    from urllib.request import urlopen
    import urllib.request
except:
    import pip
    main(['install','bs4'])
    main(['install','urllib'])

#Amazon search
amazonsearch ="https://www.amazon.in/s/field-keywords="
searchkey=input("Amazon search : ")
search=amazonsearch+searchkey

#user agent creating
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
url = urllib.request.Request(search,headers={'User-Agent': user_agent})


# searching
try:
    connection= urlopen(url)
except:
    print("URL can't opend, check internet connection")
    exit()

htmlfile= connection.read()
connection.close()

soupfile= soup(htmlfile,"html.parser")
print(soupfile.title)

print(soupfile.find_all('li',attrs={'class':'s-result-item.s-result-card-for-container.a-declarative.celwidget'}))
