import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
from pandas import value_counts
import statistics as st

# -------------Ques1. Concatenate Multiple CSV Files Into a single Pandas dataframe---------------------------


# data0 = pd.read_csv("E:\Libraries _in_python\Core_libraries_in_python\data\MFG10YearTerminationData.csv")
# data1 = pd.read_csv("E:\Libraries _in_python\Core_libraries_in_python\data\MFG10YearTerminationData 2.csv")
# data = pd.concat([data0, data1])

# ----------------------command for writing the concatenated file to excel-------------------------------------
# data.to_excel("data.xlsx")

# --------------------------------------print top 5 rows--------------------------------------------------------
# print(data.head(5))

# -------------Ques2. Plot various types of graph using visualization libraries like Matplotlib----------------

# -------------------total count of male and female employee in an organization using count plot---------------
# sns.countplot(x="gender_full", data=data)
# plt.title("The total count of Male & Female Employees")
# plt.show()

# ------------------------to get the length of service  of all department using barplot----------------------
# plt.rcParams.update({'font.size': 5})
# sns.barplot(x='length_of_service', y='department_name', data=data,
#             dodge=True)
# plt.title("length of service  of all department")
# plt.ylabel("department_name")
# plt.xlabel("length_of_service")
# plt.show()

# ------------------Display the avg range of age of employee from various cities using boxplot--------

# plt.rcParams.update({'font.size': 5})
# sns.boxplot(x='age', y='city_name', data=data)
# plt.title("Display the avg range of age of employee from various cities")
# plt.ylabel("City")
# plt.xlabel("Age")
# plt.show()

# --------------Displaying the length of service of various departments in both Business units using bar plot--

# plt.rcParams.update({'font.size': 10})
# sns.barplot(x='length_of_service',
#             y='department_name',
#             hue='BUSINESS_UNIT',
#             data=data)
# plt.title("The length of service of various departments of all Business units")
# plt.ylabel("Department_name")
# plt.xlabel("length_of_service")
# plt.show()

# ----------------------------------The total Employee of an Organization--------------------------------------
# data.dropna(subset=['BUSINESS_UNIT'])
# data_pie = data["BUSINESS_UNIT"].value_counts().rename_axis("BUSINESS_UNIT").reset_index(name="employee_count")
# plt.figure(figsize=(7, 7))
# plt.pie(data_pie.employee_count, labels=data_pie.BUSINESS_UNIT, explode=(0, 0.1), shadow=True, startangle=90,
#         autopct="%1.1f%%")
# plt.title("The total Employee of an Organization")
# plt.show()

# -------------------------------The total Sex Ratio Employee of an Organization-----------------------------
# plt.rcParams.update({'font.size': 30})
# data.dropna(subset=['gender_full'])
# data_pie = data["gender_full"].value_counts().rename_axis("gender_full").reset_index(name="employee_count")
# plt.figure(figsize=(10, 10))
# plt.pie(data_pie.employee_count, labels=data_pie.gender_full, shadow=True, startangle=90,
#         autopct="%1.1f%%")
# plt.title("The Sex Ratio of Employee in Organization")
# plt.show()


# ------------- bar graph for calculating the male and female ratio in an organisation-----------------

# x=data["gender_full"]
# y=data["age"]
# plt.xlabel("gender_full")
# plt.ylabel("age")
# plt.title("The Gender ratio of Employees Working in Organization ")
# plt.bar(x, y)
# plt.show()


# --------------------------Ques3. Determine High or Low Feature Variability in the dataframe-------------

x = data["STATUS_YEAR"]
# -----------------------calculating the standard deviation-------------------
sd = st.pstdev(x)
# -------------------calculating variance using statistics -------------
v = st.pvariance(x)
# ---------------------calculating mean using statistics------------------
# m = st.mean(x)
# print("standard Deviation:" + str(sd))
# print("variance" + str(v))
# print("mean" + str(m))
# sdx = tuple(x - m for x in x)
# print("standard Deviation:" + str(sd))
# varx = tuple(x * x for x in sdx)
# print("variance" + str(v))
# plt.rcParams.update({'font.size': 10})
# plt.bar(tuple(str(x) for x in x), sdx)
# plt.title("Determining Feature Variability ")
# plt.xlabel("STATUS_YEAR")
# plt.show()

# ---------------------------Ques4. Search duplicate records in the dataframe--------------------------
# --------------------------------check ach row for duplicate values-----------------------------------
# print(data.duplicated())
# ---------------------------------check single column for duplicate values----------------------------
# print(data[data["EmployeeID"].duplicated()].head(5))
# --------------------------------Total no. of Rows present in the entire column-----------------------
# print(data["EmployeeID"].shape)


# ----------------------------Ques5. Examine Cardinality in the dataframe--------------------------------

# ------------------------prints the data type of each column of the csv file----------------------------
# print(data.dtypes)
# ------------------------Graph to display cardinality of data  type as integer  ------------------------
# plt.rcParams.update({'font.size': 5})
# data_int = data.select_dtypes(include="int64")
# print(data_int.head())
# data_int.nunique().plot.bar(figsize=(12, 6))
# plt.title("cardinality check")
# plt.ylabel("number of unique categories")
# plt.xlabel("variables")
# print(data_int.nunique())
# plt.show()

# --------------------------Graph to display cardinality of data  type as object--------------------------
# plt.rcParams.update({'font.size': 5})
# data_obj = data.select_dtypes(include="object")
# print(data_obj.head())
# data_obj.nunique().plot.bar(figsize=(12, 6))
# plt.title("cardinality check")
# plt.ylabel("number of unique categories")
# plt.xlabel("variables")
# print(data_obj.nunique())
# plt.show()
