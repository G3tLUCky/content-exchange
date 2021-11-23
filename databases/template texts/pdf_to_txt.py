from PyPDF2 import PdfFileReader
import os

pdf_path = os.getcwd()+ "/texts"
files = os.listdir(pdf_path)
pdf_list = []
for f in files:
    file = PdfFileReader(f)
    pdf_list.append(file)

text_list = []
for pdf in pdf_list:
    for p in range(100):
        page = pdf.getPage(p).extractText()
        page = page.split("\n")
        text_list.append(page)

sentence_list = []
for text in text_list:
    for t in text:   
        sentence_list.append(t)
 
for s in sentence_list:
    if s=="Section:" or s=="Highlight:" or s=="Byline:" or s=="Load-Date:" or s=="Dateline:":
            sentence_list[sentence_list.index(s)+1] = "/n"
            sentence_list[sentence_list.index(s)] = "/n"
        
    elif s.startswith("Copyright") or s==("Body") or (s.startswith("Page") and "of" in s) or len(s)<1:
        sentence_list[sentence_list.index(s)] = "/n"

while "/n" in sentence_list:
    sentence_list.remove("/n")

os.chdir("..")
data_fp = open("data_texts.txt", "w", encoding="utf-8")
tele_nl, tele, trouw, nrc_handel, nrc, volks = 0, 0, 0, 0, 0, 0
jan2020, feb2020, maart2020, april2020,mei2020, juni2020, juli2020, aug2020, sep2020, okt2020, nov2020, dec2020, jan2021, feb2021, maart2021, april2021 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
text_count = 1

for s in sentence_list:
    if s=="De Telegraaf.nl":
        tele_nl+=1
    elif s=="Trouw":
        trouw+=1
    elif s=="NRC Handelsblad":
        nrc_handel+=1
    elif s=="De Telegraaf":
        tele+=1
    elif s=="de Volkskrant":
        volks+=1
    elif s=="NRC.NEXT":
        nrc += 1
        
    if "januari 2020" in s and len(s)<40:
        jan2020 += 1
    elif "februari 2020" in s and len(s)<40:
        feb2020 += 1
    elif "maart 2020" in s and len(s)<40:
        maart2020 += 1
    elif "april 2020" in s and len(s)<40:
        april2020 += 1
    elif "mei 2020" in s and len(s)<40:
        mei2020 += 1
    elif "juni 2020" in s and len(s)<40:
        juni2020 += 1
    elif "juli 2020" in s and len(s)<40:
        juli2020 += 1
    elif "augustus 2020" in s and len(s)<40:
        aug2020 += 1
    elif "september 2020" in s and len(s)<40:
        sep2020 += 1
    elif "oktober 2020" in s and len(s)<40:
        okt2020 += 1
    elif "november 2020" in s and len(s)<40:
        nov2020 += 1
    elif "december 2020" in s and len(s)<40:
        dec2020 += 1
    elif "januari 2021" in s and len(s)<40:
        jan2021 += 1
    elif "februari 2021" in s and len(s)<40:
        feb2021 += 1
    elif "maart 2021" in s and len(s)<40:
        maart2021 += 1
    elif "april 2021" in s and len(s)<40:
        april2021 += 1
    
    if s=="End of Document":
        text_count += 1
        data_fp.write("\n")
        data_fp.write("Title:")
    else:
        data_fp.write(s+"\n")
        
data_fp.write("\nTotals:\n""De Telegraaf.nl: " + str(tele_nl) + "\n")
data_fp.write("De Telegraaf: " + str(tele) + "\n")
data_fp.write("Trouw: " + str(trouw) + "\n")
data_fp.write("NRC: " + str(nrc) + "\n")
data_fp.write("NRC Handelsblad: " + str(nrc_handel) + "\n")
data_fp.write("De Volkskrant: " + str(volks) + "\n")
data_fp.write("Total: " + str(sum([tele_nl, tele, trouw, nrc, nrc_handel, volks])) + "\n")

data_fp.write("\nJanuari 2020: " + str(jan2020) + "\n")
data_fp.write("Februari 2020: " + str(feb2020) + "\n")
data_fp.write("Maart 2020: " + str(maart2020) + "\n")
data_fp.write("April 2020: " + str(april2020) + "\n")
data_fp.write("Mei 2020: " + str(mei2020) + "\n")
data_fp.write("Juni 2020: " + str(juni2020) + "\n")
data_fp.write("Juli 2020: " + str(juli2020) + "\n")
data_fp.write("Augustus 2020: " + str(aug2020) + "\n")
data_fp.write("September 2020: " + str(sep2020) + "\n")
data_fp.write("Oktober 2020: " + str(okt2020) + "\n")
data_fp.write("November 2020: " + str(nov2020) + "\n")
data_fp.write("December 2020: " + str(dec2020) + "\n")
data_fp.write("Januari 2021: " + str(jan2021) + "\n")
data_fp.write("Februari 2021: " + str(feb2021) + "\n")
data_fp.write("Maart 2021: " + str(maart2021) + "\n")
data_fp.write("April 2021: " + str(april2021) + "\n")
data_fp.write("Total: " + str(sum([jan2020, feb2020, maart2020, april2020, mei2020, juni2020, juli2020, aug2020, sep2020, okt2020, nov2020, dec2020, jan2021, feb2021, maart2021, april2021])) + "\n")
data_fp.write("\nText total: " + str(text_count) + "\n")
data_fp.close()
