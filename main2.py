import urllib2
import time
import random

def query(url):
    res = urllib2.urlopen(url)
    return res.read()

token = "EYbc4HINRUNEzLltaW3WKXJVCZBx9I3k"

"""
for i in range(0, 2):
    str = "ABCD"
    url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, str)
    result = query(url)
    print(str, result)

    time.sleep(1)
"""

#random.seed(1)
for j in range(0, 10000):
    aidu = ""
    for i in range(0, 50):
        ransu = int(random.random() * 4)
        if ransu == 0:
            aidu = aidu + "A"
        elif ransu == 1:
            aidu = aidu + "B"
        elif ransu == 1:
            aidu = aidu + "C"
        else:
            aidu = aidu + "D"

    url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, aidu)
    result = query(url)
    print(aidu, result)

    time.sleep(1)



"""
origin = ""
aidu = ""

for k in ("A", "B", "C", "D"):
    origin = ""
    origin = k
    aidu = k

    for j in ("A", "B", "C", "D"):
        aidu = origin
        aidu = aidu + j


        for i in ("A", "B", "C", "D"):
            aidu = origin
            aidu = aidu + i

            url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, aidu)
            result = query(url)
            print(aidu, result)

            time.sleep(1)
"""