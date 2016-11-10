import json
import itertools
from nltk.corpus import stopwords
import re
import collections


def loadJSONfile(fname):
    data = []
    dict = {}
    stoplex = set(stopwords.words('english'))

    fi = open(fname)
    fo = open("out.txt", "wb")

    for lines in itertools.islice(fi, 20001, 20100):
        content = json.loads(lines)
        unique = set()
        data = content.get('text')
        data = data.lower().strip()
        data = re.sub('[^a-z]', ' ', data)

        data = data.split(' ')
        for word in data:
            if word == '' or word in stoplex:
                continue
            else:
                unique.add(word)

        dict['type'] = content['type']
        dict['votes'] = content['votes']
        dict['stars'] = content['stars']
        dict['date'] = content['date']
        dict['business_id'] = content['business_id']
        dict['user_id'] = content['user_id']
        dict['text'] = unique

        # fo.write( '%s:%s\t' %(key,value))
        fo.write(str(dict))
        fo.write('\n')
        print dict

    fi.close()
    fo.close()


if __name__ == '__main__':
    loadJSONfile('yelp_academic_dataset_review.json')
