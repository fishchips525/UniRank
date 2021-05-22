import requests
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame
import pandas as pd


# head request
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

rank = []

# 2003
# Indicator is different from 2005-2020 
# Nobel = Alumni, Faculty = Award, HiCi
for year in range(2003, 2004):

    url = 'http://www.shanghairanking.com/ARWU' + str(year) + '.html' 
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    tables = soup.findAll('table')
    tab = tables[0]

    uni = []
    uni_rank = []
    uni_name = []
    uni_totalscore = []
    uni_scoreAlumni = []
    uni_scoreAward = []
    uni_scoreHici = []
    uni_scoreNS = []
    uni_scorePUB = []
    uni_scorePCP = []
    uni_country = []

    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            uni.append(td.getText())

    for tr in tab.findAll('tr'):
        for td in tr.findAll('img'):
            uni_country.append(td.get('src').replace('image/flag/', '').replace('.png', ''))   

    for i in range(0, len(uni)):
        if (i%9 == 0):
            uni_rank.append(uni[i])
        if (i%9 == 1):
            uni_name.append(uni[i])
        if (i%9 == 3):
            uni_totalscore.append(uni[i])
        if (i%9 == 4):
            uni_scoreAlumni.append(uni[i])
        if (i%9 == 5):
            uni_scoreHici.append(uni[i])
        if (i%9 == 6):
            uni_scoreNS.append(uni[i])
        if (i%9 == 7):
            uni_scorePUB.append(uni[i])
        if (i%9 == 8):
            uni_scoreAward.append(uni[i])
            
    Uni={'WorldRank': uni_rank, 'Institution': uni_name,'Country':uni_country, 'Score Total': uni_totalscore, 
    'Score Alumni': uni_scoreAlumni, 
    'Score Award': uni_scoreAward, 'Score HiCi': uni_scoreHici, 'Score N&S': uni_scoreNS, 
    'Score PUB':uni_scorePUB}

    data=DataFrame(Uni)
    data['Score PCP'] = 'null'
    data['Year'] = year
    rank.append(data)

# 2004
for year in range(2004, 2005):
    url = 'http://www.shanghairanking.com/ARWU' + str(year) + '.html' 
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    tables = soup.findAll('table')
    tab = tables[0]

    uni = []
    uni_rank = []
    uni_name = []
    uni_totalscore = []
    uni_scoreAlumni = []
    uni_scoreAward = []
    uni_scoreHici = []
    uni_scoreNS = []
    uni_scorePUB = []
    uni_scorePCP = []
    uni_country = []

    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            uni.append(td.getText())

    for tr in tab.findAll('tr'):
        for td in tr.findAll('img'):
            uni_country.append(td.get('src').replace('image/flag/', '').replace('.png', ''))   

    for i in range(0, len(uni)):
        if (i%10 == 0):
            uni_rank.append(uni[i])
        if (i%10 == 1):
            uni_name.append(uni[i])
        if (i%10 == 3):
            uni_totalscore.append(uni[i])
        if (i%10 == 4):
            uni_scoreAlumni.append(uni[i])
        if (i%10 == 6):
            uni_scoreHici.append(uni[i])
        if (i%10 == 7):
            uni_scoreNS.append(uni[i])
        if (i%10 == 8):
            uni_scorePUB.append(uni[i])
        if (i%10 == 9):
            uni_scorePCP.append(uni[i])
        if (i%10 == 5):
            uni_scoreAward.append(uni[i])

    Uni={'WorldRank': uni_rank, 'Institution': uni_name,'Country':uni_country, 'Score Total': uni_totalscore,
     'Score Alumni': uni_scoreAlumni, 
    'Score Award': uni_scoreAward, 'Score HiCi': uni_scoreHici, 'Score N&S': uni_scoreNS, 
    'Score PUB':uni_scorePUB, 'Score PCP':uni_scorePCP}

    data=DataFrame(Uni)
    
    data['Year'] = year
    rank.append(data)

