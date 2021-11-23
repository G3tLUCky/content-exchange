import matplotlib.pyplot as plt
import numpy as np
import os


def Visual_Display(data, data_slice):
    if len(data_slice) < 7:
        print("Input needs to have a length of at least 7")
        return
    
    all_data = []
    tests = []
    infections = []
    admissions = []
    #all_clinique = []
    #all_ic = []
    deaths = []
    vaccines = []
    dates = []
    
    for d in data_slice:
        test = int(d.find("Testen/Aantal").text)
        tests.append(test)
        infection = int(d.find("Testen/Besmettingen/Aantal").text)
        infections.append(infection)
        admission = int(d.find("Opnames/Aantal").text)
        admissions.append(admission)
        #clinique = int(d.find("Opnames/Kliniek/Aantal").text)
        #all_clinique.append(clinique)
        #ic = int(d.find("Opnames/IC/Aantal").text)
        #all_ic.append(ic)
        death = int(d.find("Doden/Aantal").text)
        deaths.append(death)
        if not data.index(data_slice[0]) < 5:
            vaccine = int(d.find("Vaccinaties/Aantal").text)
            vaccines.append(vaccine)
        
        date = d.find("Datum").text
        dates.append(date.replace("2021-", ""))
    
    all_data.append([tests, 0.2, "Aantal testen"])
    all_data.append([infections, 0.5, "Aantal besmettingen"])
    all_data.append([admissions, 0.4, "Aantal opnames in ziekenhuizen"])
    #all_data.append([all_clinique, 0.1, "Aantal opnames in de kliniek"])
    #all_data.append([all_ic, 0.1, "Aantal IC-opnames"])
    all_data.append([deaths, 0.3, "Aantal doden"])
    if not data.index(data_slice[0]) < 5:
        all_data.append([vaccines, 0.4, "Aantal vaccinaties"])
    
    data = [i for i, j in enumerate(all_data)]
    weights = [i[1] for i in all_data]
    data_normalized = [i/sum(weights) for i in weights]
    numbers = np.random.choice(data, p = data_normalized)    
    
    plt.plot(all_data[numbers][0], color = 'blue', marker = 'o')
    plt.title('Weekoverzicht')
    plt.xticks(range(7), dates)
    plt.ylabel(all_data[numbers][2])
    plt.xlabel("Datum")
    #plt.show()
    plt.savefig("visual_display.png")
