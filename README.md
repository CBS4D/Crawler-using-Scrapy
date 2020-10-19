# Crawler-using-Scrapy
#  Scrape MCQ's From Internet

Scrape different kind of questions from internet with their solutions.

### Prerequisites
```
OS - Ubuntu
Python 3.8.2
Scrapy 2.2.1
```

### Installing
 For some dependencies please run below command in terminal.
```
sudo apt-get install python3 python-dev python3-dev \
     build-essential libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev \
     python-pip
      
```
Create Virtual Environment using one of below command.
```
virtaulenv -p python3 vnv
OR
python3 -m venv vnv
```
Install all requirements from 'requirements.txt'.
```
pip install -r path/to/requirements.txt
```
go inside project folder and run below command to start collecting mcq's from internet(website).
```
scrapy crawl test_bot -o file-name.csv
```
