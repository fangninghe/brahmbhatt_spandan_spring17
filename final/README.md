# Final Exam Report
## Introduction
### Topic and Data Source
> H1B visa, an employment-based, non-immigrant visa category for temporary foreign workers in the United States, is which we international students care most if we have the intention of working in the US after graduation. Since it is the hot seaon for applying H-1B Visa, I would like to analyse the dataset named **H-1B Visa Petitions for the period 2011-2016**, which is from **Kaggle**. Please refer to **_h1b_kaggle.csv_** file in folder **final/data/**.

### Documentation for dataset
> * **CASE_STATUS**: Status associated with the last significant event or decision. Valid values include _“Certified,” “Certified-Withdrawn,” Denied,” and “Withdrawn”_.
>    * Certified: Employer filed the LCA, which was approved by DOL
>    * Certified Withdrawn: LCA was approved but later withdrawn by employer
>    * Withdrawn: LCA was withdrawn by employer before approval
>    * Denied: LCA was denied by DOL.
> * **EMPLOYER_NAME**: Name of employer submitting labor condition application.
> * **SOC_NAME**: Occupational name associated with the **SOC_CODE**. **SOC_CODE** is the occupational code associated with the job being requested for temporary labor condition, as classified by the Standard Occupational Classification (SOC) System.
> * **JOB_TITLE**: Title of the job.
> * **FULL_TIME_POSITION**: Y = Full Time Position; N = Part Time Position.
> * **PREVAILING_WAGE**: Prevailing Wage for the job being requested for temporary labor condition. The wage is listed at annual scale in USD. The prevailing wage for a job position is defined as the average wage paid to similarly employed workers in the requested occupation in the area of intended employment. The prevailing wage is based on the employer’s minimum requirements for the position.
> * **YEAR**: Year in which the H-1B visa petition was filed.
> * **WORKSITE**: City and State information of the foreign worker's intended area of employment.
> * **lon**: longitude of the Worksite.
> * **lat**: latitude of the Worksite.

## Instructions of running my code
> * Packages: pandas, matplotlib.pyplot, mpl_toolkits.basemap, seaborn.
> * Big files: the downloaded data size is 469 MB, I used git LFS to upload it. But just in case some unexpected situaiton, the original download address is https://www.kaggle.com/nsharan/h-1b-visa.

## Analysis 1： Demonstrate the distribution of H1-B opportunities all over US by latitude and longitude.
### Data cleaning
1. Delete old index column.
2. Remove rows with nan values.
3. Create a matrix with **lan** and **lon**.
   The map is shown below:
    !['data2011'](/final/analysis/ana_[1-5]/ana_1.png)

### Conclusion
According to the map, most of the H1-B opportunities are at the east and west coasts. 
   
   
## Analysis 2： Find the top 10 states with the most HI-B visa opportunities by year

1. Split **WORKSITE** into **CITY** and **STATE**.
2. Group by **YEAR** and **STATE**.
3. Select the top ten states within each **STATE** group.
4. Please refer to file _ana\_2.csv_ in folder **final/analysis/ana[1-5]/**.
5. The bar charts of each year are as below:

 !['data2011'](/final/analysis/ana_[1-5]/ana_2_2011.png)
 
 !['data2012'](/final/analysis/ana_[1-5]/ana_2_2012.png)
 
 !['data2013'](/final/analysis/ana_[1-5]/ana_2_2013.png)
 
 !['data2014'](/final/analysis/ana_[1-5]/ana_2_2014.png)
 
 !['data2015'](/final/analysis/ana_[1-5]/ana_2_2015.png)
 
 !['data2016'](/final/analysis/ana_[1-5]/ana_2_2016.png)
 
### Conclusion
From the result by year, top 5 states are selected, which are **CALIFORNIA, ILLINOIS, NEW JERSEY, NEW YORK and TEXAS**. Data from those 5 states are selected for the seconde analysis.


## Analysis 3： Find the top 20% cities and top 20% occupations with the most HI-B visa opportunities in total.
1. Select data from top 5 states mentioned in last analysis.
2. Analyze **CASE_STATUS**, as is shown below, **CERTIFIED** data is selected based on 2 reason. One reason is the **CERTIFIED** data makes the most sense for foreign candidates. The other reason is that according to the pie chart, more than 80% of the cases` result is **CERTIFIED**.
 
  !['data_casgstatus'](/final/analysis/ana_[1-5]/ana_3.png)
   
3. Based on the same reason, filter the data with **FULL TIME** positions.
4. according to Zipf's law that 20% always contributes 80%. Locate the dataframe into top 20% of cities and top 20% of the occupations(SOC_NAME).
5. Please refer to file _ana\_3.csv_ in folder **final/analysis/ana[1-5]/**. This is also a big file more than 100 MB, uploaded by git LFS.


## Analysis 4： Find out the average of top five state by year
1. Convert **PREVILILNG_WAGE** to float format.
2. Group data by **YEAR** and **STATE**. The following line chart demonstrates the trend from 2011 to 2016.
3. Please refer to file _ana\_4.csv_ in folder **final/analysis/ana[1-5]/**.

 !['data_wage'](/final/analysis/ana_[1-5]/ana_4.png)
 
### Conclusion
For the 5 years, the **average wage** for H1-B visa is increasing in general, which is absolutely a double-side sword to foreign candidates. It is no doubt that it is a good news to have more handsome salaries, as long as have a job first!


## Analysis 5: Analysis of top 10 employers ,top 20 job titles and the relation with average wages.
1. Select top 10 employers. Please refer to file _ana\_5\_1.csv_ in folder **final/analysis/ana[1-5]/**.

!['top_employer'](/final/analysis/ana_[1-5]/ana_5_1.png)
 
2. Select top 20 job titles base on the top 10 employers.
3. Calculate the average wage of the top 20 job titles.Please refer to file _ana\_5\_2.csv_ in folder **final/analysis/ana[1-5]/**.

!['job_wage'](/final/analysis/ana_[1-5]/ana_5_2.png)

### Conclusion
As we can see here, the good new is that for all these years most of those companies and jobs are about IT tecnologies, but obviously there is a decrease in 2016. Since the new policies came out, the decrease trend may continue. Recently, the Infosys, the leading H1-B sponsorship company has announced that they will no longer apply H1-B visa for engineers less than 4-year working experince, which is so frustrated for every new graduate engineer. But stay positive, at least, we are at the right track!



