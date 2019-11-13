
FROM python:3

ADD bot.py /

#RUN apt install python-pip -y
RUN pip install python-telegram-bot
RUN pip install BeautifulSoup
RUN pip install bs4

CMD [ "python", "./bot.py" ]


