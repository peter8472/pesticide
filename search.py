import json
import os.path
import p.dblog
import urllib

namesearch = '''https://ordspub.epa.gov/ords/pesticides/cswu/ProductSearch/partialprodsearch/v2/riname/'''

regsearch = 'https://ordspub.epa.gov/ords/pesticides/ppls/'


def splitreg(eparegno):
    '''removes trailing digits from eparegno, because the search 
    by distributer is not working'''
    stuff = eparegno.split("-")
    return "{}-{}".format(stuff[0],stuff[1])

def readfile(fname):
    f = open(fname)
    g = json.load(f)
    return g


if __name__ == "__main__":
    x = readfile("outfile.txt")
    # print(json.dumps(x, indent=4))
    logger = p.dblog.Dblog("regno.db")
    for a in x['items']:
        if a['product_status'] == "Active":
            ans = input("download {} (Y/n/q)? ".format(a['productname']))
            if ans == 'q':
                exit(0)
            elif ans == 'y' or ans == '':
                
                outname = splitreg(a['eparegno'])
                url = regsearch + outname
                print(url)
                if os.path.exists(outname):
                    print("{} exists".format(outname))
                    continue
                else:
                    # req= urllib.request.Request(url)
                    # req.o
                    response =  urllib.request.urlopen(url)
                    answer = response.read()
                    logger.addrow(url, answer)

                    outfile = open(outname,'wb')

                    outfile.write(answer)
                    outfile.close()

