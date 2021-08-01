import random
import os
from Lookup_module import Template_Converter, Data_Files
from Template_Selection_Module import Template_Selection
from Template_Filler_Module import Template_Filler
from Text_Collection_Module import Text_Collection
from Visual_Display_Module import Visual_Display

os.chdir("C:/Users/lucla/Documents/Studie/Tilburg University/Masterscriptie")
path = "C:/Users/lucla/Documents/Studie/Tilburg University/Masterscriptie/databases/Cijfers/XML_files"
leg, temp = Template_Converter("Templates_complete.xlsx")
data = Data_Files(path)

indices = [x for x in range(0, len(data))]
idx = random.choice(indices)
gapped_templates = Template_Selection(leg, temp, data, idx)
templates = Template_Filler(gapped_templates, data, idx)

text = Text_Collection(templates)
Visual_Display(data, data[idx-6:idx+1])

os.chdir("C:/Users/lucla/Documents/Studie/Tilburg University/Masterscriptie/Output")
file = open("Covid_Text.txt", 'w', encoding = "UTF-8")
file.write(text)
file.close()
