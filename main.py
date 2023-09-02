import requests
import smtplib
import ssl
def send_email(cont):
     port=465
     host="smtp.gmail.com"
     username="reyhaneh.gh.davodi@gmail.com"
     password="rsorsftxzuzvvhir"
     context=ssl.create_default_context()
     with smtplib.SMTP_SSL(host,port,context=context) as server:
          server.login(username,password)
          server.sendmail(username,username,cont)





api="24bc313188794f928cf0d6e7ef838c38"
url=("https://newsapi.org/v2/everything?"
     "q=tesla&from=2023-08-02&sortBy=publishedAt&api"
     "Key=24bc313188794f928cf0d6e7ef838c38")
# Make a Requests
request=requests.get(url)
# get a dictionary with data
content=request.json()
# access the articles description and titles
for article in content['articles']:
     news=article['title']+ "\n" + article['description']
     send_email(news)
     # print(article['title'])
     # print(article['description'])
