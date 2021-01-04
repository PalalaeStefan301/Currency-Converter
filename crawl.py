from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import requests

def print_file(string,column_nr):
    f = open("currencies","a")
    if column_nr==1:
         string = string.replace("100 ","")
         string = string + " "
    f.write(string)
    if column_nr==2:
        f.write('\n')

def read_value_of_currency(searched_currency):
    f = open("currencies","r")
    for i in range(33):
        temp = f.readline()
        temp = temp.split(' ')
        if(temp[0]==searched_currency):
            return temp[1]
    #print(list)
    f.close()

def read_currencies():
    list = []
    f = open("currencies","r")
    for i in range(33):
        temp = f.readline()
        temp = temp.split(' ')
        list.append(temp[0])
    list.sort()
    return list

def main():
    f = open("currencies","a")
    f.truncate(0)
    link = "https://bnr.ro/Exchange-rates-15192.aspx"
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    tb = soup.find('table')
    list_t = []
    i = 0
    for td_elem in tb.find_all('th'):
        if i!=0:
            list_t.append(td_elem.get_text())
            #print_file(str(td_elem.get_text()))
        i = i+1
    i = 0
    for td_elem in tb.find_all('td'):
        if i!=0:
            list_t.append(td_elem.get_text())
            #print_file(str(td_elem.get_text()))
        if i>31:
            break
        i = i+1
    for i in range(0,32):
        print_file(list_t[i],1)
        print_file(list_t[i+32],2)
    print_file("RON",1)
    print_file("1.0000",2)
        
        


main()
