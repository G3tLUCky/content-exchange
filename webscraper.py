# -*- coding: utf-8 -*-
import requests, csv
from bs4 import BeautifulSoup

url = "https://www.nporadio1.nl/binnenland/25799-de-coronacijfers-van-vandaag"
response = requests.get(url)#get the html-code
response_text = response.text

souped_page = BeautifulSoup(response_text, 'html.parser')#parse the html-code
dates = souped_page.find_all('h2')#find all dates by looking at the text between h2-tags
dates_list = []
for d in dates:
    dates_list.append(d.getText())
while "\xa0" in dates_list:
    dates_list.remove("\xa0")#remove these random elements
del dates_list[-3:]#last four elements don't refer to the date
#now, we have a clean list of dates that can be matched with the numbers regarding covid-19
    
numbers1 = souped_page.find_all('strong')
#all numbers that can be found between the strong-tags
numbers2 = souped_page.find_all('b')
#for some reason, only some numbers are put between b-tags, so we have to run a separate
#find_all function

n1_list = []
n2_list = []
all_numbers = []#--> final list with all the numbers

num_container = ""
for n1 in numbers1:
    try:
        n1 = n1.getText()#first, turn the element into text that can be read by python
        if len(n1)==1:#had to write this because of some stupid piece of html-code: please
        #ask/contact me if this is not clear (will add better comments in the future)
            num_container = n1
            continue
        n1 = n1.replace(".", "")
        #replace all dots (some numbers on the website are indicated like '1.234.567' which 
        #makes it hard to use the float function)
        n1 = num_container + n1
        n1 = int(n1)
        n1_list.append(n1)
        num_container = ""
    except:#if the element is not a number and therefore cannot be converted by the float-function
        continue#then just continue the loop without crashing

#same principles as the for loop above, but with some extra text replacements (see html-code for b-tags)
for n2 in numbers2:
    try:
        n2 = n2.getText()
        n2 = n2.replace(".", "")
        n2 = n2.replace(":", "")
        n2 = n2.replace(" ", "")
        n2 = int(n2)
        n2_list.append(n2)
    except:
        continue

i = 3
j = 0
for x in n1_list:
    all_numbers.append(x)
    i -= 1
    if i<=0 and j!=len(n2_list):
        all_numbers.append(n2_list[j])
        j += 1
        i = 7
    
csv_file = open("npo_numbers.csv", 'w', newline = '')
field_names = ['Date', 'Nieuwe Besmettingen', 'Totaal Besmettingen', 
               'Totaal Kliniek', 'Nieuw Kliniek', 'Totaal IC', 'Nieuw IC',
               'Nieuwe Doden', 'Totaal Doden']
writer = csv.DictWriter(csv_file, fieldnames=field_names)
writer.writeheader()
#write all data to an csv-file

l = 0
for line in dates_list:
    writer.writerow({'Date': line, 'Nieuwe Besmettingen': all_numbers[dates_list.index(line) + 7*l],
                     'Totaal Besmettingen': all_numbers[dates_list.index(line) + 7*l + 1], 
                     'Totaal Kliniek': all_numbers[dates_list.index(line) + 7*l + 2], 
                     'Nieuw Kliniek': all_numbers[dates_list.index(line) + 7*l + 3], 
                     'Totaal IC': all_numbers[dates_list.index(line) + 7*l + 4], 
                     'Nieuw IC': all_numbers[dates_list.index(line) + 7*l + 5],
                     'Nieuwe Doden': all_numbers[dates_list.index(line) + 7*l + 6], 
                     'Totaal Doden': all_numbers[dates_list.index(line) + 7*l + 7]})
    l += 1
csv_file.close()