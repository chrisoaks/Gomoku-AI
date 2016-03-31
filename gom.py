# Imports from requests, pprint, and BeautifulSoup

import requests
import pprint
from bs4 import BeautifulSoup
import ast

# pd stands for player dictioray, a hashtable of players as in:
# {Rank: 'Player', ...}
pd = {}

# A global variable needed to count each name only once.
searchednames = []

# List of turns
turnlist = []

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
def getGameLength(S):
    dotfound = False
    
    for x in S[::-1]:
        if x == '.':
            dotfound = True
        if x == ' ' and dotfound == True:
            return 0 # fix later

def getTupleFrom(S):
    return (S[0],S[1])

def getFromTxt(url):
    r = requests.get(url)
    SplitList = r.content.split('1. ',1)
    S = SplitList[1]
    
    print S.split()
    S = S.translate(None, '.')
    print S.split()
    print [int(s) for s in S.split() if s.isdigit()]
    #tuple1 = getTupleFrom(S.split()[0])
    #tuple2 = getTupleFrom(S.split()[1])
    #print 'tuple1 =' + str(tuple1)
    #print 'tuple2 =' + str(tuple2)
    #turnlist = [(tuple1),(tuple2)]
    print 'turnlist =' + str(turnlist)
    bfirstplayersturn = True
    firsttuple = ()
    secondtuple = ()
    for s in S.split():
        if s.isdigit():
            print int(s)
            continue
        if bfirstplayersturn == True:
            bfirstplayersturn = False
            firsttuple = getTupleFrom(s)
        else:
            bfirstplayersturn = True
            secondtuple = getTupleFrom(s)
            turnlist.append(((firsttuple),(secondtuple)))
    print turnlist
            
            
f = open('workfile', 'r')
pd = ast.literal_eval(f.read()) # This is temporary, should be using pickle
print pd[2041]
getFromTxt('http://www.playok.com/en/game.phtml/117844329.txt?gm')

#getfrom('http://www.playok.com/en/stat.phtml?gid=gm&uid=gregi73&sk=3&so=2',100)

                       
#game structure
#list of turns
#    tuple
#        tuple (b, 2)
#        tuple (d, 2)
#[((b,2),(d,2)),((f,3),(h,1))]

