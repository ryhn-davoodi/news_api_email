import requests
import smtplib
import ssl
import os
def send_email(cont):
     port=465
     host="smtp.gmail.com"
     username="reyhaneh.gh.davodi@gmail.com"
     password=os.getenv("NEWSPASSWORD")
     context=ssl.create_default_context()
     with smtplib.SMTP_SSL(host,port,context=context) as server:
          server.login(username,password)
          server.sendmail(username,username,cont)


api="24bc313188794f928cf0d6e7ef838c38"
url=("https://newsapi.org/v2/everything?q=tesla&from=2023-08-03&sort"
     "By=publishedAt&apiKey=24bc313188794f928cf0d6e7ef838c38&language=en")
# Make a Requests
request=requests.get(url)
# get a dictionary with data
content=request.json()
print(content)
# access the articles description and titles
news=""
for article in content['articles'][:20]:
     if article['title'] is not None:
         news=("Subject: Today's news "+"\n"+
                 news+article['title']+ "\n"
               + article['description']
               +'\n'+article['url']+ 2*"\n")
news=news.encode("utf-8")
     # send the data as an email
send_email(news)