# 2005 - 2018
for year in range(2005, 2019):

    url = 'http://www.shanghairanking.com/ARWU' + str(year) + '.html' 
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    tables = soup.findAll('table')
    tab = tables[0]

    uni = []
    uni_rank = []
    uni_name = []
    uni_totalscore = []
    uni_scoreAlumni = []
    uni_scoreAward = []
    uni_scoreHici = []
    uni_scoreNS = []
    uni_scorePUB = []
    uni_scorePCP = []
    uni_country = []

    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            uni.append(td.getText().replace("\n", "").replace("\r", ""))


    # print (uni[1:10])

    for tr in tab.findAll('tr'):
        for td in tr.findAll('img'):
            if (len(uni_country)>499):
                break
            else:
                uni_country.append(td.get('src').replace('image/flag/', '').replace('.png', ''))   
        

    for i in range(0, 500*11):
        if (i%11 == 0):
            uni_rank.append(uni[i])
        if (i%11 == 1):
            uni_name.append(uni[i])
        if (i%11 == 4):
            uni_totalscore.append(uni[i])
        if (i%11 == 5):
            uni_scoreAlumni.append(uni[i])
        if (i%11 == 6):
            uni_scoreAward.append(uni[i])
        if (i%11 == 7):
            uni_scoreHici.append(uni[i])
        if (i%11 == 8):
            uni_scoreNS.append(uni[i])
        if (i%11 == 9):
            uni_scorePUB.append(uni[i])
        if (i%11 == 10):
            uni_scorePCP.append(uni[i])
        
    # print ((uni_name))
    # print (uni_scorePUB)
    # print (len(uni_country))

    Uni={'WorldRank': uni_rank, 'Institution': uni_name,'Country':uni_country, 'Score Total': uni_totalscore, 'Score Alumni': uni_scoreAlumni, 
    'Score Award': uni_scoreAward, 'Score HiCi': uni_scoreHici, 'Score N&S': uni_scoreNS, 
    'Score PUB':uni_scorePUB, 'Score PCP':uni_scorePCP}

    data=DataFrame(Uni)
    data['Year'] = year
    rank.append(data)

# 2019-2020
for year in range(2019, 2021):

    url = 'http://www.shanghairanking.com/ARWU' + str(year) + '.html' 
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    tables = soup.findAll('table')
    tab = tables[0]

    uni = []
    uni_rank = []
    uni_name = []
    uni_totalscore = []
    uni_scoreAlumni = []
    uni_scoreAward = []
    uni_scoreHici = []
    uni_scoreNS = []
    uni_scorePUB = []
    uni_scorePCP = []
    uni_country = []

    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            uni.append(td.getText())

    print(uni[11:23])

    for i in range(0, len(uni)):
        if (i%11 == 0):
            uni_rank.append(uni[i])
        if (i%11 == 1):
            uni_name.append(uni[i])
        if (i%11 == 4):
            uni_totalscore.append(uni[i])

    for tr in tab.findAll('tr'):
        for td in tr.findAll('img'):
            uni_country.append(td.get('src').replace('image/flag/', '').replace('.png', ''))    
        for td in tr.findAll('td', attrs = {"class": "hidden-xs need-hidden alumni"}):
            uni_scoreAlumni.append(td.getText())
        for td in tr.findAll('td', attrs = {"class": "hidden-xs need-hidden award"}):
            uni_scoreAward.append(td.getText())
        for td in tr.findAll('td', attrs = {"class": "hidden-xs need-hidden hici"}):
            uni_scoreHici.append(td.getText())
        for td in tr.findAll('td', attrs = {"class": "hidden-xs need-hidden ns"}):
            uni_scoreNS.append(td.getText())
        for td in tr.findAll('td', attrs = {"class": "hidden-xs need-hidden pub"}):
            uni_scorePUB.append(td.getText())
        for td in tr.findAll('td', attrs = {"class": "hidden-xs need-hidden pcp"}):
            uni_scorePCP.append(td.getText())

    Uni={'WorldRank': uni_rank, 'Institution': uni_name,'Country':uni_country, 'Score Total': uni_totalscore, 'Score Alumni': uni_scoreAlumni, 
    'Score Award': uni_scoreAward, 'Score HiCi': uni_scoreHici, 'Score N&S': uni_scoreNS, 
    'Score PUB':uni_scorePUB, 'Score PCP':uni_scorePCP}

    print(len(uni_rank))
    print(len(uni_name))
    print(len(uni_country))
    print(len(uni_totalscore))
    print(len(uni_scoreAlumni))
    print(len(uni_scoreAward))
    data=DataFrame(Uni)
    data['Year'] = year
    rank.append(data)

Uni_rank = pd.concat(rank)

Uni_rank.replace('\\', 0) 
Uni_rank.replace(' ', 0) 

print (type(Uni_rank['Score Total'][103]))

# Uni_rank.to_csv('ARWU_2003-2020-Overall Rank.csv')