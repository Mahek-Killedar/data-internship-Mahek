
# 1. Calculator
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Addition =", num1 + num2)
elif choice == 2:
    print("Subtraction =", num1 - num2)
elif choice == 3:
    print("Multiplication =", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")

# 2. Even/odd number 
num = int(input("Enter Number: "))
if num%2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# 3. Positive/negative number  
num = int(input("Enter a number:"))
if num >=0:
    print("This number is positive")
else:
    print("This number is negative")

# 4. Largest of 3 numbers  
a=int(input("Enter Number: "))
b=int(input("Enter Number: "))
c=int(input("Enter Number: "))
if a>b and a>c:
  print(a,"is largest")
elif b>c:
  print(b,"is largest")
else:
  print(c,"is largest")

# 5. Student grade calculator  
marks=int(input("Enter Marks:"))
if marks>=90 and marks<=100:
  print("Grade A")
elif marks>=70 and marks<90:
  print("Grade B")
elif marks>=60 and marks<70:
  print("Grade C")
elif marks>=35 and marks<60:
  print("Grade D")
else:
  print("Fail")

# 6. Multiplication table 
num=int(input("Enter Number: "))
for i in range(1,11):
      print(num,"X",i,num*i)

# 7. Factorial  
fact=1
n=int(input("Enter a number:"))
for i in range(1,n+1):
    fact*=i
print(fact)

# 8. Fibonacci series 
a=0
b=1
print(a)
print(b)
for i in range(2,11):
    c=a+b
    a=b
    b=c
    print(c) 

# 9. Count vowels 
a=str(input("Enter String: "))
vowels=0
for i in a:
    if i =="a" or i =="e" or i =="i" or i == "o" or i =="u"or i =="A"or i =="E"or i =="I"or i =="O"or i =="U":
        vowels+=1
print("vowels count",vowels)
 
# 10. Reverse a string  
a=str(input("Enter String: "))
print(a[::-1])
"""
# Functions in Python (Basic)
"""
def calculate_average(a, b, c):
    avg = (a + b + c) / 3
    return avg

def calculate_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def calculate_min(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

def calculate_percentage(total):
    percentage = (total / 300) * 100
    return percentage

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

# Main Program

print("Student Result Calculator")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3

average = calculate_average(m1, m2, m3)
highest = calculate_max(m1, m2, m3)
lowest = calculate_min(m1, m2, m3)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)

print("\n----- Result -----")
print("Total Marks :", total)
print("Average :", average)
print("Highest Marks :", highest)
print("Lowest Marks :", lowest)
print("Percentage :", percentage)
print("Grade :", grade)

import numpy as np

# 1D Array (Sales Data)
sales = np.array([1200, 1500, 1800, 2000, 1700])

print("Sales Data:", sales)

# Sales Calculations
print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Maximum Sales:", np.max(sales))
print("Minimum Sales:", np.min(sales))
print("Standard Deviation:", np.std(sales))
print("Median:", np.median(sales))
print("25th Percentile:", np.percentile(sales, 25))
print("75th Percentile:", np.percentile(sales, 75))

# 2D Array
array2d = np.array([[1, 2, 3],
                    [4, 5, 6]])

print("\n2D Array:")
print(array2d)

# Reshaping
reshape_array = np.arange(1, 13).reshape(3, 4)

print("\nReshaped Array:")
print(reshape_array)

# Matrix Multiplication
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = np.matmul(A, B)

print("\nMatrix Multiplication:")
print(C)

import pandas as pd  # type: ignore[import-not-found]

# 1. Load dataset
df = pd.read_csv("sales_data.csv")

# 2. Display first 10 rows
print("First 10 Rows")
print(df.head(10))

# 3. Display last 10 rows
print("\nLast 10 Rows")
print(df.tail(10))

# 4. Find number of rows
print("\nNumber of Rows:", df.shape[0])

# 5. Find number of columns
print("Number of Columns:", df.shape[1])

# 6. Check data types
print("\nData Types")
print(df.dtypes)

# 7. Find missing values
print("\nMissing Values")
print(df.isnull().sum())

# 8. Generate summary statistics
print("\nSummary Statistics")
print(df.describe())
"""
"""
#Day 6 

import pandas as pd  

df = pd.read_csv("dirty_employee_data.csv")
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
df["Age"] = df["Age"].astype(str).str.replace(r"[^0-9]", "", regex=True)
df["Age"] = df["Age"].replace("", pd.NA)
df["Age"] = df["Age"].astype(float)
df["Salary"] = df["Salary"].astype(str).str.replace(r"[^\d.\-]", "", regex=True)
df["Salary"] = df["Salary"].replace("", pd.NA)
df["Salary"] = df["Salary"].astype(float)
df["Department"] = df["Department"].str.strip().str.lower()
df["Country"] = df["Country"].str.strip().str.lower()
country_map = {
    "usa": "USA",
    "united states": "USA",
    "india": "India",
}
df["Country"] = df["Country"].map(country_map)
df = df.drop_duplicates(subset=["Name", "Email"], keep="first")
# A number column: fill gaps with the median (the "typical" middle value)
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# A text column where guessing a value is misleading: use a clear placeholder
df["Email"] = df["Email"].fillna("unknown@company.com")
age_outliers = df[(df["Age"] < 18) | (df["Age"] > 65)]
salary_outliers = df[(df["Salary"] < 0) | (df["Salary"] > 500000)]

print(age_outliers[["EmployeeID", "Name", "Age"]])
print(salary_outliers[["EmployeeID", "Name", "Salary"]])
valid_median_age = df.loc[(df["Age"] >= 18) & (df["Age"] <= 65), "Age"].median()
df.loc[(df["Age"] < 18) | (df["Age"] > 65), "Age"] = valid_median_age
df.to_csv("cleaned_employee_data.csv", index=False)
"""
"""
#Day 9
import pandas as pd
import numpy as np

data = {
    "Hours_Studied":[1,2,3,4,5,6,7,8,9,10],
    "Marks":[35,40,50,55,65,70,75,85,90,95]
}

df = pd.DataFrame(data)
df
mean = df["Marks"].mean()

median = df["Marks"].median()

mode = df["Marks"].mode()

range_value = df["Marks"].max() - df["Marks"].min()

variance = df["Marks"].var()

std = df["Marks"].std()

q1 = df["Marks"].quantile(0.25)

q2 = df["Marks"].quantile(0.50)

q3 = df["Marks"].quantile(0.75)

iqr = q3 - q1

p90 = df["Marks"].quantile(0.90)

correlation = df["Hours_Studied"].corr(df["Marks"])

covariance = df["Hours_Studied"].cov(df["Marks"])

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode.values)
print("Range:", range_value)
print("Variance:", variance)
print("Standard Deviation:", std)
print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("IQR:", iqr)
print("90th Percentile:", p90)
print("Correlation:", correlation)
print("Covariance:", covariance)
"""
"""
#Day 10
import pandas as pd
import numpy as np
from scipy.stats import binom, norm

