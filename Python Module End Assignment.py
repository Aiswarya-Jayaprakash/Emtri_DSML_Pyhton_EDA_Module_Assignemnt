#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from a file
file_name = "E:\\ENTRI DSML\\Python\\module_assign_dataset1.csv"
data = pd.read_csv(file_name)


# In[13]:


# Correct the "height" column by replacing it with random numbers between 150 and 180 
Height = np.random.randint(150,180,size=len(data))
data["Height"]=Height
data.head()

# Display basic information about the dataset
print(data.info())
print(data.head())
print(data.describe())


# In[18]:


#Task 1: Distribution of employees across each team
team_distribution = data['Team'].value_counts()
team_percentage = (team_distribution / len(data)) * 100

print("Team Distribution:\n", team_distribution)
print("\nTeam Percentage:\n", team_percentage)

# Visualization
plt.figure(figsize=(10, 6))
team_distribution.plot(kind='bar', color='orange')
plt.title('Distribution of Employees Across Teams')
plt.xlabel('Team')
plt.ylabel('Number of Employees')
plt.show()


# In[ ]:


#Data story: Plot analysis revealed that"new orlean pelican" team has the highest number of employees which is 19 followed by "Memphis Grizzilies" at 18. Further majority team has 15 employees.


# In[22]:


#Task 2: Segregate employees based on their positions
position_distribution = data['Position'].value_counts()

print("Position Distribution:\n", position_distribution)

# Visualization
plt.figure(figsize=(12, 8))
position_distribution.plot(kind='bar', color='skyblue')
plt.title('Distribution of Employees Based on Positions')
plt.xlabel('Position')
plt.ylabel('Number of Employees')
plt.show()


# In[ ]:


#Data story:  The bar plot showed that more than 100 employees belonged to SG position followed by PF position.


# In[34]:


#Task 3: Identify the predominant age group among employees
data["Age"].unique()


# In[33]:


data["Age"].value_counts()


# In[35]:


data['Age Group'] = data['Age'].apply(lambda age:'20-25' if 20 <= age <= 25 else ('26-30' if 26 <= age <= 30 else ('31-35' if 31 <= age <= 35 else '36 -40')))
data   


# In[43]:


data["Age Group"].value_counts()
plt.figure(figsize=(10,6))
data["Age Group"].value_counts().plot(kind='bar', color='purple')
plt.title('Distribution of Employees by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Employees')
plt.show()


# In[ ]:


#Data story: It is identified that most of the employees age falls within the age of 25, with 42 individuals in this group followed by 41 individuals with the age of 24. The bar plot analysis showed majority of employees about 198 individuals are under the age of 20-25. Apart from this, there are fewer individuals between the age range of 36-40


# In[9]:


#Task 4: Team and position with the highest salary expenditure
total_salary = data.groupby(["Team","Position"])["Salary"].sum()
max_spending = total_salary.idxmax()
max_spending_salary = total_salary.max()
print(f"The team and position with the highest spending is:\n Team: {max_spending[0]}\n position: {max_spending[1]} \n with a total salary of {max_spending_salary}.")

# Visualization
plt.figure(figsize=(20,5))
sns.scatterplot(y = "Salary",x="Team",hue = "Position",data = data)
plt.ylabel("Salary")
plt.xlabel("Team")
plt.title("scatter plot position vs team with salary")
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#Data story: scatter plot analysis revealed that that Los angeles lakers standout as highest spending team when salary distribution was plotted across different positions within each team.


# In[12]:


#Task 5: Correlation between age and salary
# Correlation calculation
correlation = data['Age'].corr(data['Salary'])
print(f"Correlation between age and salary: {correlation}")

# Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Salary', data=data)
plt.title('Correlation between Age and Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()


# In[ ]:


#Data story: The correlation between age and salary: 0.21400941226570974 which is a positive correlation but the correlation values shows a weak relationship between age and salary. This means that as age increases, there's a tendency for salaries to increase slightly.

