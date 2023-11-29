#imports
from selenium import webdriver
import time


chrome_driver_path="your chrome browser path"

driver=webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://orteil.dashnet.org/experiments/cookie/") #the link to the web game 



timeout = time.time() + 5  #five seconds from now
five_min = time.time() + 60*5 # 5minute



while True:
    cookieelement=driver.find_element_by_id("#cookie") 
    cookieelement.click()
    if time.time() > timeout:
          spells=['buyCursor','buyGrandma','buyFactory','buyMine','buyShipment','buyAlchemy lab','buyPortal','buyTime machine'] #features in the web game
          upgrades_number=[(driver.find_element_by_xpath(f"//*[@id={spell}]/b/text()[2]").text for spell in spells)]
      
          cookienumber=driver.find_element_by_id("#money") 
          money=int(cookienumber.text)

          run=upgrades_number.reverse()
          rspells=spells.reverse()
      
          for number in run:
            if money>=int(number):  #if money is equal to the features money , then buy the features 
              spell_box=(driver.find_element_by_id(f"#{rspells[number]}"))
              spell_box.click()

          timeout = time.time() + 5 #increasing the time to give our money a chance to grow and get more powerfull features !

    if time.time() > int(five_min):
          cookie_per_s = driver.find_element_by_id("cps").text
          print(cookie_per_s)
          break





# so we are saying start the timer , it begans with 0 , once it starts ,
#  it start clicking , then when the timer is bigger than the range that we provide(5seconds) ,
#  check the money , if its equal to any amount but in an descending order giving the periuority to the biggest ,
#  then the check ends , here we add another 5 seconds to the timer range and its now at 10 , we says that as much as its < than 10 ,
#  keep clicking until it reaches 11 , and we keep so until the timer is 5min , here the loop breaks and the checking ,
#  and we print out the number of cookies!






