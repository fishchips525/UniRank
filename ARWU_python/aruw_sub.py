# https://zhuanlan.zhihu.com/p/32568168

import requests
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame
import pandas as pd
import re

rank = []

# head request
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}


# print (result[0][1].replace('&amp;','&'))
# print (result[0][0])

def rank_subject(year, subject_html, subject):

    if (year == 2020):
        url = 'http://www.shanghairanking.com/Shanghairanking-Subject-Rankings/' + subject_html
        print ('********************')
        print(url)
    else:
        url = 'http://www.shanghairanking.com/Shanghairanking-Subject-Rankings-' + year + '/' + subject_html

    # print(url)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    tables = soup.findAll('table')
    tab = tables[0]
    # print (tab)

    uni = []
    uni_rank = []
    uni_name = []
    uni_country = []
    uni_NationalRank = []
    uni_totalscore = []
    uni_scoreQ1 = []
    uni_scoreCNCI = []
    uni_scoreIC = []
    uni_scoreTOP = []
    uni_scoreAward = []

    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            uni.append(td.getText())

    # print(uni[0:11])


    for tr in tab.findAll('tr'):
        for td in tr.findAll('img'):
            # print (td)
            uni_country.append(td.get('src').replace('image/flag/', '').replace('.png', ''))   
        

    for i in range(len(uni)):
        if (i%10 == 0):
            uni_rank.append(uni[i])
        if (i%10 == 1):
            uni_name.append(uni[i])
        if (i%10 == 3):
            uni_NationalRank.append(uni[i])
        if (i%10 == 4):
            uni_totalscore.append(uni[i])
        if (i%10 == 5):
            uni_scoreQ1.append(uni[i])
        if (i%10 == 6):
            uni_scoreCNCI.append(uni[i])
        if (i%10== 7):
            uni_scoreIC.append(uni[i])
        if (i%10 == 8):
            uni_scoreTOP.append(uni[i])
        if (i%10 == 9):
            uni_scoreAward.append(uni[i])

    # print(len(uni_rank)) 
    # print(len(uni_name))
    # print(len(uni_country))
    # print(len(uni_NationalRank))
    # print(len(uni_totalscore))
    # print(len(uni_scoreQ1))
    # print(len(uni_scoreCNCI))
    # print(len(uni_scoreIC))
    # print(len(uni_scoreTOP))
    # print(len(uni_scoreAward))

    Uni_Subject={'WorldRank': uni_rank, 'Institution': uni_name,'Country':uni_country, 'Nationa Rank': uni_NationalRank, 
    'Total Score': uni_totalscore, 
    'Score Q1': uni_scoreQ1, 'Score CNCI': uni_scoreCNCI, 'Score IC': uni_scoreIC, 
    'Score TOP':uni_scoreTOP, 'Score Award':uni_scoreAward}

    data=DataFrame(Uni_Subject)
    data['Subject'] = subject
    data['Year'] = year
    rank.append(data)

    # print (rank)


def subject_year(year):

    if (year == 2020):
        url = 'http://www.shanghairanking.com/Shanghairanking-Subject-Rankings/index.html'
    else:
        url = 'http://www.shanghairanking.com/Shanghairanking-Subject-Rankings-' + str(year) + '/index.html'

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    result = re.findall('<a.*?href="(.*?)">(.*?)</a>', str(soup.find_all("a")))

    # print (result)

    for i in range(0, len(result)):
        try:
            if (result[i][1].replace('&amp;','&')  == '2004'):
                print (result)
                break
            else:
                rank_subject(year, result[i][0], result[i][1].replace('&amp;','&') )
                print ("Success:" + result[i][0])
        except:
            print ("Error:" + result[i][0])

subject_year(2020)
Uni_rank_subject = pd.concat(rank)
Uni_rank_subject.to_csv('ARWU_2017-2020_Subject.csv')

# url = 'http://www.shanghairanking.com/Shanghairanking-Subject-Rankings-2017/index.html'
# res = requests.get(url, headers=headers)
# soup = BeautifulSoup(res.text, 'html.parser')

# result = re.findall('<a.*?href="(.*?)">(.*?)</a>', str(soup.find_all("a")))

# # print (result)

# url = 'http://www.shanghairanking.com/Shanghairanking-Subject-Rankings-2017/statistics.html'
# res = requests.get(url, headers=headers)
# soup = BeautifulSoup(res.text, 'html.parser')


# print (soup)