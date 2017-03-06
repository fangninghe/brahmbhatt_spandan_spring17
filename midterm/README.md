# Illustration of midterm project
## Question 1 Enron Email:
### 1. Find who has the most Emails
- First step in detecting Enron Scandel is to search who has the most Emails. Since it is reasonalbe to conclude that people who had the bigger volumn of Emails might involve more in this event. 
- Email amount of the each person was calculated and generated a csv file in **midterm/que[1-2]/ana[1-3]/** named **mail_list.csv**.

### 2. Dig into the most active people
- According to the result in first step, the five most active people and their Email amount is as below:

| Name        | Email Amount  | 
| ------------|:-------------:| 
| kaminski-v      |28465 | 
| dasovich-j      |28234 |   
| kean-s          |25351 |  
| mann-k          |23381 |   
| jones-t         |19950 |  

- Then analysis was performed on the most active years, the result is as below:

 !['Top five Email By Year'](/midterm/que[1-2]/ana[1-3]/Email_Volumn.png)
 
 According to the line chart below, it shows that the most active years are 2000 and 2001. So next step will do rearch on the Email content in those two years.

## 3. Detect Email Content of the top five people
- Get the each person`s Email content of year 2000 and year 2001.
- Remove stop words, punctuation words and useless words like "subject", "to" and "forwarded".
- Generate the wordcloud graphs for each person. The graphs are as below:
  * kaminski's wordcloud graph
  !['kaminski's wordcloud graph'](/midterm/que[1-2]/ana[1-3]/kaminski_words.png)
  * dasovich's wordcloud graph
  !['dasovich's wordcloud graph'](/midterm/que[1-2]/ana[1-3]/dasovich_words.png)
  * kean's wordcloud graph
  !['kean's wordcloud graph'](/midterm/que[1-2]/ana[1-3]/kean_words.png)
  * mann's wordcloud graph
  !['mann's wordcloud graph'](/midterm/que[1-2]/ana[1-3]/mann_words.png)
  * jones's wordcloud graph
  !['jones's wordcloud graph'](/midterm/que[1-2]/ana[1-3]/jones_words.png)
- Generate csv files for each person's top 500 hot words in Email content. Please refer to **midterm/que[1-2]/ana[1-3]/** and review **kaminski-v_word.csv**, **dasovich-j_word.csv**, **kean-s_word.csv**, **mann-k_word.csv** and **jones-t_word.csv**.

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
  
  
  * I also generated a csv file of distribution of material type, please refer to **material_type_distribution.csv** at **midterm/que[1-2]/ana[1-3]/**.
  
  
  * **Analysis two** is to generate a csv file to give a general idea of every artial's rank status at different journals. Please review the **archive_rank_status.csv** at **midterm/que[1-2]/ana[1-3]/**.
- One analysis is performed on Community API
  * Community API is getting access to comments from registered users on New York Times articals.
  * For my project, since the data size and project complexity requirement, I downloaded 2016 year data, one json file for one day,so 366 files in total. Please review data at **midterm/data/user_content/**.
  * **Anaylsis three** is to test Zipf's Law. Here is attached a log-log plot between user comments rank and user comments amount.
  
  
   !['Zipf's Law'](/midterm/que[1-2]/ana[1-3]/Zipf`s_Law.png)
   
### **According to the plot, we can conclude that 20% of the users contributed 80% of the comments** Please refer to user_content_zipf's.csv file at **midterm/que[1-2]/ana[1-3]/**.



