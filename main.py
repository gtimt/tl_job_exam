import urllib2
import time
import sys
import random
import csv

th = 200

token = "EYbc4HINRUNEzLltaW3WKXJVCZBx9I3k"
char_list = ["A", "B", "C", "D"]
word_dict = {}

def query(url):
    res = urllib2.urlopen(url)
    return res.read()

while True:
    string = ""

    for i in range(0,8):
        rand = int(random.random() * 4)
        string = string + char_list[rand]

    url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, string)
    result = query(url)

    if int(result) > th :
        print "%8s:%4s" % (string, result)
        f = open("output.csv", "a")
        writer = csv.writer(f, delimiter=",", quotechar='"')
        writer.writerow([string, str(result)])
        f.close()

    time.sleep(1)
