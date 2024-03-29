from pathlib import Path

from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import re
from selenium import webdriver
from time import sleep
import openpyxl


def getUser(user, driver):
    url = "https://music.163.com/#/search/m/?type=1002"
    driver.get(url)
    driver.switch_to.frame('g_iframe')
    sleep(0.1)
    driver.find_element_by_id('m-search-input').send_keys(user)
    driver.find_element_by_id('m-search-input').send_keys(Keys.ENTER)
    sleep(0.5)
    try:
        tab = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/table/tbody')
        users = tab.find_elements_by_tag_name('a')
    except:
        print('error')
        return None
    list = []
    for i, n in enumerate(users):
        if (i - 1) % 3 == 0:
            tu = (n.get_attribute('title'), n.get_attribute('href'))
            list.append(tu)
    return list

def getListSong(str, driver):
    url = "https://music.163.com/#/search/m/?type=1000"
    driver.get(url)
    driver.switch_to.frame('g_iframe')
    sleep(0.1)
    driver.find_element_by_id('m-search-input').send_keys(str)
    driver.find_element_by_id('m-search-input').send_keys(Keys.ENTER)
    sleep(0.5)
    try:
        tab = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/table/tbody')
        lists = tab.find_elements_by_tag_name('a')
    except:
        print('error')
        return None
    list = []
    for i, n in enumerate(lists):
        if (i - 2) % 4 == 0:
            tu = (n.get_attribute('title'), n.get_attribute('href'))
            list.append(tu)
    return list

def getSongSearch(str, driver):
    url = "https://music.163.com/#/search/m/?type=1"
    driver.get(url)
    driver.switch_to.frame('g_iframe')
    sleep(0.1)
    driver.find_element_by_id('m-search-input').send_keys(str)
    driver.find_element_by_id('m-search-input').send_keys(Keys.ENTER)
    sleep(0.5)
    try:
        tab = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div')
        songs = tab.find_elements_by_class_name('text')
    except:
        print('error')
        return None
    list = []
    for i, n in enumerate(songs):
        if i % 3 == 0:
            tu = (n.find_element_by_tag_name('a').find_element_by_tag_name('b').get_attribute('title'), n.find_element_by_tag_name('a').get_attribute('href'))
            list.append(tu)
    return list


def getSongs(user, driver):
    driver.get(user[1])
    sleep(1)
    driver.switch_to.frame('g_iframe')
    try:
        box = driver.find_element_by_xpath('//*[@id="cBox"]')
        li = box.find_elements_by_tag_name('a')
    except:
        print('error')
        return None
    list = []
    for i, n in enumerate(li):
        if i % 3 == 0:
            tu = (n.get_attribute('title'), n.get_attribute('href'))
            list.append(tu)
    print(user[0] + '创建的歌单如下：')
    for i, n in enumerate(list):
        print('[' + str(i) + ']\t' + n[0] + '\t' + n[1])
    return list

def getAsong(wb,I,i,dicurl,driver):
    comment = getComment(driver, dicurl, i)
    sheet = wb.active
    for n in comment:
        sheet['A' + str(I)].value = n['歌曲']
        sheet['B' + str(I)].value = n['用户']
        sheet['C' + str(I)].value = n['内容']
        sheet['D' + str(I)].value = n['时间']
        sheet['E' + str(I)].value = n['点赞数']
        sheet['F' + str(I)].value = n['类型']
        sheet['G' + str(I)].value = n['关联评论']
        I+=1
    return I

def getSong(songlist,driver,I,wb):
    driver.get(songlist[1])
    driver.switch_to.frame('contentFrame')
    sleep(1)
    a = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[2]/div/div/div/span/a')
    b = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[2]/div/div/div/span/a/b')
    dic = {}
    for i in range(len(a)):
        title = b[i].get_attribute('title')
        dic[title] = [a[i].get_attribute('href')]
    for i in dic:
        I=getAsong(wb,I,i,dic[i][0],driver)
    return I

def getASonglist(songlist,driver):
    driver.get(songlist[1])
    driver.switch_to.frame('contentFrame')
    sleep(1)
    a = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[2]/div/div/div/span/a')
    b = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[2]/div/div/div/span/a/b')
    li = []
    for i in range(len(a)):
        dic=[]
        dic.append(b[i].get_attribute('title'))
        dic.append(a[i].get_attribute('href'))
        li.append(dic)
    return li

