import requests
import pprint
from bs4 import BeautifulSoup
pd = {} #player dictionary
searchednames = []
def getfrom(url,n):
    
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        rank = int(soup.table.tr.next_sibling.next_sibling.next_sibling.next_sibling.td.next_sibling.next_sibling.contents[0])
        name = str(soup.table.tr.next_sibling.next_sibling.next_sibling.next_sibling.td.a.contents[0])
        table = soup.table
        row = table.tr.next_sibling.next_sibling.next_sibling.next_sibling
        for x in range(0,30):
            pd[rank] = name
            rank = int(row.td.next_sibling.next_sibling.contents[0])
            name = str(row.td.a.contents[0])
            row = row.next_sibling.next_sibling

        pd[rank] = name
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(pd)
    
    except AttributeError:
        print 'ae'
    topname = pd[sorted(pd.keys())[-1]]
    for x in range(len(pd),0,-1):
        print x
        topname = pd[sorted(pd.keys())[x-1]]
        print topname
        if topname not in searchednames:
            searchednames.append(topname)
            break
    
    print topname
    newurl = 'http://www.playok.com/en/stat.phtml?gid=gm&uid=' + topname + '&sk=3&so=2'
    if n - 1 !=0:
        getfrom(newurl, n-1)

getfrom('http://www.playok.com/en/stat.phtml?gid=gm&uid=gregi73&sk=3&so=2',100)



