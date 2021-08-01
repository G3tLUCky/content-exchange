import Ruleset_module as Ruleset
import random


def Template_Filler(gapped_templates, xml_files, idx):
    filled_templates = []
    temp_types = ['Title', 'Tests', 'Infections', 'Admissions', 'Clinique', 'IC', 'Deaths', 'Vaccines']
    
    zelfs_nw_synonyms = {'Tests': ['testen', 'testen voor corona', 'testen voor Covid', 'dagelijkse coronatesten', 'dagelijkse Covid-testen', 'testen voor het coronavirus'], \
                "Infections":['besmettingen', 'positieve testen', 'coronagevallen', 'coronabesmettingen', 'gevallen van Covid', 'Covid-gevallen',\
                'mensen met Covid', 'mensen met corona', 'positief geteste mensen'], 'Admissions':['opnames in het ziekenhuis', 'ziekenhuisopnames', 'coronapatiënten in ziekenhuizen',\
                'patiënten met Covid in het ziekenhuis', 'mensen met Covid in ziekenhuizen'], 'Clinique':['opnames in de kliniek', 'coronapatiënten in de kliniek', 'patiënten met Covid in de kliniek', 'mensen in de kliniek'], \
                'IC':['opnames op de IC', 'IC-opnames', 'patiënten met Covid op de IC', 'mensen op de IC'], 'Deaths':['sterfgevallen', 'doden', 'coronadoden', 'doden aan Covid', 'sterfgevallen door corona', 'overleden personen'],\
                'Vaccines':['vaccinaties', 'prikken', 'prikken tegen corona', 'gevaccineerde personen']}
    time_synonyms = {'Yesterday': ['gisteren', 'een dag eerder', 'een dag geleden', 'een dag voorheen'], "Week":['het weekgemiddelde', 'het gemiddelde van de week']}
    place_synonyms = {'Admissions':['in de ziekenhuizen', 'in het ziekenhuis', 'in ziekenhuizen', 'in het hospitaal'],\
                      'Clinique':['in de klinieken', 'in de kliniek', 'in klinieken'], \
                          'IC':["op de IC's", "op IC's", 'op de IC', 'op de intensive care']}
    
    #expression = re.compile(r'(<+.*?>)')
    
    if len(gapped_templates) <= 1:
        return "error"
    for t, p in zip(gapped_templates, temp_types):
        if p ==  "Title":
            line = t[0]
            if t[1] == "Tests":
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Testen/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['Tests'])
                    line = line.replace("<zelfs.nw>", name)
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "getest")
                if "<totaal>" in line:
                    total = xml_files[idx].find("Testen/Totaal").text
                    line = line.replace("<totaal>", total)
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Testen/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Testen/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")
                if len(t) > 2:
                    if "<gisteren|het weekgemiddelde>" in line:
                        if t[2] == Ruleset.Tests_Yesterday(xml_files, idx):
                            time = random.choice(time_synonyms['Yesterday'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
                        elif t[2] == Ruleset.Tests_Week(xml_files, idx):
                            time = random.choice(time_synonyms['Week'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time) 
            if t[1] == "Infections":
                if len(t) > 2:
                    if "<GemeenteMax (provincie)|ProvincieMin>" in line and "<aantal>" in line:
                        if t[2] == "increase":
                            amount = xml_files[idx].find("Testen/Besmettingen/GemeenteMax/Aantal").text
                            line = line.replace("<aantal>", amount)
                        else:
                            amount = xml_files[idx].find("Testen/Besmettingen/ProvincieMin/Aantal").text
                            line = line.replace("<aantal>", amount)
                    if "<GemeenteMax (provincie)|ProvincieMin>" in line:
                        if t[2] == "increase":
                            mun = xml_files[idx].find("Testen/Besmettingen/GemeenteMax/Gemeente").text
                            prov = xml_files[idx].find("Testen/Besmettingen/GemeenteMax").attrib['provincie']
                            line = line.replace("<GemeenteMax (provincie)|ProvincieMin>", mun+" ("+prov+")")
                        else:
                            prov = xml_files[idx].find("Testen/Besmettingen/ProvincieMin/Provincie").text
                            line = line.replace("<GemeenteMax (provincie)|ProvincieMin>", prov)
                    if "<hoogste|laagste>" in line:
                        if t[2] == "increase":
                            line = line.replace("<hoogste|laagste>", "hoogste")
                        else:
                            line = line.replace("<hoogste|laagste>", "laagste")
                    if "<hoog|laag>" in line:
                        if t[2] == "increase":
                            line = line.replace("<hoog|laag>", "hoog")
                        else:
                            line = line.replace("<hoog|laag>", "laag")    
                    if "<gisteren|het weekgemiddelde>" in line:
                        if t[2] == Ruleset.Infections_Yesterday(xml_files, idx):
                            time = random.choice(time_synonyms['Yesterday'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
                        elif t[2] == Ruleset.Infections_Week(xml_files, idx):
                            time = random.choice(time_synonyms['Week'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Testen/Besmettingen/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['Infections'])
                    line = line.replace("<zelfs.nw>", name)
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "besmet")
                if "<totaal>" in line:
                    total = xml_files[idx].find("Testen/Besmettingen/Totaal").text
                    line = line.replace("<totaal>", total)
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Testen/Besmettingen/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Testen/Besmettingen/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")
            if t[1] == "Admissions":
                if len(t) > 2:
                    if "<GemeenteMax (provincie)|ProvincieMin>" in line and "<aantal>" in line:
                        if t[2] == "increase":
                            amount = xml_files[idx].find("Opnames/GemeenteMax/Aantal").text
                            line = line.replace("<aantal>", amount)
                        else:
                            amount = xml_files[idx].find("Opnames/ProvincieMin/Aantal").text
                            line = line.replace("<aantal>", amount) 
                    if "<GemeenteMax (provincie)|ProvincieMin>" in line:
                        if t[2] == "increase":
                            mun = xml_files[idx].find("Opnames/GemeenteMax/Gemeente").text
                            prov = xml_files[idx].find("Opnames/GemeenteMax").attrib['provincie']
                            line = line.replace("<GemeenteMax (provincie)|ProvincieMin>", mun+" ("+prov+")")
                        else:
                            prov = xml_files[idx].find("Opnames/ProvincieMin/Provincie").text
                            line = line.replace("<GemeenteMax (provincie)|ProvincieMin>", prov)
                    if "<hoogste|laagste>" in line:
                        if t[2] == "increase":
                            line = line.replace("<hoogste|laagste>", "hoogste")
                        else:
                            line = line.replace("<hoogste|laagste>", "laagste")
                    if "<hoog|laag>" in line:
                        if t[2] == "increase":
                            line = line.replace("<hoog|laag>", "hoog")
                        else:
                            line = line.replace("<hoog|laag>", "laag") 
                    if "<gisteren|het weekgemiddelde>" in line:
                        if t[2] == Ruleset.Admissions_Yesterday(xml_files, idx):
                            time = random.choice(time_synonyms['Yesterday'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
                        elif t[2] == Ruleset.Admissions_Week(xml_files, idx):
                            time = random.choice(time_synonyms['Week'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Opnames/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['Admissions'])
                    line = line.replace("<zelfs.nw>", name)
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "opgenomen in het ziekenhuis")
                if "<totaal>" in line:
                    total = xml_files[idx].find("Opnames/TotaalAlgemeen").text
                    line = line.replace("<totaal>", total)
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Opnames/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Opnames/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")
            if t[1] == "Clinique":
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Opnames/Kliniek/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['Clinique'])
                    line = line.replace("<zelfs.nw>", name)
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "opgenomen in de kliniek")
                if "<totaal>" in line:
                    total = xml_files[idx].find("Opnames/Kliniek/TotaalAlgemeen").text
                    line = line.replace("<totaal>", total)
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Opnames/Kliniek/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Opnames/Kliniek/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")
                if len(t) > 2:
                    if "<gisteren|het weekgemiddelde>" in line:
                        if t[2] == Ruleset.Clinique_Yesterday(xml_files, idx):
                            time = random.choice(time_synonyms['Yesterday'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
                        elif t[2] == Ruleset.Clinique_Week(xml_files, idx):
                            time = random.choice(time_synonyms['Week'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
            if t[1] == "IC":
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Opnames/IC/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['IC'])
                    line = line.replace("<zelfs.nw>", name)
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "opgenomen op de IC")
                if "<totaal>" in line:
                    total = xml_files[idx].find("Opnames/IC/TotaalAlgemeen").text
                    line = line.replace("<totaal>", total)  
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Opnames/IC/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Opnames/IC/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")
                if len(t) > 2:
                    if "<gisteren|het weekgemiddelde>" in line:
                        if t[2] == Ruleset.IC_Yesterday(xml_files, idx):
                            time = random.choice(time_synonyms['Yesterday'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
                        elif t[2] == Ruleset.IC_Week(xml_files, idx):
                            time = random.choice(time_synonyms['Week'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
            if t[1] == "Deaths":
                if len(t) > 2:
                    if "<GemeenteMax (provincie)|ProvincieMin>" in line and "<aantal>" in line:
                        if t[2] == "increase":
                            amount = xml_files[idx].find("Doden/GemeenteMax/Aantal").text
                            line = line.replace("<aantal>", amount)
                        else:
                            amount = xml_files[idx].find("Doden/ProvincieMin/Aantal").text
                            line = line.replace("<aantal>", amount) 
                    if "<GemeenteMax (provincie)|ProvincieMin>" in line:
                        if t[2] == "increase":
                            mun = xml_files[idx].find("Doden/GemeenteMax/Gemeente").text
                            prov = xml_files[idx].find("Doden/GemeenteMax").attrib['provincie']
                            line = line.replace("<GemeenteMax (provincie)|ProvincieMin>", mun+" ("+prov+")")
                        else:
                            prov = xml_files[idx].find("Doden/ProvincieMin/Provincie").text
                            line = line.replace("<GemeenteMax (provincie)|ProvincieMin>", prov)
                    if "<hoogste|laagste>" in line:
                        if t[2] == "increase":
                            line = line.replace("<hoogste|laagste>", "hoogste")
                        else:
                            line = line.replace("<hoogste|laagste>", "laagste")
                    if "<hoog|laag>" in line:
                        if t[2] == "increase":
                            line = line.replace("<hoog|laag>", "hoog")
                        else:
                            line = line.replace("<hoog|laag>", "laag") 
                    if "<gisteren|het weekgemiddelde>" in line:
                        if t[2] == Ruleset.Deaths_Yesterday(xml_files, idx):
                            time = random.choice(time_synonyms['Yesterday'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
                        elif t[2] == Ruleset.Deaths_Week(xml_files, idx):
                            time = random.choice(time_synonyms['Week'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Doden/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['Deaths'])
                    line = line.replace("<zelfs.nw>", name)
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "overleden")
                if "<totaal>" in line:
                    total = xml_files[idx].find("Doden/Totaal").text
                    line = line.replace("<totaal>", total)
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Doden/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Doden/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")
            if t[1] == "Vaccines":
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Vaccinaties/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['Vaccines'])
                    line = line.replace("<zelfs.nw>", name)
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "gevaccineerd")
                if "<totaal>" in line:
                    total = xml_files[idx].find("Vaccinaties/Totaal").text
                    line = line.replace("<totaal>", total)  
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Vaccinaties/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Vaccinaties/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")
                if len(t) > 2:
                    if "<gisteren|het weekgemiddelde>" in line:
                        if t[2] == Ruleset.Vaccines_Yesterday(xml_files, idx):
                            time = random.choice(time_synonyms['Yesterday'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
                        elif t[2] == Ruleset.Vaccines_Week(xml_files, idx):
                            time = random.choice(time_synonyms['Week'])
                            line = line.replace("<gisteren|het weekgemiddelde>", time)
            filled_templates.append(line)
            filled_templates.append("\n")
                    
        if p == "Tests":
            for line in t[0]:
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['Tests'])
                    line = line.replace("<zelfs.nw>", name)
                if "<zelfs.nw+voorz>" in line:
                    line = line.replace("<zelfs.nw+voorz>", "testen voor")
                if "<bijv.nw>" in line:
                    line = line.replace("<bijv.nw>", "geteste")
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "getest")
                if "<volt.deelw+voorz>" in line:
                    line = line.replace("<volt.deelw+voorz>", "getest op")
                if "<ww+volt.deelw>" in line:
                    line = line.replace("<ww+volt.deelw>", "is getest")
                if "<ww+volt.deelw+voorz>" in line:
                    line = line.replace("<ww+volt.deelw+voorz>", "is getest op")
                if "<ww_mv+volt.deelw>" in line:
                    line = line.replace("<ww_mv+volt.deelw>", "getest zijn")
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Testen/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<aantal-vergelijkingGisteren>" in line: 
                    amount_yesterday = xml_files[idx-1].find("Testen/Aantal").text 
                    line = line.replace("<aantal-vergelijkingGisteren>", amount_yesterday)
                if "<vergelijkingGisteren|week|percentage>" in line:
                    if t[1] == Ruleset.Tests_Yesterday(xml_files, idx):
                        amount_diff = xml_files[idx].find("Testen/Vergelijking/Gisteren").text
                        amount_perc = xml_files[idx].find("Testen/Vergelijking/Gisteren").attrib['percentage']
                    elif t[1] == Ruleset.Tests_Week(xml_files, idx):
                        amount_diff = xml_files[idx].find("Testen/Vergelijking/Week").text
                        amount_perc = xml_files[idx].find("Testen/Vergelijking/Week").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|week|percentage>", amount_diff+" ("+amount_perc+")")
                if "<gisteren|het weekgemiddelde>" in line:
                    if t[1] == Ruleset.Tests_Yesterday(xml_files, idx):
                        time = random.choice(time_synonyms['Yesterday'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                    elif t[1] == Ruleset.Tests_Week(xml_files, idx):
                        time = random.choice(time_synonyms['Week'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Testen/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Testen/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")                    
                if "<totaal>" in line:
                    total = xml_files[idx].find("Testen/Totaal").text
                    line = line.replace("<totaal>", total)
                filled_templates.append(line)
            filled_templates.append("\n")
                
        if p == "Infections":
            for line in t[0]:
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['Infections'])
                    line = line.replace("<zelfs.nw>", name)
                if "<zelfs.nw+voorz>" in line:
                    line = line.replace("<zelfs.nw+voorz>", "besmettingen door")
                if "<bijv.nw>" in line:
                    line = line.replace("<bijv.nw>", "besmette")
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "besmet")
                if "<volt.deelw+voorz>" in line:
                    line = line.replace("<volt.deelw+voorz>", "positief getest op")
                if "<ww+volt.deelw>" in line:
                    line = line.replace("<ww+volt.deelw>", "is besmet")
                if "<ww+volt.deelw+voorz>" in line:
                    line = line.replace("<ww+volt.deelw+voorz>", "is besmet met")
                if "<ww_mv+volt.deelw>" in line:
                    line = line.replace("<ww_mv+volt.deelw>", "besmet zijn")
                if "<GemeenteMax (provincie)|ProvincieMin>" in line and "<aantal>" in line:
                    if t[1] == "increase":
                        amount = xml_files[idx].find("Testen/Besmettingen/GemeenteMax/Aantal").text
                        line = line.replace("<aantal>", amount)
                    else:
                        amount = xml_files[idx].find("Testen/Besmettingen/ProvincieMin/Aantal").text
                        line = line.replace("<aantal>", amount)  
                if "<GemeenteMax (provincie)>" in line and "<aantal>" in line:
                    amount = xml_files[idx].find("Testen/Besmettingen/GemeenteMax/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Testen/Besmettingen/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<aantal-vergelijkingGisteren>" in line: 
                    amount_yesterday = xml_files[idx-1].find("Testen/Besmettingen/Aantal").text 
                    line = line.replace("<aantal-vergelijkingGisteren>", amount_yesterday)
                if "<vergelijkingGisteren|week|percentage>" in line:
                    if t[1] == Ruleset.Infections_Yesterday(xml_files, idx):
                        amount_diff = xml_files[idx].find("Testen/Besmettingen/Vergelijking/Gisteren").text
                        amount_perc = xml_files[idx].find("Testen/Besmettingen/Vergelijking/Gisteren").attrib['percentage']
                    elif t[1] == Ruleset.Infections_Week(xml_files, idx):
                        amount_diff = xml_files[idx].find("Testen/Besmettingen/Vergelijking/Week").text
                        amount_perc = xml_files[idx].find("Testen/Besmettingen/Vergelijking/Week").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|week|percentage>", amount_diff+" ("+amount_perc+")")
                if "<gisteren|het weekgemiddelde>" in line:
                    if t[1] == Ruleset.Infections_Yesterday(xml_files, idx):
                        time = random.choice(time_synonyms['Yesterday'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                    elif t[1] == Ruleset.Infections_Week(xml_files, idx):
                        time = random.choice(time_synonyms['Week'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Testen/Besmettingen/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Testen/Besmettingen/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")                    
                if "<GemeenteMax (provincie)|ProvincieMin>" in line:
                    if t[1] == "increase":
                        mun = xml_files[idx].find("Testen/Besmettingen/GemeenteMax/Gemeente").text
                        prov = xml_files[idx].find("Testen/Besmettingen/GemeenteMax").attrib['provincie']
                        line = line.replace("<GemeenteMax (provincie)|ProvincieMin>", mun+" ("+prov+")")
                    else:
                        prov = xml_files[idx].find("Testen/Besmettingen/ProvincieMin/Provincie").text
                        line = line.replace("<GemeenteMax (provincie)|ProvincieMin>", prov)
                if "<GemeenteMax (provincie)>" in line:
                   mun = xml_files[idx].find("Testen/Besmettingen/GemeenteMax/Gemeente").text
                   line = line.replace("<GemeenteMax (provincie)>", mun)
                if "<hoogst|laagst>" in line:
                    if t[1] == "increase":
                        line = line.replace("<hoogst|laagst>", "hoogst")
                    else:
                        line = line.replace("<hoogst|laagst>", "laagst")
                if "<zwaarst|minst zwaar>" in line:
                    if t[1] == "increase":
                        line = line.replace("<zwaarst|minst zwaar>", "zwaarst")
                    else:
                        line = line.replace("<zwaarst|minst zwaar>", "minst zwaar")     
                if "<meeste|minste>" in line:
                    if t[1] == "increase":
                        line = line.replace("<meeste|minste>", "meeste")
                    else:
                        line = line.replace("<meeste|minste>", "minste")
                if "<gemeente|provincie>" in line:
                    if t[1] == "increase":
                        line = line.replace("<gemeente|provincie>", "gemeente")
                    else:
                        line = line.replace("<gemeente|provincie>", "provincie")
                if "<gemeenten|provincies>" in line:
                    if t[1] == "increase":
                        line = line.replace("<gemeenten|provincies>", "gemeenten")
                    else:
                        line = line.replace("<gemeenten|provincies>", "provincies")
                if "<hoger|lager>" in line:
                    if t[1] == "increase":
                        line = line.replace("<hoger|lager>", "hoger")
                    else:
                        line = line.replace("<hoger|lager>", "lager")
                if "<totaal>" in line:
                    total = xml_files[idx].find("Testen/Besmettingen/Totaal").text
                    line = line.replace("<totaal>", total)
                filled_templates.append(line)
            filled_templates.append("\n")
                
        if p == "Admissions":
            for line in t[0]:
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['Admissions'])
                    line = line.replace("<zelfs.nw>", name)
                if "<zelfs.nw+voorz>" in line:
                    line = line.replace("<zelfs.nw+voorz>", "opnames in het ziekenhuis met")
                if "<bijv.nw>" in line:
                    line = line.replace("<bijv.nw>", "opgenomen")
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "opgenomen in het ziekenhuis")
                if "<volt.deelw+voorz>" in line:
                    line = line.replace("<volt.deelw+voorz>", "opgenomen in het ziekenhuis met")
                if "<ww+volt.deelw>" in line:
                    line = line.replace("<ww+volt.deelw>", "is opgenomen in het ziekenhuis")
                if "<ww+volt.deelw+voorz>" in line:
                    line = line.replace("<ww+volt.deelw+voorz>", "is opgenomen in het ziekenhuis met")
                if "<ww_mv+volt.deelw>" in line:
                    line = line.replace("<ww_mv+volt.deelw>", "in het ziekenhuis zijn opgenomen")
                if "<GemeenteMax (provincie)|ProvincieMin>" in line and "<aantal>" in line:
                    if t[1] == "increase":
                        amount = xml_files[idx].find("Opnames/GemeenteMax/Aantal").text
                        line = line.replace("<aantal>", amount)
                    else:
                        amount = xml_files[idx].find("Opnames/ProvincieMin/Aantal").text
                        line = line.replace("<aantal>", amount)  
                if "<GemeenteMax (provincie)>" in line and "<aantal>" in line:
                    amount = xml_files[idx].find("Opnames/GemeenteMax/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Opnames/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<aantal-vergelijkingGisteren>" in line: 
                    amount_yesterday = xml_files[idx-1].find("Opnames/Aantal").text 
                    line = line.replace("<aantal-vergelijkingGisteren>", amount_yesterday)
                if "<vergelijkingGisteren|week|percentage>" in line:
                    if t[1] == Ruleset.Admissions_Yesterday(xml_files, idx):
                        amount_diff = xml_files[idx].find("Opnames/Vergelijking/Gisteren").text
                        amount_perc = xml_files[idx].find("Opnames/Vergelijking/Gisteren").attrib['percentage']
                    elif t[1] == Ruleset.Admissions_Week(xml_files, idx):
                        amount_diff = xml_files[idx].find("Opnames/Vergelijking/Week").text
                        amount_perc = xml_files[idx].find("Opnames/Vergelijking/Week").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|week|percentage>", amount_diff+" ("+amount_perc+")")
                if "<gisteren|het weekgemiddelde>" in line:
                    if t[1] == Ruleset.Admissions_Yesterday(xml_files, idx):
                        time = random.choice(time_synonyms['Yesterday'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                    elif t[1] == Ruleset.Admissions_Week(xml_files, idx):
                        time = random.choice(time_synonyms['Week'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Opnames/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Opnames/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")                    
                if "<GemeenteMax (provincie)|ProvincieMin>" in line:
                    if t[1] == "increase":
                        mun = xml_files[idx].find("Opnames/GemeenteMax/Gemeente").text
                        prov = xml_files[idx].find("Opnames/GemeenteMax").attrib['provincie']
                        line = line.replace("<GemeenteMax (provincie)|ProvincieMin>", mun+" ("+prov+")")
                    else:
                        prov = xml_files[idx].find("Opnames/ProvincieMin/Provincie").text
                        line = line.replace("<GemeenteMax (provincie)|ProvincieMin>", prov)
                if "<GemeenteMax (provincie)>" in line:
                   mun = xml_files[idx].find("Opnames/GemeenteMax/Gemeente").text
                   line = line.replace("<GemeenteMax (provincie)>", mun)
                if "<hoogst|laagst>" in line:
                    if t[1] == "increase":
                        line = line.replace("<hoogst|laagst>", "hoogst")
                    else:
                        line = line.replace("<hoogst|laagst>", "laagst")
                if "<zwaarst|minst zwaar>" in line:
                    if t[1] == "increase":
                        line = line.replace("<zwaarst|minst zwaar>", "zwaarst")
                    else:
                        line = line.replace("<zwaarst|minst zwaar>", "minst zwaar")     
                if "<meeste|minste>" in line:
                    if t[1] == "increase":
                        line = line.replace("<meeste|minste>", "meeste")
                    else:
                        line = line.replace("<meeste|minste>", "minste")
                if "<gemeente|provincie>" in line:
                    if t[1] == "increase":
                        line = line.replace("<gemeente|provincie>", "gemeente")
                    else:
                        line = line.replace("<gemeente|provincie>", "provincie")
                if "<gemeenten|provincies>" in line:
                    if t[1] == "increase":
                        line = line.replace("<gemeenten|provincies>", "gemeenten")
                    else:
                        line = line.replace("<gemeenten|provincies>", "provincies")
                if "<hoger|lager>" in line:
                    if t[1] == "increase":
                        line = line.replace("<hoger|lager>", "hoger")
                    else:
                        line = line.replace("<hoger|lager>", "lager")
                if "<plaats>" in line:
                    place = random.choice(place_synonyms['Admissions'])
                    line = line.replace("<plaats>", place)
                if "<totaalAlgemeen>" in line:
                    total = xml_files[idx].find("Opnames/TotaalAlgemeen").text
                    line = line.replace("<totaalAlgemeen>", total)
                if "<totaal>" in line:
                    total = xml_files[idx].find("Opnames/TotaalMomenteel").text
                    line = line.replace("<totaal>", total)
                filled_templates.append(line)
                
        if p == "Clinique":
            for line in t[0]:
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['Clinique'])
                    line = line.replace("<zelfs.nw>", name)
                if "<zelfs.nw+voorz>" in line:
                    line = line.replace("<zelfs.nw+voorz>", "opnames in de kliniek met")
                if "<bijv.nw>" in line:
                    line = line.replace("<bijv.nw>", "in de kliniek opgenomen")
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "opgenomen in de kliniek")
                if "<volt.deelw+voorz>" in line:
                    line = line.replace("<volt.deelw+voorz>", "opgenomen in de kliniek met")
                if "<ww+volt.deelw>" in line:
                    line = line.replace("<ww+volt.deelw>", "is opgenomen in de kliniek")
                if "<ww+volt.deelw+voorz>" in line:
                    line = line.replace("<ww+volt.deelw+voorz>", "is opgenomen in de kliniek met")
                if "<ww_mv+volt.deelw>" in line:
                    line = line.replace("<ww_mv+volt.deelw>", "in de kliniek zijn opgenomen")
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Opnames/Kliniek/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<aantal-vergelijkingGisteren>" in line: 
                    amount_yesterday = xml_files[idx-1].find("Opnames/Kliniek/Aantal").text 
                    line = line.replace("<aantal-vergelijkingGisteren>", amount_yesterday)
                if "<vergelijkingGisteren|week|percentage>" in line:
                    if t[1] == Ruleset.Clinique_Yesterday(xml_files, idx):
                        amount_diff = xml_files[idx].find("Opnames/Kliniek/Vergelijking/Gisteren").text
                        amount_perc = xml_files[idx].find("Opnames/Kliniek/Vergelijking/Gisteren").attrib['percentage']
                    elif t[1] == Ruleset.Clinique_Week(xml_files, idx):
                        amount_diff = xml_files[idx].find("Opnames/Kliniek/Vergelijking/Week").text
                        amount_perc = xml_files[idx].find("Opnames/Kliniek/Vergelijking/Week").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|week|percentage>", amount_diff+" ("+amount_perc+")")
                if "<gisteren|het weekgemiddelde>" in line:
                    if t[1] == Ruleset.Clinique_Yesterday(xml_files, idx):
                        time = random.choice(time_synonyms['Yesterday'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                    elif t[1] == Ruleset.Clinique_Week(xml_files, idx):
                        time = random.choice(time_synonyms['Week'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Opnames/Kliniek/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Opnames/Kliniek/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")                    
                if "<plaats>" in line:
                    place = random.choice(place_synonyms['Clinique'])
                    line = line.replace("<plaats>", place)
                if "<totaalAlgemeen>" in line:
                    total = xml_files[idx].find("Opnames/Kliniek/TotaalAlgemeen").text
                    line = line.replace("<totaalAlgemeen>", total)
                if "<totaal>" in line:
                    total = xml_files[idx].find("Opnames/Kliniek/TotaalMomenteel").text
                    line = line.replace("<totaal>", total)
                filled_templates.append(line)
                
        if p == "IC":
            for line in t[0]:
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['IC'])
                    line = line.replace("<zelfs.nw>", name)
                if "<zelfs.nw+voorz>" in line:
                    line = line.replace("<zelfs.nw+voorz>", "opnames op de IC met")
                if "<bijv.nw>" in line:
                    line = line.replace("<bijv.nw>", "op de IC opgenomen")
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "opgenomen op de IC")
                if "<volt.deelw+voorz>" in line:
                    line = line.replace("<volt.deelw+voorz>", "opgenomen op de IC met")
                if "<ww+volt.deelw>" in line:
                    line = line.replace("<ww+volt.deelw>", "is opgenomen op de IC")
                if "<ww+volt.deelw+voorz>" in line:
                    line = line.replace("<ww+volt.deelw+voorz>", "is opgenomen op de IC met")
                if "<ww_mv+volt.deelw>" in line:
                    line = line.replace("<ww_mv+volt.deelw>", "op de IC zijn opgenomen")
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Opnames/IC/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<aantal-vergelijkingGisteren>" in line: 
                    amount_yesterday = xml_files[idx-1].find("Opnames/IC/Aantal").text 
                    line = line.replace("<aantal-vergelijkingGisteren>", amount_yesterday)
                if "<vergelijkingGisteren|week|percentage>" in line:
                    if t[1] == Ruleset.IC_Yesterday(xml_files, idx):
                        amount_diff = xml_files[idx].find("Opnames/IC/Vergelijking/Gisteren").text
                        amount_perc = xml_files[idx].find("Opnames/IC/Vergelijking/Gisteren").attrib['percentage']
                    elif t[1] == Ruleset.IC_Week(xml_files, idx):
                        amount_diff = xml_files[idx].find("Opnames/IC/Vergelijking/Week").text
                        amount_perc = xml_files[idx].find("Opnames/IC/Vergelijking/Week").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|week|percentage>", amount_diff+" ("+amount_perc+")")
                if "<gisteren|het weekgemiddelde>" in line:
                    if t[1] == Ruleset.IC_Yesterday(xml_files, idx):
                        time = random.choice(time_synonyms['Yesterday'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                    elif t[1] == Ruleset.IC_Week(xml_files, idx):
                        time = random.choice(time_synonyms['Week'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Opnames/IC/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Opnames/IC/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")                    
                if "<plaats>" in line:
                    place = random.choice(place_synonyms['IC'])
                    line = line.replace("<plaats>", place)
                if "<totaalAlgemeen>" in line:
                    total = xml_files[idx].find("Opnames/IC/TotaalAlgemeen").text
                    line = line.replace("<totaalAlgemeen>", total)
                if "<totaal>" in line:
                    total = xml_files[idx].find("Opnames/IC/TotaalMomenteel").text
                    line = line.replace("<totaal>", total)
                filled_templates.append(line)
            filled_templates.append('\n')
                
        if p == "Deaths":
            for line in t[0]:
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['Deaths'])
                    line = line.replace("<zelfs.nw>", name)
                if "<zelfs.nw+voorz>" in line:
                    line = line.replace("<zelfs.nw+voorz>", "doden door")
                if "<bijv.nw>" in line:
                    line = line.replace("<bijv.nw>", "overleden")
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "overleden")
                if "<volt.deelw+voorz>" in line:
                    line = line.replace("<volt.deelw+voorz>", "gestorven aan")
                if "<ww+volt.deelw>" in line:
                    line = line.replace("<ww+volt.deelw>", "is overleden")
                if "<ww+volt.deelw+voorz>" in line:
                    line = line.replace("<ww+volt.deelw+voorz>", "is overleden aan")
                if "<ww_mv+volt.deelw>" in line:
                    line = line.replace("<ww_mv+volt.deelw>", "zijn overleden")
                if "<GemeenteMax (provincie)|ProvincieMin>" in line and "<aantal>" in line:
                    if t[1] == "increase":
                        amount = xml_files[idx].find("Doden/GemeenteMax/Aantal").text
                        line = line.replace("<aantal>", amount)
                    else:
                        amount = xml_files[idx].find("Doden/ProvincieMin/Aantal").text
                        line = line.replace("<aantal>", amount)  
                if "<GemeenteMax (provincie)>" in line and "<aantal>" in line:
                    amount = xml_files[idx].find("Doden/GemeenteMax/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Doden/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<aantal-vergelijkingGisteren>" in line: 
                    amount_yesterday = xml_files[idx-1].find("Doden/Aantal").text 
                    line = line.replace("<aantal-vergelijkingGisteren>", amount_yesterday)
                if "<vergelijkingGisteren|week|percentage>" in line:
                    if t[1] == Ruleset.Deaths_Yesterday(xml_files, idx):
                        amount_diff = xml_files[idx].find("Doden/Vergelijking/Gisteren").text
                        amount_perc = xml_files[idx].find("Doden/Vergelijking/Gisteren").attrib['percentage']
                    elif t[1] == Ruleset.Deaths_Week(xml_files, idx):
                        amount_diff = xml_files[idx].find("Doden/Vergelijking/Week").text
                        amount_perc = xml_files[idx].find("Doden/Vergelijking/Week").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|week|percentage>", amount_diff+" ("+amount_perc+")")
                if "<gisteren|het weekgemiddelde>" in line:
                    if t[1] == Ruleset.Deaths_Yesterday(xml_files, idx):
                        time = random.choice(time_synonyms['Yesterday'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                    elif t[1] == Ruleset.Deaths_Week(xml_files, idx):
                        time = random.choice(time_synonyms['Week'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Doden/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Doden/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")                    
                if "<GemeenteMax (provincie)|ProvincieMin>" in line:
                    if t[1] == "increase":
                        mun = xml_files[idx].find("Doden/GemeenteMax/Gemeente").text
                        prov = xml_files[idx].find("Doden/GemeenteMax").attrib['provincie']
                        line = line.replace("<GemeenteMax (provincie)|ProvincieMin>", mun+" ("+prov+")")
                    else:
                        prov = xml_files[idx].find("Doden/ProvincieMin/Provincie").text
                        line = line.replace("<GemeenteMax (provincie)|ProvincieMin>", prov)
                if "<GemeenteMax (provincie)>" in line:
                   mun = xml_files[idx].find("Doden/GemeenteMax/Gemeente").text
                   line = line.replace("<GemeenteMax (provincie)>", mun)
                if "<hoogst|laagst>" in line:
                    if t[1] == "increase":
                        line = line.replace("<hoogst|laagst>", "hoogst")
                    else:
                        line = line.replace("<hoogst|laagst>", "laagst")
                if "<hoogste|laagste>" in line:
                    if t[1] == "increase":
                        line = line.replace("<hoogste|laagste>", "hoogste")
                    else:
                        line = line.replace("<hoogste|laagste>", "laagste")
                if "<zwaarst|minst zwaar>" in line:
                    if t[1] == "increase":
                        line = line.replace("<zwaarst|minst zwaar>", "zwaarst")
                    else:
                        line = line.replace("<zwaarst|minst zwaar>", "minst zwaar")     
                if "<meeste|minste>" in line:
                    if t[1] == "increase":
                        line = line.replace("<meeste|minste>", "meeste")
                    else:
                        line = line.replace("<meeste|minste>", "minste")
                if "<gemeente|provincie>" in line:
                    if t[1] == "increase":
                        line = line.replace("<gemeente|provincie>", "gemeente")
                    else:
                        line = line.replace("<gemeente|provincie>", "provincie")
                if "<gemeenten|provincies>" in line:
                    if t[1] == "increase":
                        line = line.replace("<gemeenten|provincies>", "gemeenten")
                    else:
                        line = line.replace("<gemeenten|provincies>", "provincies")
                if "<hoger|lager>" in line:
                    if t[1] == "increase":
                        line = line.replace("<hoger|lager>", "hoger")
                    else:
                        line = line.replace("<hoger|lager>", "lager")
                if "<totaal>" in line:
                    total = xml_files[idx].find("Doden/Totaal").text
                    line = line.replace("<totaal>", total)
                filled_templates.append(line)
            filled_templates.append("\n")
                
        if p == "Vaccines":
            for line in t[0]:
                if "<zelfs.nw>" in line:
                    name = random.choice(zelfs_nw_synonyms['Vaccines'])
                    line = line.replace("<zelfs.nw>", name)
                if "<zelfs.nw+voorz>" in line:
                    line = line.replace("<zelfs.nw+voorz>", "vaccinaties tegen")
                if "<bijv.nw>" in line:
                    line = line.replace("<bijv.nw>", "gevaccineerde")
                if "<volt.deelw>" in line:
                    line = line.replace("<volt.deelw>", "gevaccineerd")
                if "<volt.deelw+voorz>" in line:
                    line = line.replace("<volt.deelw+voorz>", "gevaccineerd tegen")
                if "<ww+volt.deelw>" in line:
                    line = line.replace("<ww+volt.deelw>", "is gevaccineerd")
                if "<ww+volt.deelw+voorz>" in line:
                    line = line.replace("<ww+volt.deelw+voorz>", "is gevaccineerd tegen")
                if "<ww_mv+volt.deelw>" in line:
                    line = line.replace("<ww_mv+volt.deelw>", "zijn gevaccineerd")
                if "<aantal>" in line:
                    amount = xml_files[idx].find("Vaccinaties/Aantal").text
                    line = line.replace("<aantal>", amount)
                if "<aantal-vergelijkingGisteren>" in line: 
                    amount_yesterday = xml_files[idx-1].find("Vaccinaties/Aantal").text 
                    line = line.replace("<aantal-vergelijkingGisteren>", amount_yesterday)
                if "<vergelijkingGisteren|week|percentage>" in line:
                    if t[1] == Ruleset.Vaccines_Yesterday(xml_files, idx):
                        amount_diff = xml_files[idx].find("Vaccinaties/Vergelijking/Gisteren").text
                        amount_perc = xml_files[idx].find("Vaccinaties/Vergelijking/Gisteren").attrib['percentage']
                    elif t[1] == Ruleset.Vaccines_Week(xml_files, idx):
                        amount_diff = xml_files[idx].find("Vaccinaties/Vergelijking/Week").text
                        amount_perc = xml_files[idx].find("Vaccinaties/Vergelijking/Week").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|week|percentage>", amount_diff+" ("+amount_perc+")")
                if "<gisteren|het weekgemiddelde>" in line:
                    if t[1] == Ruleset.Vaccines_Yesterday(xml_files, idx):
                        time = random.choice(time_synonyms['Yesterday'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                    elif t[1] == Ruleset.Vaccines_Week(xml_files, idx):
                        time = random.choice(time_synonyms['Week'])
                        line = line.replace("<gisteren|het weekgemiddelde>", time)
                if "<vergelijkingGisteren|percentage>" in line:
                    amount_diff = xml_files[idx].find("Vaccinaties/Vergelijking/Gisteren").text
                    amount_perc = xml_files[idx].find("Vaccinaties/Vergelijking/Gisteren").attrib['percentage']
                    if "-" in amount_diff or "-" in amount_perc:
                        amount_diff = amount_diff.replace("-", "")
                        amount_perc = amount_perc.replace("-", "")
                    line = line.replace("<vergelijkingGisteren|percentage>", amount_diff+" ("+amount_perc+")")                    
                if "<totaal>" in line:
                    total = xml_files[idx].find("Vaccinaties/Totaal").text
                    line = line.replace("<totaal>", total)
                filled_templates.append(line)
            filled_templates.append("\n")
                
    return filled_templates
                

#zelfs.nw = <testen|besmettingen|opnames|kliniek|IC|doden|vaccinaties>
#zelfs.nw+voorz = <testen voor|besmettingen door|opnames met|kliniek met|IC met|doden door|vaccinaties tegen>
#ww+volt.deelw+voorz = <is getest op|dat positief is getest op|is opgenomen in ziekenhuizen met|is opgenomen in klinieken met|is opgenomen op IC's met|is overleden aan|is gevaccineerd tegen>
#ww+volt.deelw = <is getest|is besmet|is opgenomen in het ziekenhuis|is opgenomen in de kliniek|is opgenomen op de IC|is overleden|is gevaccineerd>
#plaats = <in de ziekenhuizen|in de klinieken|op de IC's>
#bijv.nw = <geteste|besmette|opgenomen|overleden|gevaccineerde>
#volt.deelw+voorz = <getest op|positief getest op|opgenomen in het ziekenhuis met|opgenomen in de kliniek met|opgenomen op de IC met|gestorven aan|gevaccineerd tegen>
#ww_mv+volt.deelw = <gestest zijn|positief getest zijn|in het ziekenhuis zijn opgenomen|in de kliniek zijn opgenomen|op de IC zijn opgenomen|zijn overleden|zijn gevaccineerd>
#volt.deelw = <getest|besmet|opgenomen in het ziekenhuis|opgenomen in de kliniek|opgenomen op de IC|overleden|gevaccineerd>



