import urllib2
import time
import sys
import json

token = "EYbc4HINRUNEzLltaW3WKXJVCZBx9I3k"
char_list = ["A", "B", "C", "D"]
word_dict = {}

def query(url):
    res = urllib2.urlopen(url)
    return res.read()

def search(str):
    if len(str) > 8:
        print "Words too long!"
        sys.exit()

    max_score = 0
    max_score_str = ""

    for char in char_list:
        new_str = str + char
        url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, new_str)
        result = query(url)

        if result > max_score:
            max_score = result
            max_score_str = new_str

        time.sleep(1)

    print "%8s:%4s" % (max_score_str, max_score)
    word_dict[max_score_str] = max_score
    search(max_score_str)

if __name__ == '__main__':
    search("")
    f = open('output.json', 'w')
    json.dump(word_dict, f)