data = {
    "Student":["A","B","C","D","E","F","G","H","I","J"],
    "Gender":["F","M","F","M","F","M","F","M","F","M"],
    "Hours":[2,3,4,5,6,4,7,8,9,10],
    "Attendance":[75,80,82,85,88,78,90,92,95,97],
    "Marks":[45,52,60,66,72,58,80,86,91,96],
    "Department":["CSE","IT","CSE","ECE","CSE","IT","CSE","ECE","CSE","IT"]
}

df = pd.DataFrame(data)
df
# 1. Probability of Female
female = len(df[df["Gender"]=="F"])
total = len(df)

print(female/total)

# 2. Conditional Probability
cse = df[df["Department"]=="CSE"]
female_cse = len(cse[cse["Gender"]=="F"])

print(female_cse/len(cse))

# 3. Independent Event
coin = 1/2
dice = 1/6

print(coin*dice)

# 4. Binomial Distribution
from scipy.stats import binom

print(binom.pmf(3,5,0.5))

print(binom.pmf(3,5,0.5))

# 5. Normal Distribution
mean = 70
std = 10
score = 91

z = (score-mean)/std
print(z)

"""

#Day 11
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Gender": ["F", "M", "F", "M", "F", "M", "F", "M", "F", "M"],
    "Hours": [2, 3, 4, 5, 6, 4, 7, 8, 9, 10],
    "Attendance": [75, 80, 82, 85, 88, 78, 90, 92, 95, 97],
    "Marks": [45, 52, 60, 66, 72, 58, 80, 86, 91, 96],
    "Department": ["CSE", "IT", "CSE", "ECE", "CSE", "IT", "CSE", "ECE", "CSE", "IT"]
}

df = pd.DataFrame(data)

print(df)
# 1. Line Chart
plt.figure(figsize=(6,4))
plt.plot(df["Hours"],df["Marks"],marker="o")
plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.grid()
plt.show()


# 2. Bar Chart
dept = df.groupby("Department")["Marks"].mean()

plt.bar(dept.index,dept.values)
plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.show()

# 3. Histogram
plt.hist(df["Marks"],bins=5)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot
plt.scatter(df["Attendance"],df["Marks"])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.show()

# 5. Pie Chart
gender = df["Gender"].value_counts()

plt.pie(gender.values,
        labels=gender.index,
        autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.show()

# 6. Box Plot
plt.boxplot(df["Marks"])
plt.title("Marks Boxplot")
plt.ylabel("Marks")
plt.show()

#7. Area Chart
plt.fill_between(df["Hours"],df["Marks"],alpha=0.5)
plt.title("Area Chart: Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()

# 8. Horizontal Bar Chart
plt.barh(df["Student"],df["Marks"])
plt.title("Marks of Students")
plt.xlabel("Marks")
plt.ylabel("Student")
plt.show()

# 9. Multiple Line Chart
plt.plot(df["Student"],df["Marks"],label="Marks")
plt.plot(df["Student"],df["Attendance"],label="Attendance")

plt.title("Marks & Attendance")
plt.xlabel("Student")
plt.ylabel("Value")
plt.legend()
plt.show()

# 10. Stem Plot
plt.stem(df["Hours"],df["Marks"])
plt.title("Stem Plot")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()

"""
#Day 12
import pandas as pd
import numpy as np
from scipy.stats import binom, norm

