# project3-wildfires
Bootcamp Project 3 - Wildfires History

Project Overview:
We (Emilia Roberts, Chris Tanner, Dustin Malandra, and Justin Lawrence) are using a compiled and cleaned database published by the USDA to visualize trends in wildfire size and location on a year by year basis. We wanted to visualize size, prevalence and locations of class D and above (>100 acres burned) wildfires over time course in complete database,Examine most severe fires and what caused them (eg. lightning strike/human cause), and see how humans start forest fires and what can be done to mitigate human started fires.



###
Instructions:
###

Wildfire Size and Location Graphics
For the cause breakdown: The data was given in a SQLite database from the USDA. With this large data set centered around wildfiresand using DB Browser, we were able to download and clean the data in a csv format. Fire size was filtered to only have fires greater than 100 acres. The dataset was filtered by year and state and plotted using plotly, scattergeo, and Dash and dash bootstrap components was used to create the app.

For the cause breakdown: The data was given in a SQLite database from the USDA. With this large data set centered around wildfiresand using DB Browser, we were able to download and clean the data in a csv format. 
After the data was cleaned and into a more manageable format, I was able to use data frames and pandas in order to make a map and filtered bar chart. These interactive visuals were made with Python and Plotly then exported into an html where they could be viewed and manipulated base applied filters using Dash. 

For the animated bar chart which examines total number of fires per fire code for a given year:
Wildfire data gathered from the USDA (all table columns deleted except for fire year and fire code) was exported from SQLite DB Viewer into a .csv file.  The .csv was read into a Pandas DataFrame, then a new column was added to include the sum for each code per year.  The resulting DataFrame was exported as an excel spreadsheet for further organization.  The spreadsheet was parsed into 1 workbook for each year of data, then those workbooks were saved as new .csv's, then converted to .json's inside a new Jupyter notebook.  The final .jsons (1 per year of data) were the arrays used to create the interactive bar chart in a JavaScript HTML file.
5:09
To run the app, the year 1992 should auto-load with the chart.  Any year can be toggled to show fire code counts for that specific year.

Number of Fires by Year Line chart and Causes of Fires bar charts:
Data was downloaded from the US Department of Agriculture
https://www.fs.usda.gov/rds/archive/catalog/RDS-2013-0009.6
The data was provided as a SQLite database file. This was opened in DB Viewer to examine its structure. The data used in this work is in a single table so unwanted columns were removed. The table was then exported as a .csv file.
The csv was imported into a Jupyter notebook, cleaned and filtered using Pandas. Interactive graphs were built using Plotly for Python and exported as a html file using Dash



###
Ethical Considerations:
###

After examining all the data, we determined that there was no personal identifying information. Therefore we had no ethical considerations for actually transforming/displaying that data. That being said, we believe that we have an imperative to present data related to dangerous wildfires, especially in places where human created wildfires may be dangerous and destructive to people.




###
References:
###

- Spatial wildfire occurrence data for the United States, 1992-2020 https://www.fs.usda.gov/rds/archive/catalog/RDS-2013-0009.6
- https://www.iii.org/fact-statistic/facts-statistics-wildfires
- https://www.nifc.gov/fire-information/fire-prevention-education-mitigation/wildfire-prevention
- https://www.nwcg.gov/sites/default/files/data-standards/pdf/values.pdf
- https://www.fs.usda.gov/rds/archive/catalog/RDS-2013-0009.6
- https://www.somervillema.gov/news/arson-prevention-tips-and-fire-safety 
- https://smokeybear.com/en/prevention-how-tos/backyard-debris-burning 
- https://www.fastcompany.com/90945794/power-lines-and-wildfires-why-the-decision-to-shut-off-power-is-more-complicated-that-youd-think#:~:text=There%20are%20a%20lot%20of,touch%20dry%20grass%20or%20trees.  
