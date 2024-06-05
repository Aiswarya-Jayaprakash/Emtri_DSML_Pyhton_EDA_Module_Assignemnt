# Entri_DSML_Pyhton_EDA_Module_Assignemnt
A dataset from ABC company, consisting of 458 rows and 9 columns. The company requires a comprehensive report detailing information about their employees across various teams. Your tasks include preprocessing the dataset, analyzing the data, and presenting your findings graphically. Here's a breakdown of what you need to do:

Preprocessing:
Correct the data in the "height" column by replacing it with random numbers between 150 and 180. Ensure data consistency and integrity before proceeding with analysis. (1 mark)

Analysis Tasks:
1. Determine the distribution of employees across each team and calculate the percentage split relative to the total number of employees. (2 marks)
2. Segregate employees based on their positions within the company. (2 marks)
3. Identify the predominant age group among employees. (2 marks)
4. Discover which team and position have the highest salary expenditure. (2 marks)
5. Investigate if there's any correlation between age and salary, and represent it visually. (2 marks)

Data Preprocessing:
Data preprocessing is done before raw data is entered into an analytical tool. Here the following actions are performed

1:importing required libraries:numpy,pandas,matplotlib,seaborn 
2:Edited column "height" with random numbers within the range of 150 to 180

Team analysis:
1:find number of teamsin which employees exist and count most number of employee belong to which team
2:visualised the team distribution using barplot for meaningful and easiest insight

Data story: Plot analysis revealed that"new orlean pelican" team has the highest number of employees which is 19 followed by "Memphis Grizzilies" at 18. Further majority team has 15 employees.

Position segregation:
1:count number of position present in the dataset and calculate employee count in each position 
2:visualisation of position distribution using barplot for best insight

Data story:  The bar plot showed that more than 100 employees belonged to SG position followed by PF position.

Age Group identification:
1:To identify predominant age group among employees 
2:visualisation of corresponding distribution

Data story: It is identified that most of the employees age falls within the age of 25, with 42 individuals in this group followed by 41 individuals with the age of 24. The bar plot analysis showed majority of employees about 198 individuals are under the age of 20-25. Apart from this, there are fewer individuals between the age range of 36-40

Salary analysis:
1:Determine the team and position of employees with highest salary spending 
2:visualisation salary distribution by using scatterplot

Data story: scatter plot analysis revealed that that Los angeles lakers standout as highest spending team when salary distribution was plotted across different position within each team.

Correlation between Age and SALARY:
1:Analyse the relationship between employees age and their corresponding salaries through correlation method
2:Visulisation of the correlation through  scatter plot

Data story: The correlation between age and salary: 0.21400941226570974 which is a positive correlation but the correlation values shows a weak relationship between age and salary. This means that as age increases, there's a tendency for salaries to increase slightly.

