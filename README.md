# COVID-19 Data Analysis using PySpark

This project performs basic COVID-19 data analysis using PySpark and the Our World in Data (OWID) COVID dataset.

## Project Objectives

The project demonstrates how Apache Spark can be used for large-scale data processing and analysis.

### Tasks Performed
- Load COVID-19 dataset
- Filter country-specific records
- Find total COVID cases and deaths
- Sort countries by highest number of cases

---

## Technologies Used

- Python
- PySpark
- Apache Spark
- Command Prompt (CMD)

---

## Dataset

Dataset used:

- Our World in Data (OWID) COVID-19 Dataset

Download Link:
https://ourworldindata.org/covid-deaths

CSV File:
`owid-covid-data.csv`
But I could not upload the csv file here because of its huge size. 
---

## Insights 
=> In first step we loaded the data set named “owid-covid-data.csv” in our 
working environment to perform different operations on the data. 
=> In second step we filter country-specific data and the country we take is China 
and total cases and total deaths are shown. China was one of the first countries 
affected by COVID-19.   Initial COVID-19 cases in China increased rapidly 
during the early outbreak period. The total number of deaths increased with 
the rise in total cases. PySpark efficiently processed and analyzed China’s 
large COVID-19 dataset. 
=> In third step we found Total cases and deaths overall. The purpose of this step 
was to observe the overall impact of COVID-19 on public health. By 
analyzing these values, we could compare the spread of the virus and the 
number of deaths caused by it. 
=> In forth step we apply Sorting by highest cases. The Sorting is an important 
data analysis technique because it helps users quickly identify trends and 
compare records. Through this step, we were able to analyze which countries 
experienced the largest outbreaks during the pandemic.

## Project Structure

```text
COVID-19-Data-Analysis/
│
├── covid_analysis.py
├── owid-covid-data.csv
└── README.md
----
