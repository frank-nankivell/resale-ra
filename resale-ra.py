import bs4
import requests
import smtplib
import datetime
from secrets import *

now = datetime.datetime.now()
url_list = url_input
print(url_list)


res=[]
for link in url_list:
    getPage = requests.get(link)

    getPage.encoding = 'utf-8'
    getPage.raise_for_status()
    rapage = bs4.BeautifulSoup(getPage.text,'html.parser')
    tickets = rapage.find_all("li", class_="closed")
    title = rapage.find_all("title")
    subject = ("Subject: Ticket Alert \n\n Tickets now available for this event"+(str(title))+"link found here"+(str(link)))

    available = False
    the_one = parser_check
    if any(the_one in s for s in rapage.strings):
        available = True

    if available == True:
        print(str(now)+'  YES  Tickets now available'+(str(title))+(str(link)))
        conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
        conn.ehlo() # call this to start the connection
        conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
        conn.login(login_email, login_app_pass)
        conn.sendmail(login_email, send_mail_to, subject,)
        conn.quit()
        print('Sent notificaton e-mails for the following recipients:\n')
        for i in range(len(send_mail_to)):
            print(send_mail_to[i])
    else:
        print(str(now)+'    No tickets available now for this url '+(str(title))+(str(link)))
        with open('Ra-resale-debug.txt','a') as file:
            file.writelines(str(now)+'   No tickets available now for this url '+(str(title))+(str(link)))
            file.write("\n")
            file.close()
res = [i for i in res if i[0]!='']
