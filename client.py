import json
import requests
import time

PORT="80"
ADD_URL="http://localhost/"
SUGGEST_URL="http://localhost/ABC-Book-Store/req.php"
TOTAL_URL="http://localhost/ABC-Book-Store/req.php"

class Obj:
    def __init__(self):
        pass

def postMe(dict, URL):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(URL, data=json.dumps(dict, default=lambda o: o.__dict__),headers=headers)
    print(json.dumps(dict, default=lambda o: o.__dict__))
    return r

def getMe (URL):
    r = requests.post(URL)
    return r

file=open("mydata.csv", 'r')
#file.readline()
file.readline()
lines = file.readlines()
i = -2
for line in lines :
    #print (line.strip().split(','))
    asset=line.strip().split(',')
    i+=1
    if (i>=0 and asset[3] == invo.invoiceId):
        invo.books.append({'BookID': asset[4], 'CategoryId': asset[6], 'Category': asset[7], 'Price': asset[9], 'Quantity': asset[8]})
        continue
    elif i==-1:
        invo=Obj()
        invo.invoiceId=asset[3]
        invo.invoiceDate=asset[2]
        invo.memberId=asset[0]
        invo.memberName=asset[1]
                
        invo.amount=asset[10]
        invo.grossTotal=asset[11]
        invo.discount=asset[12]
        invo.NetTotal=asset[13]
        invo.books = [{'BookID': asset[4], 'CategoryId': asset[6], 'Category': asset[7], 'Price': asset[9], 'Quantity': asset[8]}]

            
    else:
        postMe(invo, 'http://localhost/req.php')
        invo=Obj()
        invo.invoiceId=asset[3]
        invo.invoiceDate=asset[2]
        invo.memberId=asset[0]
        invo.memberName=asset[1]
                
        invo.amount=asset[10]
        invo.grossTotal=asset[11]
        invo.discount=asset[12]
        invo.NetTotal=asset[13]
        invo.books = [{'BookID': asset[4], 'CategoryId': asset[6], 'Category': asset[7], 'Price': asset[9], 'Quantity': asset[8]}]
        #time.sleep(3)

while True:
    print ("Enter 1 to get suggestion")
    print ("Enter 2 to get income")
    num=int(input("Enter : "))
    if num==1:
        memberId=input("Member ID : ")
        bookLst=input("Books (seperated by commas) :")
        books=bookLst.strip().split(',')
        sugg=Obj()
        sugg.memberId=memberId
        sugg.books=books
        res=postMe(sugg, SUGGEST_URL+":"+PORT)
        print (res)
    elif num==2:
        print (getMe(TOTAL_URL+":"+PORT))
    else:
        print ("error!")