data = {
    "Student":["A","B","C","D","E","F","G","H","I","J"],
    "Gender":["F","M","F","M","F","M","F","M","F","M"],
    "Hours":[2,3,4,5,6,4,7,8,9,10],
    "Attendance":[75,80,82,85,88,78,90,92,95,97],
    "Marks":[45,52,60,66,72,58,80,86,91,96],
    "Department":["CSE","IT","CSE","ECE","CSE","IT","CSE","ECE","CSE","IT"]
}

df = pd.DataFrame(data)
df
import seaborn as sns
import matplotlib.pyplot as plt
# 1. Distribution Analysis
sns.histplot(df["Marks"],kde=True)
plt.title("Distribution of Marks")
plt.show()
# 2. Countplot (Category Analysis)
sns.countplot(x="Department",data=df)
plt.title("Students per Department")
plt.show()
# 3. Boxplot (Outlier Analysis)
sns.boxplot(y="Marks",data=df)
plt.title("Marks Boxplot")
plt.show()
# 4. Violin Plot
sns.violinplot(x="Gender",y="Marks",data=df)
plt.title("Marks by Gender")
plt.show()
# 5. Correlation Heatmap
corr = df[["Hours","Attendance","Marks"]].corr()

sns.heatmap(corr,
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
# 6. Pairplot
sns.pairplot(df[["Hours","Attendance","Marks"]])
plt.show()
"""
