from selenium import webdriver


def print_file(string):
    f = open("output","a")
    f.truncate(0)
    for i in range(len(string)):
        f.write(string[i])
        f.write(' ')
    f.close()
def crawl():
    PATH  = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://bnr.ro/Exchange-rates-1224.aspx")
    content = driver.find_element_by_id("ctl00_ctl00_CPH1_CPH1_ctl00_phContent")
    string = ""
    string = content.text
    string = string.replace("\n"," ")
    string = string.split(' ')
    #print(string)
    print_file(string)
    driver.quit()
def read_currencies():
    f = open("output","r")
    list = f.read()
    list = list.split(" ")
    del list[0:10]
    
    for i in range(0,7):
        del list[(2*i)+0:(2*i)+2]
        del list[(2*i)+1:(2*i)+5]
    del list[14:15]
    del list[15:19]
    print(list)
    

crawl()
read_currencies()