# Illustration of midterm project
## Question 1 Enron Email:
---
## Question 2 NYT API:
### 1. Collect data and store data
- Archive API and Community API were chozen to perform analysis on
- Data is stored at **midterm/data/**.

### 2. Data analysis
- Two analysis are performed on Archive API
  * The Archive API provides lists NYT articals by months going back to 1851.
  * For my project, since the data size and project complexity requirement, I downloaded 6-months data(07/2016-16/2016), one json file for one month. Please refer to **midterm/data/archive/** to check the 6 json files.
  * **Analysis one** is to illustrate the **distribution of document type** and **distributrion of material type** of all the articals over 6 months. The result is shown as the graph below:
  
  !['distribution of doctype'](/midterm/que[1-2]/ana[1-3]/document_type.png)
  
  
  !['distribution of materialtype'](/midterm/que[1-2]/ana[1-3]/material_type.png)
  
  
  * I also generate a csv file of distribution of material type, please refer to **material_type_distribution.csv** at **midterm/que[1-2]/ana[1-3]/**.
  
  
  * **Analysis two** is to generate a csv file to give a general idea of every artial's rank status at different journals. Please review the **archive_rank_status.csv** at **midterm/que[1-2]/ana[1-3]/**.
- One analysis is performed on Community API
  * Community API is getting access to comments from registered users on New York Times articals.
  * For my project, since the data size and project complexity requirement, I downloaded 2016 year data, one json file for one day,so 366 files in total. Please review data at **midterm/data/user_content/**.
  * **Anaylsis three** is to test Zipf's Law. Here is attached a log-log plot between user comments rank and user comments amount.
  
  
   !['Zipf's Law'](/midterm/que[1-2]/ana[1-3]/Zipf`s_Law.png)
   
### **According to the plot, we can conclude that 20% of the users contributed 80% of the comments** Please refer to user_content_zipf's.csv file at **midterm/que[1-2]/ana[1-3]/**.
  
  


