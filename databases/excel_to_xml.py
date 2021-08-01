import pandas as pd
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as xml_minidom

os.chdir("C:/Users/lucla/Documents/Studie/Tilburg University/Masterscriptie/databases/Cijfers")

df = pd.read_excel("all_data.xlsx")
row = 0
tot_testen_number = 6254298
tot_besmet_number = 795644
tot_doden_number = 11400
tot_vac_number = 0
tot_clin_number = 35129
tot_ic_number = 6579
tot_hos_number = tot_clin_number + tot_ic_number

os.chdir("C:/Users/lucla/Documents/Studie/Tilburg University/Masterscriptie/databases/Cijfers/XML_files")
for x in df['Date']:
    x = str(x).replace(" 00:00:00", "")
    filename = "COVID_"+x.replace("-","_")+".xml"
    
    
    root = ET.Element("Covid")
    datum = ET.SubElement(root, 'Datum')
    datum.text = x
    
    
    testen = ET.SubElement(root, 'Testen')
    aantal_testen = ET.SubElement(testen, 'Aantal')
    aantal_testen.text = str(df['Tested'][row])
    tot_testen_number += df['Tested'][row]
    totaal_testen = ET.SubElement(testen, 'Totaal')
    totaal_testen.text = str(tot_testen_number)
    
    vergelijking_testen = ET.SubElement(testen, 'Vergelijking')
    verg_gisteren_testen = ET.SubElement(vergelijking_testen, 'Gisteren')
    if row > 0:
        verg_gisteren_testen.text = str(df['Tested'][row]-df['Tested'][row-1])
        verg_gisteren_testen.set('percentage', str(round(((df['Tested'][row]-df['Tested'][row-1])/df['Tested'][row-1])*100, 1))+"%")
    verg_week_testen = ET.SubElement(vergelijking_testen, 'Week')
    if row > 6:
        week_average = round(sum(df['Tested'][row-7:row-1])/7)
        verg_week_testen.text = str(week_average-df['Tested'][row])
        verg_week_testen.set('percentage', str(round(((week_average-df['Tested'][row])/week_average)*100, 1))+"%")
    
    
    besmettingen = ET.SubElement(testen, 'Besmettingen')
    aantal_besmettingen = ET.SubElement(besmettingen, 'Aantal')
    aantal_besmettingen.text = str(df['Infections'][row])
    tot_besmet_number += df['Infections'][row]
    totaal_besmettingen = ET.SubElement(besmettingen, 'Totaal')
    totaal_besmettingen.text = str(tot_besmet_number)
    
    vergelijking_besmettingen = ET.SubElement(besmettingen, 'Vergelijking')
    verg_gisteren_besmettingen = ET.SubElement(vergelijking_besmettingen, 'Gisteren')
    if row > 0:
        verg_gisteren_besmettingen.text = str(df['Infections'][row]-df['Infections'][row-1])
        verg_gisteren_besmettingen.set('percentage', str(round(((df['Infections'][row]-df['Infections'][row-1])/df['Infections'][row-1])*100, 1))+"%")
    verg_week_besmettingen = ET.SubElement(vergelijking_besmettingen, 'Week')
    if row > 6:
        week_average = round(sum(df['Infections'][row-7:row-1])/7)
        verg_week_besmettingen.text = str(week_average-df['Infections'][row])
        verg_week_besmettingen.set('percentage', str(round(((week_average-df['Infections'][row])/week_average)*100, 1))+"%")
    
    gemeente_max_besmettingen = ET.SubElement(besmettingen, "GemeenteMax")
    gemeente_max_besmettingen.set("provincie", str(df['Max Infections Province'][row]))
    gemMaxBesmet_gemeente = ET.SubElement(gemeente_max_besmettingen, "Gemeente")
    gemMaxBesmet_gemeente.text = str(df['Max Infections Municipality'][row])
    gemMaxBesmet_aantal = ET.SubElement(gemeente_max_besmettingen, "Aantal")
    gemMaxBesmet_aantal.text = str(df['Max Infections'][row])
    #gemMaxBesmet_totaal = ET.SubElement(gemeente_max_besmettingen, "Totaal")
    
    prov_min_besmettingen = ET.SubElement(besmettingen, "ProvincieMin")
    provMinBesmet_provincie = ET.SubElement(prov_min_besmettingen, "Provincie")
    provMinBesmet_provincie.text = str(df['Min Infections Province'][row])
    provMinBesmet_aantal = ET.SubElement(prov_min_besmettingen, "Aantal")
    provMinBesmet_aantal.text = str(df['Min Infections'][row])
    #gemMinBesmet_totaal = ET.SubElement(gemeente_min_besmettingen, "Totaal")
    
    #leeftijd_besmettingen = ET.SubElement(besmettingen, 'Leeftijd')
    
    
    opnames = ET.SubElement(root, 'Opnames')
    aantal_opnames = ET.SubElement(opnames, 'Aantal')
    aantal_opnames.text = str(df['Hospital Admission'][row])
    totaal_opnames_momenteel = ET.SubElement(opnames, 'TotaalMomenteel')
    totaal_opnames_momenteel.text = str(df['Hospital Total'][row])
    tot_hos_number += df['Hospital Admission'][row]
    totaal_opnames_algemeen = ET.SubElement(opnames, 'TotaalAlgemeen')
    totaal_opnames_algemeen.text = str(tot_hos_number)
    
    vergelijking_opnames = ET.SubElement(opnames, 'Vergelijking')
    verg_gisteren_opnames = ET.SubElement(vergelijking_opnames, 'Gisteren')
    if row > 0:
        verg_gisteren_opnames.text = str(df['Hospital Admission'][row]-df['Hospital Admission'][row-1])
        verg_gisteren_opnames.set('percentage', str(round(((df['Hospital Admission'][row]-df['Hospital Admission'][row-1])/df['Hospital Admission'][row-1])*100, 1))+"%")
    verg_week_opnames = ET.SubElement(vergelijking_opnames, 'Week')
    if row > 6:
        week_average = round(sum(df['Hospital Admission'][row-7:row-1])/7)
        verg_week_opnames.text = str(week_average-df['Hospital Admission'][row])
        verg_week_opnames.set('percentage', str(round(((week_average-df['Hospital Admission'][row])/week_average)*100, 1))+"%")
    
    
    gemeente_max_opnames = ET.SubElement(opnames, "GemeenteMax")
    gemeente_max_opnames.set("provincie", str(df['Max Admissions Province'][row]))
    gemMaxOpname_gemeente = ET.SubElement(gemeente_max_opnames, "Gemeente")
    gemMaxOpname_gemeente.text = str(df['Max Admissions Municipality'][row])
    gemMaxOpname_aantal = ET.SubElement(gemeente_max_opnames, "Aantal")
    gemMaxOpname_aantal.text = str(df['Max Admissions'][row])
    #gemMaxOpname_totaal = ET.SubElement(gemeente_max_opnames, "Totaal")
    
    prov_min_opnames = ET.SubElement(opnames, "ProvincieMin")
    provMinOpname_provincie = ET.SubElement(prov_min_opnames, "Provincie")
    provMinOpname_provincie.text = str(df['Min Admissions Province'][row])
    provMinOpname_aantal = ET.SubElement(prov_min_opnames, "Aantal")
    provMinOpname_aantal.text = str(df['Min Admissions'][row])
    #gemMinOpname_totaal = ET.SubElement(gemeente_min_opnames, "Totaal")
    
    #leeftijd_opnames = ET.SubElement(opnames, 'Leeftijd')
    
    
    kliniek = ET.SubElement(opnames, 'Kliniek')
    aantal_kliniek = ET.SubElement(kliniek, 'Aantal')
    aantal_kliniek.text = str(df['Clinique Admission'][row])
    totaal_kliniek_momenteel = ET.SubElement(kliniek, 'TotaalMomenteel')
    totaal_kliniek_momenteel.text = str(df['Clinique Total'][row])
    tot_clin_number += df['Clinique Admission'][row]
    totaal_kliniek_algemeen = ET.SubElement(kliniek, 'TotaalAlgemeen')
    totaal_kliniek_algemeen.text = str(tot_clin_number)
    
    vergelijking_kliniek = ET.SubElement(kliniek, 'Vergelijking')
    verg_gisteren_kliniek = ET.SubElement(vergelijking_kliniek, 'Gisteren')
    if row > 0:
        verg_gisteren_kliniek.text = str(df['Clinique Admission'][row]-df['Clinique Admission'][row-1])
        verg_gisteren_kliniek.set('percentage', str(round(((df['Clinique Admission'][row]-df['Clinique Admission'][row-1])/df['Clinique Admission'][row-1])*100, 1))+"%")
    verg_week_kliniek = ET.SubElement(vergelijking_kliniek, 'Week')
    if row > 6:
        week_average = round(sum(df['Clinique Admission'][row-7:row-1])/7)
        verg_week_kliniek.text = str(week_average-df['Clinique Admission'][row])
        verg_week_kliniek.set('percentage', str(round(((week_average-df['Clinique Admission'][row])/week_average)*100, 1))+"%")
    
    #leeftijd_kliniek = ET.SubElement(kliniek, 'Leeftijd')
    
    
    ic = ET.SubElement(opnames, 'IC')
    aantal_ic = ET.SubElement(ic, 'Aantal')
    aantal_ic.text = str(df['IC Admission'][row])
    totaal_ic_momenteel = ET.SubElement(ic, 'TotaalMomenteel')
    totaal_ic_momenteel.text = str(df['IC Total'][row])
    tot_ic_number += df['IC Admission'][row]
    totaal_ic_algemeen = ET.SubElement(ic, 'TotaalAlgemeen')
    totaal_ic_algemeen.text = str(tot_ic_number)
    
    vergelijking_ic = ET.SubElement(ic, 'Vergelijking')
    verg_gisteren_ic = ET.SubElement(vergelijking_ic, 'Gisteren')
    if row > 0:
        verg_gisteren_ic.text = str(df['IC Admission'][row]-df['IC Admission'][row-1])
        verg_gisteren_ic.set('percentage', str(round(((df['IC Admission'][row]-df['IC Admission'][row-1])/df['IC Admission'][row-1])*100, 1))+"%")
    verg_week_ic = ET.SubElement(vergelijking_ic, 'Week')
    if row > 6:
        week_average = round(sum(df['IC Admission'][row-7:row-1])/7)
        verg_week_ic.text = str(week_average-df['IC Admission'][row])
        verg_week_ic.set('percentage', str(round(((week_average-df['IC Admission'][row])/week_average)*100, 1))+"%")
    
    
    #leeftijd_ic = ET.SubElement(ic, 'Leeftijd')
    
    
    """ontslagen = ET.SubElement(opnames, 'Ontslagen')
    aantal_ontslagen = ET.SubElement(ontslagen, 'Aantal')
    totaal_ontslagen = ET.SubElement(ontslagen, 'Totaal')
    
    vergelijking_ontslagen = ET.SubElement(ontslagen, 'Vergelijking')
    verg_gisteren_ontslagen = ET.SubElement(vergelijking_ontslagen, 'Gisteren')
    verg_gisteren_ontslagen.set('percentage', "")
    verg_week_ontslagen = ET.SubElement(vergelijking_ontslagen, 'Week')
    verg_week_ontslagen.set('percentage', "")
    
    gemeente_max_ontslagen = ET.SubElement(ontslagen, "GemeenteMax")
    gemMaxOntsl_gemeente = ET.SubElement(gemeente_max_ontslagen, "Gemeente")
    gemMaxOntsl_aantal = ET.SubElement(gemeente_max_ontslagen, "Aantal")
    gemMaxOntsl_totaal = ET.SubElement(gemeente_max_ontslagen, "Totaal")
    
    gemeente_min_ontslagen = ET.SubElement(ontslagen, "GemeenteMin")
    gemMinOntsl_gemeente = ET.SubElement(gemeente_min_ontslagen, "Gemeente")
    gemMinOntsl_aantal = ET.SubElement(gemeente_min_ontslagen, "Aantal")
    gemMinOntsl_totaal = ET.SubElement(gemeente_min_ontslagen, "Totaal")
    
    leeftijd_ontslagen = ET.SubElement(ontslagen, 'Leeftijd')"""
    
    
    doden = ET. SubElement(root, 'Doden')
    aantal_doden = ET.SubElement(doden, 'Aantal')
    tot_doden_number += df['Deceased'][row]
    aantal_doden.text = str(df['Deceased'][row])
    totaal_doden = ET.SubElement(doden, 'Totaal')
    totaal_doden.text = str(tot_doden_number)
    
    vergelijking_doden = ET.SubElement(doden, 'Vergelijking')
    verg_gisteren_doden = ET.SubElement(vergelijking_doden, 'Gisteren')
    if row > 0:
        verg_gisteren_doden.text = str(df['Deceased'][row]-df['Deceased'][row-1])
        verg_gisteren_doden.set('percentage', str(round(((df['Deceased'][row]-df['Deceased'][row-1])/df['Deceased'][row-1])*100, 1))+"%")
    verg_week_doden = ET.SubElement(vergelijking_doden, 'Week')
    if row > 6:
        week_average = round(sum(df['Deceased'][row-7:row-1])/7)
        verg_week_doden.text = str(week_average-df['Deceased'][row])
        verg_week_doden.set('percentage', str(round(((week_average-df['Deceased'][row])/week_average)*100, 1))+"%")
    
    gemeente_max_doden = ET.SubElement(doden, "GemeenteMax")
    gemeente_max_doden.set("provincie", str(df['Max Deceased Province'][row]))
    gemMaxDoden_gemeente = ET.SubElement(gemeente_max_doden, "Gemeente")
    gemMaxDoden_gemeente.text = str(df['Max Deceased Municipality'][row])
    gemMaxDoden_aantal = ET.SubElement(gemeente_max_doden, "Aantal")
    gemMaxDoden_aantal.text = str(df['Max Deceased'][row])
    #gemMaxDoden_totaal = ET.SubElement(gemeente_max_doden, "Totaal")
    
    prov_min_doden = ET.SubElement(doden, "ProvincieMin")
    provMinDoden_provincie = ET.SubElement(prov_min_doden, "Provincie")
    provMinDoden_provincie.text = str(df['Min Deceased Province'][row])
    provMinDoden_aantal = ET.SubElement(prov_min_doden, "Aantal")
    provMinDoden_aantal.text = str(df['Min Deceased'][row])
    #gemMinDoden_totaal = ET.SubElement(gemeente_min_doden, "Totaal")
    
    #leeftijd_doden = ET.SubElement(doden, 'Leeftijd')
    
    
    vaccinaties = ET. SubElement(root, 'Vaccinaties')
    aantal_vaccinaties = ET.SubElement(vaccinaties, 'Aantal')
    aantal_vaccinaties.text = str(df['Vaccines'][row])
    totaal_vaccinaties = ET.SubElement(vaccinaties, 'Totaal')
    if row > 4:    
        tot_vac_number += df['Vaccines'][row]
        totaal_vaccinaties.text = str(tot_vac_number)
    
    vergelijking_vaccinaties = ET.SubElement(vaccinaties, 'Vergelijking')
    verg_gisteren_vaccinaties = ET.SubElement(vergelijking_vaccinaties, 'Gisteren')
    if row > 5:
        verg_gisteren_vaccinaties.text = str(df['Vaccines'][row]-df['Vaccines'][row-1])
        verg_gisteren_vaccinaties.set('percentage', str(round(((df['Vaccines'][row]-df['Vaccines'][row-1])/df['Vaccines'][row-1])*100, 1))+"%")
    verg_week_vaccinaties = ET.SubElement(vergelijking_vaccinaties, 'Week')
    if row > 11:
        week_average = round(sum(df['Vaccines'][row-7:row-1])/7)
        verg_week_vaccinaties.text = str(week_average-df['Vaccines'][row])
        verg_week_vaccinaties.set('percentage', str(round(((week_average-df['Vaccines'][row])/week_average)*100, 1))+"%")
    
    
    """gemeente_max_vaccinaties = ET.SubElement(vaccinaties, "GemeenteMax")
    gemMaxVac_gemeente = ET.SubElement(gemeente_max_vaccinaties, "Gemeente")
    gemMaxVac_aantal = ET.SubElement(gemeente_max_vaccinaties, "Aantal")
    gemMaxVac_totaal = ET.SubElement(gemeente_max_vaccinaties, "Totaal")
    
    gemeente_min_vaccinaties = ET.SubElement(vaccinaties, "GemeenteMin")
    gemMinVac_gemeente = ET.SubElement(gemeente_min_vaccinaties, "Gemeente")
    gemMinVac_aantal = ET.SubElement(gemeente_min_vaccinaties, "Aantal")
    gemMinVac_totaal = ET.SubElement(gemeente_min_vaccinaties, "Totaal")"""
    
    #leeftijd_vaccinaties = ET.SubElement(vaccinaties, 'Leeftijd')
    
    
    #r_getal = ET. SubElement(root, 'Rgetal')
    
    
    data = xml_minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    file = open(filename, "w")
    file.write(data)
    file.close()
    row += 1