def giveValue(dic,i,str):
    dic[i]=str
    print(dic)

def search(driver,dic,str,li):
    if dic['searchtype']==0:
        li=getUser(str,driver)
    elif dic['searchtype']==1:
        li = getSongSearch(str, driver)
    elif dic['searchtype']==2:
        li = getListSong(str, driver)
    return li

def savefile(wb,name,url):
    num = 0;
    my_file = Path("{}/{}_{}.xlsx".format(url, name, str(num)))
    while my_file.is_file( ):
         num = num + 1;
         my_file = Path("{}/{}_{}.xlsx".format(url, name, str(num)))
    wb.save("{}/{}_{}.xlsx".format(url, name, str(num)))
    print("保存成功！")

def save(driver,dic, str,url,name):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'].value = '歌曲名'
    sheet['B1'].value = '用户'
    sheet['C1'].value = '内容'
    sheet['D1'].value = '时间'
    sheet['E1'].value = '点赞数'
    sheet['F1'].value = '类型'
    sheet['G1'].value = '关联评论'
    I = 2
    print(str)
    print(dic['searchtype'])
    if dic['searchtype']==0:
        li = []
        for i in str:
            li.append(getSongs(i,driver))
        print(li)
        for i in li:
            for j in i:
              I=getSong(j,driver,I,wb)
        name="用户"+name

    elif dic['searchtype']==1:
        for i in str:
            I=getAsong(wb,I,i[0],i[1],driver)+1
        name="歌曲"+name

    elif dic['searchtype']==2:
        for i in str:
            I=getSong(i,driver,I,wb)
        name="歌单"+name
    savefile(wb,name,url)

def login(driver,dic):
    url = "https://music.163.com/#/search/m/"
    driver.get(url)
    try:
        if dic['lognStatus'] == 1:
            ActionChains(driver).move_to_element(
                driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[1]')).perform()
            driver.find_element_by_class_name('itm-3').click()
        sleep(0.1)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]').click()
        sleep(0.1)
        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/div/div[3]').click()
        sleep(0.1)
        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[1]/div[3]/input').click()
        sleep(0.1)
        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[1]/div[1]/div[2]').click()
        sleep(0.1)
        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[1]/div/div/input').send_keys(dic['user'])
        sleep(0.1)
        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[2]/input').send_keys(
            dic['pwd'] + Keys.ENTER)
        sleep(0.5)
        dic['lognStatus'] = 1
        dic['url'] = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/a').get_attribute('href')
        driver.get(dic['url'])
        sleep(1)
        dic['name'] = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/a').get_attribute('textContent')
        if  dic['name']=='登录':
            dic['lognStatus'] = 0
    except:
        print('error')

    print(dic)



def getComment(driver, url, song):
    driver.get(url)
    sleep(1)
    driver.switch_to.frame('g_iframe')
    try:
        client = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/a')
        time = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[@class="rp"]/div')
        thumbs = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[@class="rp"]/a[1]')
        text = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]')
    except:
        print('error')
        return None
    print('正在爬取:' + song)
    li = []
    for n, i in enumerate(time):
        if n >= 15:
            break
        if re.search(r'[(](.*)[)]', thumbs[n].text) == None:
            thumb = '0'
        else:
            thumb = re.findall(r'[(](.*)[)]', thumbs[n].text)[0]
        if re.search(r'万', thumb) != None:
            thumb = thumb.split('万')[0]
            thumb = int(float(thumb) * 10000)
        else:
            thumb = int(thumb)
        comment = {
            '歌曲': song,
            '用户': client[n].text,
            '内容': ILLEGAL_CHARACTERS_RE.sub(r'', re.findall(r'：(.*)' + i.text, text[n].get_attribute('textContent'))[0]),
            '时间': i.text,
            '点赞数': thumb,
            '类型': '评论',
            '关联评论': '无'
        }
        if re.search(r'◆◆', comment['内容']) != None:
            tu = re.findall(r'(.*)◆◆(.*)', comment['内容'])[0]
            comment['内容'] = tu[0]
            comment['类型'] = '回复'
            comment['关联评论'] = tu[1]
        li.append(comment)
    return li
