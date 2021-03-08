# content-exchange
This is a readme-file for the Master Thesis: The Content Exchange (under the supervision of Chris van der Lee). 
The aim of this thesis is to create a Natural Language Generator that generates texts regarding to Covid-19 in the Netherlands,
e.g. the amount of people who are infected per day, the number of hospital admissions (including admissions on Intensive Care) per day and the amount of deceased people per day.

This project tries to follow the same structure as a NLG which has been created by Chris van der Lee in order to generate soccer reports with a human tone of voice.
Therefore, the first step is to collect (the appropriate amount of) data on which the NLG can be tested. However, Munzert, Rubba, Meißner, and Nyhuis (2015) also suggest to define the variables first before deciding where to look for data.

Taking this into account, some important variables for the current system could be:
- The number of new covid-19 infections on a certain day
- The number of new hospital admissions on a certain day, including:
          - Admissions in the Intensive Care
          - Admissions in regular clinics
- The number of new people who passed away due to covid-19 on a certain day

These seem the most important variables for now, and it seems appropriate to keep the amount of variables low at the start, since this will make it easier to test the system. However, other variables can certainly be implemented in the future, like:
- The amount of new vaccinations given to people on a certain
- The number of new people who left the hospital/IC on a certain day
- The total/cumulative amount for all variables so far
- Numbers that don't match trends (so-called outliers) on a certain day
- Variables that compare the numbers with the numbers from earlier days or with the average number of a certain week (which could also make it easier to spot outliers)
- Variables that include demographics, like age or sex.
- And finally, variables that look at covid-19 in certain provinces/regions of the Netherlands or variables that compare the Netherlands with other countries in the world.
