import pandas as pd
df1=pd.read_csv('titanic (1).csv')
# Show the first 10 rows of the dataset.
# td2=df1.head(10)


# What are the column names, shape, and datatypes of the dataset?
# td2=df1.info()
# print(td2)


# survived_not=df1.groupby("Survived").size()
# print(survived_not)

# survived_per=(df1['Survived'].mean()) *100
# print(survived_per)


# avg_age=(df1["Age"].mean())
# print(avg_age)

# fare_max=(df1["Fare"].max())
# print(fare_max)

# fare_min=(df1["Fare"].min())
# print(fare_min)



# pass_gen=df1.groupby("Sex").size()
# print(pass_gen)


# pass_embark=df1.groupby("Embarked").size()
# print(pass_embark)

# pclass_count=df1["Pclass"].value_counts()
# print(pclass_count)


# avg_agesurvi_not=df1.groupby("Survived")["Age"].mean()
# print(avg_agesurvi_not)


# survivalrate_bygen=df1.groupby("Sex")["Survived"].mean() *100
# print(survivalrate_bygen)


# survivalrate_bypclass=df1.groupby("Pclass")["Survived"].mean() *100
# print(survivalrate_bypclass)


# farepaidby_eachcls=df1.groupby("Pclass")["Fare"].mean()
# print(farepaidby_eachcls)

# df1['AgeGroup'] = pd.cut(df1['Age'], bins=[0, 12, 18, 35, 60, 100],
#                         labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])

# survival_agegroup=df1.groupby("AgeGroup")["Survived"].mean() *100
# print(survival_agegroup)


# sibsp_alone=df1["SibSp"].value_counts()
# print(sibsp_alone)


# find the most common passenger age.
# freq_age=df1["Age"].mode()
# print(freq_age)

# What is the average fare paid by survivors vs non-survivors?
# avg_faresurvi_not=df1.groupby("Survived")["Fare"].mean()
# print(avg_faresurvi_not)


# Create a new column "family_size" = sibsp + parch + 1.

# add_col=df1["family_size"] =df1["SibSp"]+df1["Parch"]+1
# print(add_col)

