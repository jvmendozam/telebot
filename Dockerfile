
FROM python:3

ADD bot.py /

#RUN apt install python-pip -y
#This is a test for a new line and the Jenkins bulid a new release
RUN pip install python-telegram-bot
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install bs4

CMD [ "python3", "./bot.py" ]


