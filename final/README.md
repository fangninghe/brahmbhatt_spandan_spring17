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

## Analysis 1： Find the top 10 states with the most HI-B visa opportunities by year
### Data cleaning
1. Delete old index column.
2. Remove rows with nan values.
3. Split **WORKSITE** into **CITY** and **STATE**.

### Group data 
1. Group by **YEAR** and **STATE**.
2. Select the top ten states within each **STATE** group.
3. Please refer to file _ana\_1.csv_ in folder **final/analysis/ana[1-5]/**.
4. The bar charts of each year are as below:

 !['data2011'](/final/analysis/ana_[1-5]/ana_1_2011.png)
 
 !['data2012'](/final/analysis/ana_[1-5]/ana_1_2012.png)
 
 !['data2013'](/final/analysis/ana_[1-5]/ana_1_2013.png)
 
 !['data2014'](/final/analysis/ana_[1-5]/ana_1_2014.png)
 
 !['data2015'](/final/analysis/ana_[1-5]/ana_1_2015.png)
 
 !['data2016'](/final/analysis/ana_[1-5]/ana_1_2016.png)
 
### Conclusion
From the result by year, top 5 states are selected, which are **CALIFORNIA, ILLINOIS, NEW JERSEY, NEW YORK and TEXAS**. Data from those 5 states are selected for the seconde analysis.


## Analysis 2： Find the top 20% cities and top 20% occupations with the most HI-B visa opportunities in total.
1. Select data from top 5 states mentioned in last analysis.
2. Analyze **CASE_STATUS**, as is shown below, **CERTIFIED** data is selected based on 2 reason. One reason is the **CERTIFIED** data makes the most sense for foreign candidates. The other reason is that according to the pie chart, more than 80% of the cases` result is **CERTIFIED**.
 
  !['data_casgstatus'](/final/analysis/ana_[1-5]/ana_2.png)
   
3. Based on the same reason, filter the data with **FULL TIME** positions.
4. according to Zipf's law that 20% always contributes 80%. Locate the dataframe into top 20% of cities and top 20% of the occupations(SOC_NAME).
5. Please refer to file _ana\_2.csv_ in folder **final/analysis/ana[1-5]/**.


