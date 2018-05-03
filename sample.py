import urllib2
import time
import sys

def query(url):
    res = urllib2.urlopen(url)
    return res.read()

token = "EYbc4HINRUNEzLltaW3WKXJVCZBx9I3k"

for i in range(0, 2):
    string = sys.argv[1]
    url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, string)
    result = query(url)
    print result

    time.sleep(1)
