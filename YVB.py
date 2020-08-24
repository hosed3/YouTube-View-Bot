#liberaries
from selenium import webdriver #click on "install liberaries.bat" in main folder
import time
driver = webdriver.Chrome(executable_path= r'chromedriver.exe')

Timer = 3 #this set time in secounds, after the page is refresh, optimally value 3-5
link = 'https://www.youtube.com/watch?v=gz-kUmx1GmE' #put here link to video 
views = 3 #this is amount of views after the program stop and ask u want to do script again
n = 0 #DONT CHANGE THIS ITS TO COUNT VIEWS

driver = webdriver.Chrome() #Open web driver
driver.get(link) #Open chrome and passes to link 
for i in range(views): #function to refresh pages and count views, just dont change anything in this
    time.sleep(Timer)
    if driver.refresh():
        n += 1
        print("View: ", n)
    else:
        n += 1
        print("View: ", n)