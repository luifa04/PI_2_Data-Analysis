<h1 align='center'>
 <b>Homicides in Traffic Accidents in the City of Buenos Aires</b>
</h1>

<p align='center'>
<img src = 'Img/Siniestros-viales.jpg' height = 500>
<p>

## <h1 align="center">**Introduction**</h1>

In this simulated scenario, we assume the role of a Data Analyst in a consulting company's team. The company has been contacted by the Mobility and Road Safety Observatory (OMSV), a research center under the jurisdiction of the Ministry of Transportation of the Government of the Autonomous City of Buenos Aires (CABA). The OMSV has requested our team to conduct a data analysis project.

The primary objective of this project is to provide valuable information that enables local authorities to take concrete measures to reduce the number of fatalities in traffic accidents in CABA. To carry out this analysis, we have a dataset covering homicides in traffic accidents that occurred in the City of Buenos Aires between 2016 and 2021.

As final deliverables, the project includes a detailed report describing the tasks performed, adopted methodologies, and key conclusions. Additionally, the creation of an interactive visualization panel (dashboard) is requested to facilitate the interpretation and analysis of information.


## <h1 align="center">**Context**</h1>


Traffic accidents, also known as road accidents, involve vehicles on public roads and can result from various causes such as collisions between cars, motorcycles, bicycles, or pedestrians, as well as collisions with fixed objects or vehicle overturns. These incidents can lead to consequences ranging from property damage to severe or even fatal injuries for those involved.

The Autonomous City of Buenos Aires (CABA), located in the province of Buenos Aires, Argentina, is not immune to this issue. Traffic accidents pose a significant concern due to the high volume of traffic and population density in the area. These events can significantly impact the safety of residents and visitors, as well as the road infrastructure and emergency services.

According to the 2022 population census, CABA is estimated to have a population of 3,120,612 inhabitants, covering an area of 200 km², resulting in an approximate density of 15,603 inhabitants/km². Additionally, in July 2023, 12,437,735 vehicles were recorded passing through toll booths on access highways to CABA. In this context, the prevention of traffic accidents and the implementation of effective policies are crucial to address this issue adequately.


## <h1 align="center">**Data**</h1>

For this project, we worked with the Fatal Victims in Traffic Accidents dataset in Excel format, containing two data sheets:

- **HECHOS:** Contains a row per incident with a unique ID and associated temporal, spatial, and participant variables.
- **VICTIMAS:** Contains a row for each victim of the incidents with variables such as age, gender, and mode of displacement.

For a detailed explanation of the definitions used in the data and the development of this project, refer to this [document](Data\NOTAS_HOMICIDIOS_SINIESTRO_VIAL.pdf). The dataset used in the analysis can be found [here](https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales).

## <h1 align="center">**Technologies**</h1>

Python and Pandas were used for data extraction, transformation, and loading processes, as well as for exploratory data analysis. Additional data for population estimation in 2021 was obtained through web scraping using the BeautifulSoup library. Details can be found [here](Poblacion_CABA.ipynb). Finally, Power BI was utilized for the construction of an interactive dashboard, available [here](DashBoard.pbix).

## <h1 align="center">**EDA**</h1>


First, data extraction was performed. After a brief exploratory and descriptive analysis, topics such as outliers, duplicated values, and missing values will be addressed. Additionally, certain columns will be normalized to work optimally in the creation of relevant graphics with their respective variables. This EDA is divided into two parts for practicality and readability. This first [EDA_PART_1](EDA_Part_1.ipynb) covers the aforementioned, and subsequently, in the second document [EDA_PART_2](EDA_Part_2.ipynb), relevant graphs will be created.

# <h1 align="center">**Data Analysis**</h1>
## <h1 align="center">**Analysis of Temporal Distribution**</h1>

In a preliminary evaluation, the temporal variable was examined to understand the distribution of homicides at different time scales. The annual distribution of fatal victims is notably 60% during the first 3 years of the dataset, with a marked decrease in 2020 due to COVID-19 quarantine measures. Monthly variation throughout the year is significant, with a peak in December. This December increase is related to the easing of quarantine measures.

Descending in the temporal scale, it is observed that 70% of the victims lost their lives between Monday and Friday, suggesting a possible association with daily commuting. However, in the weekly distribution, no significant differences are seen between different days. That is, the number of victims on Saturday or Sunday is approximately the same for the dataset.

Analyzing the time slots, it stands out that 12% of the victims were recorded between 6 to 8 in the morning, suggesting a possible relation to the work entry hours. However, within this time frame, 55% of the victims experienced incidents during the weekend.

## <h1 align="center">**Victim Profile**</h1>


Regarding the victim's profile, 77% of the victims are male. Almost 50% of the victims fall in the age range of 25 to 44 years, and within this group, 84% are males.

Regarding the victim's role, i.e., the position they occupied at the time of the incident, 48% were drivers. This 48% is divided into 77% of victims who were moving on motorcycles and 19% in cars. Regarding the means of transport at the time of the incident, 42% are motorcycle drivers, with 88% of these drivers being male.

Regarding responsibility in the incident, i.e., the vehicle occupied by the accused person, in 29% of cases, it was a car, but 75% are the responsibility of vehicles such as cars, buses, and trucks.

## <h1 align="center">**Analysis by Location**</h1>

Patterns in the spatial distribution of incidents were explored. A notable finding is that in all districts of CABA, avenues, arterial roads at least 13 meters wide, are common in accidents. 62% of victims lost their lives on avenues, and 82% of these incidents occurred at the intersection of avenues with other streets. This pattern remains consistent over the years. Regarding the victim's role, it varies between motorcycles and pedestrians in different districts.

# <h1 align="center">**KPIs**</h1>


