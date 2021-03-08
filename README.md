# content-exchange
This is a readme-file for the Master Thesis: The Content Exchange (under the supervision of Chris van der Lee). 
The aim of this thesis is to create a Natural Language Generator that generates texts regarding to Covid-19 in the Netherlands,
e.g. the amount of people who are infected per day, the number of hospital admissions (including admissions on Intensive Care) per day and the amount of deceased people per day.

This project tries to follow the same structure as a NLG which has been created by Chris van der Lee in order to generate soccer reports with a human tone of voice.
Therefore, the first step is to collect (the appropriate amount of) data on which the NLG can be tested. However, Munzert, Rubba, Meißner, and Nyhuis (2015) also suggest to define the variables first before deciding where to look for data.

Taking this into account, some important variables for the current system could be:
- The number of new Covid-19 infections on a certain day
- The number of new hospital admissions on a certain day, including:
          - Admissions in the Intensive Care
          - Admissions in regular clinics
- The number of new people who passed away due to Covid-19 on a certain day

These seem the most important variables for now, and it seems appropriate to keep the amount of variables low at the start, since this will make it easier to test the system. However, other variables can certainly be implemented in the future, like:
- The amount of new vaccinations given to people on a certain
- The number of new people who left the hospital/IC on a certain day
- The total/cumulative amount for all variables so far
- Numbers that don't match trends (so-called outliers) on a certain day
- Variables that compare the numbers with the numbers from earlier days or with the average number of a certain week (which could also make it easier to spot outliers)
- Variables that include demographics, like age or sex.
- And finally, variables that look at Covid-19 in certain provinces/regions of the Netherlands or variables that compare the Netherlands with other countries in the world.

Now that the variables are known, my search for appropriate data begins. After looking at a reasonable amount of websites, I could already conclude that many websites were not really practical, because they either 1) consisted of an interactive dashboard without any files that could be downloaded, which makes regular webscraping more difficult, 2) only showed the covid-related numbers of today and not of earlier days, which makes it harder to collect enough data to test the system on, and (3 consisted of a labyrinth of secundary sources, which makes it not only harder to manage, organize and evaluate the data, but also to acknowledge the appropriate sources. Let's take a look at some of these websites/sources:
- WHO (https://covid19.who.int/region/euro/country/nl): Not only does WHO use an interactive dashboard (which is hard to scrape), but it also reports Covid-cases one day later (e.g. number of infections on the 17th of January are actually the number of infections on the 16th of January according to Dutch institutions). Moreover, the dashboard seems to be a secondary source.
- https://ourworldindata.org/coronavirus/country/netherlands?country=~NLD: This site seems to report different numbers for the Netherlands than the numbers reported on most other sites
- https://coronadashboard.rijksoverheid.nl/: Even though this website seems/is very useful to check the correctness of other sources (which has been done during the project from time to time), the data on this website are more difficult to retrieve than data on other websites.

Talking about websites on which data is easier to retrieve, let's also take a look at those sites:
-https://data.rivm.nl/covid-19/: This site provides multiple files with Covid-related numbers that are being updates every day! Theses files are provided by Dutch governmental institutions and Dutch healthcare institutions, like the RIVM (Rijksinstituut voor Volksgezondheid en Milieu) and NICE (Nationale Intensive Care Evaluatie), which makes the site a reliable source. Moreover, the files are created since the start of the Covid-pandemic, which means that there is enough data to test the system on.
-https://github.com/J535D165/CoronaWatchNL#geographical-datasets: Even though this site is a secondary source, it provides a nice overview of the data since the start of the Covid-pandemic, and, more importantly, it's easy to retrieve this data! The numbers on this site also match or are close to the numbers on other sites, like https://graphics.reuters.com/world-coronavirus-tracker-and-maps/countries-and-territories/netherlands/ and https://www.worldometers.info/coronavirus/country/netherlands/. One thing has to be noted, namely that the numbers don't exactly match the numbers of the RIVM. That is because the RIVM constantly updates its numbers (due to, for example, the delay of reported Covid-cases), while the github-version only retrieves the numbers of its primary sources on a certain time every day (without updating). Still, the numbers are close to the numbers of formal institutions and are available to the public, which makes it more feasible to retrieve data from this site.
-https://www.nporadio1.nl/binnenland/25799-de-coronacijfers-van-vandaag: The site of NPORadio1 (a public broadcasting channel) is also a secondary source and it doesn't update its numbers either (which means that the numbers on this site might deviate a little from the numbers of other websites), but it does provide a nice overview of the number of infections, hospital admissions and deceased people. Moreover, the information on this website is easy to scrape using a HTML webscraper (which is included in this branch).
-https://lcps.nu/datafeed/: LCPS is another Dutch organization that provides the number of hospital admissions in a csv.-dataset that is easy to retrieve. However, this dataset has to be treated with caution because of two reasons: 1) Even though the file provides enough data, the dataset doesn't show the numbers from the start of the Covid-pandemic in the Netherlands (i.e. it only shows the data untill October 2020), and 2) LCPS reports the numbers regarding the occupation of hospital beds (including beds on the IC), which differs from the actual amount of Covid-patients in hospitals reported by NICE.

This information led to the creation of six files, that are all included under 'databases.'
- RIVM_numbers_infections_and_deceased --> shows the number of new Covid-19 infections and deaths on every day according to the RIVM
- npo_numbers --> secondary source that shows information for each main variable (including the total amount of each variable) according to NPORadio1
- NICE_numbers_hospital_admission --> shows the number of new hospital admissions, including admissions in regular clinics, on every day according to NICE (Note: the number of admissions in regular clinics has been calculated by subtracting numbers from NICE with numbers from the github-source).
- LCPS_numbers_hospital_admission --> shows the number of new hospital admissions, including admissions in the IC and regular clinics, on every day according to LCPS
- github_numbers_IC --> secondary source that shows the number of new hospital admissions in the IC on every day
- github_number_infections_and_deceased --> secondary source that shows the number of new Covid-19 infections and deaths on every day
