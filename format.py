import json
import itertools


def loadJSONfile(fname):
    data = []
    dict = {}

    fi = open(fname)
    fo = open("out.txt", "wb")

    for lines in itertools.islice(fi, 0, 20):
        content = json.loads(lines)
        dict['type']=content['type']
        dict['votes']= content['votes']
        dict['stars']=content['stars']
        dict['date']=content['date']
        for key,value in dict.items():
            fo.write('%s:%s\t' % (key,value) )
        fo.write('\n')

        print dict

    fi.close()
    fo.close()



if __name__ == '__main__':
    loadJSONfile('yelp_academic_dataset_review.json')
