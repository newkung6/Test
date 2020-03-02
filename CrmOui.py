#!/usr/local/bin/python 
import time
from time import gmtime, strftime 
from PIL import Image

from selenium import webdriver
#  import for explicit wait and another thing
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#Webdriver Setting
# chrome_options = webdriver.Chrome(executable_path=r'C:\Users\Nsan\code\Seletest\Driver\chromedriver.exe')
chrome_options = Options()
#don't use headless
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-logging")

#chrome_options.add_argument("--log-level=3")

chrome_options.add_argument("--proxy-server=proxy.true.th:80")
chrome_options.add_argument("--proxy-bypass-list=*.true.th;172.*")

chrome_options.add_argument("--disable-3d-apis")
chrome_options.add_argument("--disable-accelerated-video")
chrome_options.add_argument("--disable-background-mode")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-plugins")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--disable-preconnect")
chrome_options.add_argument("--disable-translate")


# chrome_options = webdriver.Chrome(executable_path=r'C:\Users\Nsan\code\Seletest\Driver\chromedriver.exe')
# driver = webdriver.Remote('http://172.19.187.122:14120/wd/hub', chrome_options.to_capabilities())
# driver = webdriver.Remote('http://172.16.40.245:5544/wd/hub', chrome_options.to_capabilities())
driver = webdriver.Remote('http://172.19.176.213:13333/wd/hub', chrome_options.to_capabilities())
driver.set_window_size(1360,1280)

driver.get("http://itpmon.true.th/zabbix") 
# Login
driver.find_element_by_xpath('//*[@id="name"]').send_keys("crmmonitor")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("P@ssw0rd")
# wait until element show
wait = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="enter"]'))
)
wait.click()
print("complete")
#changePathHere
path = "/Users/Nsan/code/MRCtest/"
# path = "/root/pytest/"


driver.get("http://itpmon.true.th/zabbix") 
# Login
driver.find_element_by_xpath('//*[@id="name"]').send_keys("crmmonitor")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("P@ssw0rd")
# wait until element show
wait = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="enter"]'))
)
wait.click()
print("complete")

