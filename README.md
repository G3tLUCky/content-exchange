# content-exchange
This is a readme-file for the Master Thesis: The Content Exchange (under the supervision of Chris van der Lee). The aim of this thesis is to create a Natural Language Generator that generates texts regarding to Covid-19 in the Netherlands, e.g. the amount of people who are infected per day, the number of hospital admissions (including admissions on Intensive Care) per day and the amount of deceased people per day.

This project tries to follow the same structure as a NLG which has been created by Chris van der Lee in order to generate soccer reports with a human tone of voice. Therefore, the first step is to collect (the appropriate amount of) data on which the NLG can be tested. However, Munzert, Rubba, Meißner, and Nyhuis (2015) also suggest to define the variables first before deciding where to look for data.

Taking this into account, some important variables for the current system are: -The daily and total number of Covid-tests -The daily and total number of Covid-infections -The daily and total number of hospital admissions, including admissions on the Intensive Care and admissions in regular clinics. -The daily and total number of new people who passed away due to Covid-19 -The daily and total number of vaccines

Data related to these variables were offered in data files on websites from the RIVM, NICE, and LPCS. These are all Dutch institutions that register important information about the Covid-virus in the Netherlands and publicly share this information online. All collected data can be found under databases in all_data.xlsx.

The data in all_data.xlsx shows the data from 01-01-2021 till 31-03-2021 and has been transformed to a XML-format by using excel_to_xml.py. This way, the data is shown per day (see the 'XML_files'-directory).

The directory 'template texts' includes a text file with articles that have been published by different news organizations during the pandemic. These texts were used to generate the template sentences in Templates_complete.xlsx. pdf_to_txt.py has been used to transform the texts, that originally appeared in PDF-format, to a .txt-format.

The 'automatically-generated'-directory shows all texts and visual displays that have been created by the system. The 'human-written'-directory, on the other hand, shows the texts that have been written by a Dutch news organization (namely NOS).

The system itself can be found under 'Modules.' The following modules are included:

-Lookup_module.py: This module loads the XML-data and templates.
-Template_Selection_Module: This module uses Ruleset_module.py to determine which templates are eligible according to the XML-data and randomly chooses a template from all possible templates.
-Template_Filler_Module: This module fills the gaps in the chosen templates with the appropriate XML-data.
-Text_Collection_Module: This module collects all filled out templates (i.e. sentences), and creates a coherent text with them.
-Visual_Display_Module: This module randomly chooses a topic (e.g. infections, vaccines, etc.) and creates a line graph that shows a trend (related to the topic) during the last seven days
-Governing_Module: This module interacts with every module and saves the resulting text and graph to a .txt- and .png-file.