- `*Reduce by 10% the homicide rate in traffic accidents in the last six months, in CABA, compared to the homicide rate in traffic accidents in the previous semester*`.

  We define the **homicide rate in traffic accidents** as the number of fatal victims in traffic accidents per 100,000 inhabitants in a geographical area during a specific period. Its formula is:

  $\text{Homicide rate in traffic accidents} = \frac{\text{Number of homicides in traffic accidents}}{\text{Total population}}·100,000$

  To determine the Total Population in 2021, an estimate was made based on the population censuses of 2010 and 2022. This value is used in the calculation of the Homicide Rate in Traffic Accidents.

  In 2021, the homicide rate in traffic accidents was 1.77, indicating that there were approximately 1.77 homicides in traffic accidents per 100,000 inhabitants during the first 6 months of the year. The established goal is to reduce this rate to 1.60 in the following semester of 2021, representing a 10% decrease.

  By calculating the KPI for this period, it is found that the Homicide Rate in Traffic Accidents was 1.35, meaning that the proposed objective was successfully achieved. This result suggests an improvement in road safety during the second semester of 2021, achieving a 10% reduction compared to the previous semester.

- `*Reduce by 7% the number of fatal accidents involving motorcyclists in the last year, in CABA, compared to the previous year*`.

  We define the **number of fatal accidents involving motorcyclists in traffic accidents** as the absolute number of fatal accidents involving victims traveling on motorcycles in a given time period. Its formula to measure the evolution of fatal accidents with motorcycle victims is:

  $\text{Number of fatal accidents involving motorcyclists} = -\frac{\text{Motorcycle victims previous year - Motorcycle victims current year}}{\text{Motorcycle victims previous year}}·100$

  Where:
  - $\text{Motorcycle victims previous year}$: Number of fatal accidents with motorcycle victims in the previous year
  - $\text{Motorcycle victims current year}$: Number of fatal accidents with motorcycle victims in the current year

  To analyze the evolution of fatal accidents involving motorcyclists, the figures for 2020 (considered the previous year) and 2021 (considered the current year) were compared. The established goal was to achieve a 7% reduction in the number of fatal accidents compared to the previous year.

  Initially, the Number of Fatal Accidents Involving Motorcyclists for 2020 was calculated, obtaining a value of -44.00. This negative result indicates a decrease compared to the previous year and sets the basis for the goal to be achieved. The proposed goal was a reduction of 7%, equivalent to -40.92 accidents.

  However, when calculating the Number of Fatal Accidents Involving Motorcyclists for 2021, a value of 64.29 was obtained, indicating a 64% increase in the number of deaths of motorcycle drivers compared to 2020. This result suggests that, unfortunately, the established goal was not achieved, as a significant increase in the number of fatal accidents involving motorcyclists was experienced during 2021.

* `*Reduce by 10% the homicide rate on avenues in the last year, in CABA, compared to the previous year*`

  As seen in the exploratory analysis, 62% of fatal victims were traveling on avenues at the time of the incident. The **Homicide Rate on Avenues** is defined as the number of fatal victims in traffic accidents on avenues per 100,000 inhabitants in a geographical area during a specific period, in this case, annually. Its formula is:

  $\text{Homicide rate on avenues} = \frac{\text{Number of fatal accidents with victims that occurred on avenues}}{\text{Total population}}·100000$

  To analyze safety on avenues, the Homicide Rate on Avenues for 2020 was calculated, obtaining a value of 1.68. This indicator served as a reference to set an ambitious goal for the following year, establishing a 10% reduction in the homicide rate compared to 2020. The defined goal was to achieve a Homicide Rate on Avenues of 1.51 for 2021.

  However, when calculating the Homicide Rate on Avenues for 2021, a value of 1.97 was obtained, indicating that the established goal was not achieved. Instead of experiencing a 10% decrease, the homicide rate on avenues increased compared to the previous year, exceeding the set expectations. This result suggests the need to review and adjust strategies to improve road safety on the avenues of the Autonomous City of Buenos Aires.

<p align='center'>
<img src = 'Img/kpis.png' height = 350>
<p>

## <h1 align="center">**Conclusions**</h1>

During the period from 2016 to 2021, 717 fatal victims were recorded in traffic accidents in the Autonomous City of Buenos Aires (CABA). Of this total, 70% of incidents took place during weekdays, highlighting the importance of focusing safety measures during these specific times.

### Key Findings:

- **Time Slot:** 12% of fatal accidents occur between 6 and 8 in the morning, mainly during weekends.
  
- **Critical Month:** December records the maximum number of deaths, emphasizing the importance of specific campaigns during this month.

- **Gender and Age:** 77% of victims were males, half of them in the 25 to 44 age range.

- **User Type:** Motorcyclists represent 42% of cases.

- **Avenues:** 62% of traffic homicides occurred on avenues, with 82% at intersections with other streets.

### Recommendations:

1. Continue monitoring the proposed objectives with specific campaigns, especially targeting motorcycle drivers and avenue users.

2. Strengthen road safety campaigns between Fridays and Mondays, intensifying particularly in December.

3. Emphasize safe driving campaigns on avenues and street intersections.

4. Direct safety campaigns towards males, especially in terms of motorcycle driving, for an age range between 15 and 44 years.

### Results and Goals Achieved:

Despite successfully achieving the goal of reducing the homicide rate in traffic accidents during the second semester of 2021, the set goals to decrease the number of fatal accidents involving motorcyclists and on avenues during the same year compared to 2020 were not met.

As a result, it is recommended to continue monitoring and adjusting strategies, with a specific focus on campaigns targeting motorcycle drivers, avenue users, and specific days of the week, especially in December. Additionally, reinforcing campaigns aimed at males, covering safe driving, especially for those in the age range between 15 and 44 years, is suggested. These actions could significantly contribute to improving road safety in CABA.







