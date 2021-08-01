

def Tests_Yesterday(xml_files, idx):
    if idx < 1:
        return "error"
    percentage_difference = xml_files[idx].find("Testen/Vergelijking/Gisteren").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"

def Tests_Week(xml_files, idx):
    if idx < 7:
        return "error"
    percentage_difference = xml_files[idx].find("Testen/Vergelijking/Week").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"
    
    
def Infections_Yesterday(xml_files, idx):
    if idx < 1:
        return "error"
    percentage_difference = xml_files[idx].find("Testen/Besmettingen/Vergelijking/Gisteren").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"

def Infections_Week(xml_files, idx):
    if idx < 7:
        return "error"
    percentage_difference = xml_files[idx].find("Testen/Besmettingen/Vergelijking/Week").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"
    
    
def Admissions_Yesterday(xml_files, idx):
    if idx < 1:
        return "error"
    percentage_difference = xml_files[idx].find("Opnames/Vergelijking/Gisteren").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"

def Admissions_Week(xml_files, idx):
    if idx < 7:
        return "error"
    percentage_difference = xml_files[idx].find("Opnames/Vergelijking/Week").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"
    
    
def Clinique_Yesterday(xml_files, idx):
    if idx < 1:
        return "error"
    percentage_difference = xml_files[idx].find("Opnames/Kliniek/Vergelijking/Gisteren").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"

def Clinique_Week(xml_files, idx):
    if idx < 7:
        return "error"
    percentage_difference = xml_files[idx].find("Opnames/Kliniek/Vergelijking/Week").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"
    
    
def IC_Yesterday(xml_files, idx):
    if idx < 1:
        return "error"
    percentage_difference = xml_files[idx].find("Opnames/IC/Vergelijking/Gisteren").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"

def IC_Week(xml_files, idx):
    if idx < 7:
        return "error"
    percentage_difference = xml_files[idx].find("Opnames/IC/Vergelijking/Week").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"
    
    
def Deaths_Yesterday(xml_files, idx):
    if idx < 1:
        return "error"
    percentage_difference = xml_files[idx].find("Doden/Vergelijking/Gisteren").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"

def Deaths_Week(xml_files, idx):
    if idx < 7:
        return "error"
    percentage_difference = xml_files[idx].find("Doden/Vergelijking/Week").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"


def Vaccines_Yesterday(xml_files, idx):
    if idx < 6:
        return "error"
    percentage_difference = xml_files[idx].find("Vaccinaties/Vergelijking/Gisteren").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"

def Vaccines_Week(xml_files, idx):
    if idx < 12:
        return "error"
    percentage_difference = xml_files[idx].find("Vaccinaties/Vergelijking/Week").attrib
    percentage_difInt = float(percentage_difference['percentage'].replace("%", ""))
    if percentage_difInt > 5:
        return "increase"
    elif percentage_difInt < -5:
        return "decrease"
    else:
        return "constant"
    


    