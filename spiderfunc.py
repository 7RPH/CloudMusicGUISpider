from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import re
from selenium import webdriver
from time import sleep
import openpyxl


def getUser(user, driver):
    url = "https://music.163.com/#/search/m/"
    driver.get(url)
    driver.switch_to.frame('g_iframe')
    sleep(1)
    driver.find_element_by_id('m-search-input').send_keys(user)
    driver.find_element_by_id('m-search-input').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@class="m-tabs m-tabs-srch f-cb ztag"]/li[8]').click()
    sleep(1)
    tab = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/table/tbody')
    users = tab.find_elements_by_tag_name('a')
    list = []
    for i, n in enumerate(users):
        if (i - 1) % 3 == 0:
            tu = (n.get_attribute('title'), n.get_attribute('href'))
            list.append(tu)
    for i, n in enumerate(list):
        print('[' + str(i) + ']\t' + n[0] + '\t' + n[1])
    num = input('请输入用户对应序号：')
    return list[int(num)]


def getSongs(user, driver):
    driver.get(user[1])
    sleep(1)
    driver.switch_to.frame('g_iframe')
    box = driver.find_element_by_xpath('//*[@id="cBox"]')
    li = box.find_elements_by_tag_name('a')
    list = []
    for i, n in enumerate(li):
        if i % 3 == 0:
            tu = (n.get_attribute('title'), n.get_attribute('href'))
            list.append(tu)
    print(user[0] + '创建的歌单如下：')
    for i, n in enumerate(list):
        print('[' + str(i) + ']\t' + n[0] + '\t' + n[1])
    num = input('请选择对应歌单:')
    return list[int(num)]

def login(driver,user,pwd,login):
    sleep(0.1)
    if login==True:
        #driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[1]').click()
        sleep(0.1)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/ul[3]/li').click()
        sleep(0.1)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/ul[3]/li').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/div/div[3]').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[1]/div[3]/input').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[1]/div[1]/div[2]').click()
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[1]/div/div/input').send_keys(user)
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[2]/input').send_keys(
        pwd + Keys.ENTER)
    sleep(0.1)
    login=True
    print(whoami(driver))

def whoami(driver):
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul/li[2]').click()
    return driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[1]/div/div[2]/div/div[2]/span[1]').find_element_by_tag_name('a')

def getSong(driver, songsname):
    login(driver,'13636193157','Frank5379768')
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
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.merge_cells(start_row=1, start_column=1, end_row=1, end_column=7)
    sheet['A1'].value = songsname
    sheet['A2'].value = '歌曲名'
    sheet['B2'].value = '用户'
    sheet['C2'].value = '内容'
    sheet['D2'].value = '时间'
    sheet['E2'].value = '点赞数'
    sheet['F2'].value = '类型'
    sheet['G2'].value = '关联评论'
    I = 3
    for i in dic:
        # print(i,dic[i][0])
        comment = getComment(driver, dic[i][0], i)
        for n in comment:
            sheet['A' + str(I)].value = n['歌曲']
            sheet['B' + str(I)].value = n['用户']
            sheet['C' + str(I)].value = n['内容']
            sheet['D' + str(I)].value = n['时间']
            sheet['E' + str(I)].value = n['点赞数']
            sheet['F' + str(I)].value = n['类型']
            sheet['G' + str(I)].value = n['关联评论']
            I += 1
    wb.save(filename=songsname + '歌单爬取.xlsx')

def getComment(driver, url, song):
    driver.get(url)
    sleep(1)
    driver.switch_to.frame('g_iframe')
    # comment=driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]')
    # print(song)
    # for n, i in enumerate(comment):
    #     if n >= 15:
    #         break
    #     print(i.get_attribute('textContent'))
    #     text = i.get_attribute('textContent')
    #     li = re.findall(r'(.*?)：(.*)20(.*?)日 [(](.*?)[)][|]回复', text)[0]
    #     print(li)
    #     content = {
    #         '用户': li[0],
    #         '内容': li[1],
    #         '时间': '20' + li[2] + '日',
    #         '点赞数': li[3]
    #     }
    #     print(content)
    client = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/a')
    # content=driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div')
    time = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[@class="rp"]/div')
    thumbs = driver.find_elements_by_xpath(
        '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[@class="rp"]/a[1]')
    text = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]')
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
            # print(tu[0]+'回复了评论：'+tu[1])
            comment['内容'] = tu[0]
            comment['类型'] = '回复'
            comment['关联评论'] = tu[1]
        li.append(comment)
    # print(li)
    return li

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(chrome_options=chrome_options)
# user = input('请输入你要查找的用户：')
# li = getUser(user, driver)
# songs = getSongs(li, driver)
# print('准备开始爬取歌单: ' + songs[0] + ' 中的内容')
# driver.get(songs[1])
# getSong(driver, songs[0])
# driver.quit()
