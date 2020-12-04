from selenium import webdriver


def print_file(string):
    f = open("output","a")
    f.truncate(0)
    for i in range(32):
        f.write(string[i]+" "+string[i+32]+"\n")
    f.write("RON 1.0000")
    f.close()
def crawl():
    print("Taking current currencies...")
    PATH  = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://bnr.ro/Exchange-rates-15192.aspx")
    content = driver.find_element_by_tag_name("tbody")
    string = ""
    string = content.text
    string = string.replace("\n"," ")
    string = string.split(' ')
    del string[0]
    del string[9]
    del string[10]
    del string[22]
    del string[32]
    del string[64:len(string)]
    print_file(string)
    driver.quit()
    print("Current currencies are stored")
def read_value_of_currency(searched_currency):
    f = open("output","r")
    for i in range(33):
        temp = f.readline()
        temp = temp.split(' ')
        if(temp[0]==searched_currency):
            return temp[1]
    #print(list)
    f.close()
def read_currencies():
    list = []
    f = open("output","r")
    for i in range(33):
        temp = f.readline()
        temp = temp.split(' ')
        list.append(temp[0])
    list.sort()
    return list

#crawl()