try:
    #OUI
    driver.get("http://itpmon.true.th/zabbix/charts.php?page=1&groupid=0&hostid=13673&graphid=26755&action=showgraph") 
    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="graph_full"]'))
    )
    # driver.execute_script("window.scrollTo(0, 150)") 
    # driver.save_screenshot(format(strftime("OUI-%Y%m%d-%H%M%S"))+".png")
    element = driver.find_element_by_xpath('//*[@id="graph_full"]')
    name = format(strftime("OUI-%Y%m%d-%H%M"))
    driver.save_screenshot(path+name+".png")
    location = element.location
    size = element.size
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']
    im = Image.open(path + name + '.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(path+name+".png")
    im.save(path+"OUI.png")
    print("OUI")
except:
    print("it's have a Problem with OUI")

try:
    #Eai
    driver.get("http://itpmon.true.th/zabbix/charts.php?page=1&groupid=0&hostid=13673&graphid=26637") 
    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="graph_full"]'))
    )
    # driver.execute_script("window.scrollTo(0, 200)") 
    # driver.save_screenshot(format(strftime("Eai-%Y%m%d-%H%M%S"))+".png")
    element = driver.find_element_by_xpath('//*[@id="graph_full"]')
    name = format(strftime("EAI-%Y%m%d-%H%M"))
    driver.save_screenshot(path+name+".png")
    location = element.location
    size = element.size
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']

    im = Image.open(path + name + '.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(path+name+".png")
    im.save(path+"EAI.png")
    print("EAI")
except:
    print("it's have a Problem with EAI")

try:
    #WorkFlow
    driver.get("http://itpmon.true.th/zabbix/charts.php?page=1&groupid=22&hostid=21768&graphid=37005&action=showgraph") 
    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="graph_full"]'))
    )
    # driver.execute_script("window.scrollTo(0, 200)") 
    # driver.save_screenshot(format(strftime("Eai-%Y%m%d-%H%M%S"))+".png")
    element = driver.find_element_by_xpath('//*[@id="graph_full"]')
    name = format(strftime("Workflow-%Y%m%d-%H%M"))
    driver.save_screenshot(path+name+".png")
    location = element.location
    size = element.size
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']

    im = Image.open(path + name + '.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(path+name+".png")
    im.save(path+"Workflow.png")
    print("Workflow")
    driver.find_element_by_xpath('//*[@id="mmenu"]/ul/li[2]/ul/li[5]/a').click()
    print("Logoutitp")
except:
    print("it's have a Problem with Workflow")
    driver.find_element_by_xpath('//*[@id="mmenu"]/ul/li[2]/ul/li[5]/a').click()
    print("Logoutitp")

try:
    #Disk Usage
    driver.get("http://itzbmon.true.th/zabbix/") 
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("mrcmon")
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("P@ssw0rd")
    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="enter"]'))
    )
    wait.click()
    print("logIn ITZ")
    driver.get("http://itzbmon.true.th/zabbix/history.php?sid=d659d431c8f54d45&form_refresh=1&action=batchgraph&itemids%5B3101154%5D=3101154&itemids%5B3101156%5D=3101156&graphtype=0") 
    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="scrollbar_cntr"]/div[1]/div[1]/div[1]/span[2]/a[9]'))
    )
    wait.click()
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="historyGraph"]')
    name = format(strftime("Disk-%Y%m%d-%H%M"))
    driver.save_screenshot(path+name+".png")
    location = element.location
    size = element.size
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']

    im = Image.open(path + name+'.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(path+name+".png")
    im.save(path+"Disk.png")
    print("Disk")
except:
    print("it's have a Problem with Disk Usage")

try:
    #CRMAdapterCPU
    driver.get("http://itzbmon.true.th/zabbix/history.php?sid=00e04faeb2497b36&form_refresh=1&action=batchgraph&itemids%5B3114661%5D=3114661&itemids%5B3114721%5D=3114721&itemids%5B3114781%5D=3114781&itemids%5B3114841%5D=3114841&graphtype=0") 
    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="scrollbar_cntr"]/div[1]/div[1]/div[1]/span[2]/a[7]'))
    )
    wait.click()
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="historyGraph"]')
    name = format(strftime("ADPCPU-%Y%m%d-%H%M"))
    driver.save_screenshot(path+name+".png")
    location = element.location
    size = element.size
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']

    im = Image.open( path + name+'.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(path+name+".png")
    im.save(path+"ADPCPU.png")
    print("ADPCPU")
except:
    print("it's have a Problem with"+name)
    driver.find_element_by_xpath('//*[@id="mmenu"]/ul[2]/li[5]/a').click()

try:
    #CRMAdapterMem
    driver.get("http://itzbmon.true.th/zabbix/history.php?sid=00e04faeb2497b36&form_refresh=1&action=batchgraph&itemids%5B3114641%5D=3114641&itemids%5B3114701%5D=3114701&itemids%5B3114761%5D=3114761&itemids%5B3114821%5D=3114821&itemids%5B3114641%5D=3114641&itemids%5B3114701%5D=3114701&itemids%5B3114761%5D=3114761&itemids%5B3114821%5D=3114821&graphtype=0") 
    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="scrollbar_cntr"]/div[1]/div[1]/div[1]/span[2]/a[7]'))
    )
    wait.click()
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="historyGraph"]')
    name = format(strftime("ADPMEM-%Y%m%d-%H%M"))
    driver.save_screenshot(path+name+".png")
    location = element.location
    size = element.size
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']

    im = Image.open( path + name+'.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(path+name+".png")
    im.save(path+"ADPMEM.png")
    print("ADPMEM")
except:
    print("it's have a Problem with"+name)
    driver.find_element_by_xpath('//*[@id="mmenu"]/ul[2]/li[5]/a').click()

try:
    #ESBCPU
    driver.get("http://itzbmon.true.th/zabbix/history.php?sid=5764fd4dffccf388&form_refresh=1&action=batchgraph&all_items=1&itemids%5B1262652%5D=1262652&itemids%5B1262845%5D=1262845&itemids%5B1262593%5D=1262593&itemids%5B1262912%5D=1262912&itemids%5B1262534%5D=1262534&itemids%5B1262180%5D=1262180&itemids%5B1262121%5D=1262121&itemids%5B1262062%5D=1262062&itemids%5B1262711%5D=1262711&itemids%5B1262003%5D=1262003&itemids%5B1261944%5D=1261944&itemids%5B1262239%5D=1262239&itemids%5B1653441%5D=1653441&itemids%5B1653527%5D=1653527&graphtype=0") 
    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="scrollbar_cntr"]/div[1]/div[1]/div[1]/span[2]/a[7]'))
    )
    wait.click()
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="historyGraph"]')
    name = format(strftime("ESBCPU-%Y%m%d-%H%M"))
    driver.save_screenshot(path+name+".png")
    location = element.location
    size = element.size
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']

    im = Image.open( path + name+'.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(path+name+".png")
    im.save(path+"ESBCPU.png")
    print("ESBCPU")
except:
    print("it's have a Problem with"+name)
    driver.find_element_by_xpath('//*[@id="mmenu"]/ul[2]/li[5]/a').click()
    
try:
    #ESBMem
    driver.get("http://itzbmon.true.th/zabbix/history.php?sid=00e04faeb2497b36&form_refresh=1&action=batchgraph&itemids%5B3114641%5D=3114641&itemids%5B3114701%5D=3114701&itemids%5B3114761%5D=3114761&itemids%5B3114821%5D=3114821&itemids%5B3114641%5D=3114641&itemids%5B3114701%5D=3114701&itemids%5B3114761%5D=3114761&itemids%5B3114821%5D=3114821&graphtype=0") 
    wait = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="scrollbar_cntr"]/div[1]/div[1]/div[1]/span[2]/a[7]'))
    )
    wait.click()
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="historyGraph"]')
    name = format(strftime("ESBMEM-%Y%m%d-%H%M"))
    driver.save_screenshot(path+name+".png")
    location = element.location
    size = element.size
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']

    im = Image.open( path + name+'.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(path+name+".png")
    im.save(path+"ESBMEM.png")
    print("ESBMEM")
    driver.find_element_by_xpath('//*[@id="mmenu"]/ul[2]/li[5]/a').click()
    print("Logoutitz")
except:
    print("it's have a Problem with "+name)
    driver.find_element_by_xpath('//*[@id="mmenu"]/ul[2]/li[5]/a').click()
    print("Logoutitz")


# driver.get("https://172.19.190.147:1158/em/console/logon/logoff?event=load")
# driver.find_element_by_xpath('//*[@id="mmenu"]/ul/li[2]/ul/li[5]/a').click()
# print("Logout")
driver.close()
driver.quit()
