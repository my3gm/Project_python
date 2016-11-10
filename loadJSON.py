import json
from pandas.io.json import json_normalize
import itertools
from nltk.corpus import stopwords
import re


def loadReviews(fname):
    data = []
    dict = {}
    stoplex = set(stopwords.words('english'))

    fi = open(fname)
    fo = open("reviews.txt", "wb")

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
        return dict

    fi.close()
    fo.close()

def loadCheckins(fname):
   
    fopen = open(fname)
    
    #fwrite = open("checkins.txt", "wb")
    #for lines in itertools.islice(fopen,1, 100):
    checkinData = json.loads(fopen)
    results = json_normalize(checkinData,'[0-9]','checkin_info',['type','business_id'])
    print results
    #fwrite.write(str(result)) 
    #fopen.close()
    #fwrite.close()

    

def loadJSONfile():
    loadReviews('yelp_academic_dataset_review.json')
    loadCheckins('yelp_academic_dataset_checkin.json')

if __name__ == '__main__':
    loadJSONfile()
