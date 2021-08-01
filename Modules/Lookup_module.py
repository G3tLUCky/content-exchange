import xml.etree.ElementTree as ET
import pandas as pd
import os


def Template_Converter(excel_file):
    df = pd.read_excel(excel_file)

    legend = []
    templates = []

    for col_name in df:
        legend.append(col_name)
        temp = []
        for cell in df[col_name]:
            if not isinstance(cell, float):
                temp.append(cell)
        templates.append(temp)
    
    return legend, templates


def Data_Files(path):
    os.chdir(path)
    current_dir = os.listdir(".")
    all_xml = []     
    for file in current_dir:
        tree = ET.parse(file)
        root = tree.getroot()
        all_xml.append(root)
    return all_xml


    