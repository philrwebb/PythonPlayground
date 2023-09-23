import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data into a DataFrame
df = pd.read_csv('titanic.csv') 

# Calculate survival rate by passenger class
class1_survived = df[df['Pclass'] == 1]['Survived'].mean() 
class2_survived = df[df['Pclass'] == 2]['Survived'].mean()
class3_survived = df[df['Pclass'] == 3]['Survived'].mean()

male_survived = df[df['Sex'] == 'male']['Survived'].mean()
female_survived = df[df['Sex'] == 'female']['Survived'].mean()

# Print survival rates by class  
print(class1_survived)
print(class2_survived) 
print(class3_survived)

print(male_survived)
print(female_survived)

# Create bar chart 
classes = [1, 2, 3]
survival_rates = [class1_survived, class2_survived, class3_survived]

genders = ['male','female']
survival_rates2 = [male_survived, female_survived]

plt.bar(genders, survival_rates2)
plt.xlabel('Gender')
plt.xticks(genders, ['male', 'female'])
plt.ylabel('Survival Rate')
plt.title('Titanic Survival Rate by Gender')
plt.show()

plt.bar(classes, survival_rates)
plt.xlabel('Passenger Class')
plt.xticks(classes, ['First', 'Second', 'Third'])
plt.ylabel('Survival Rate')
plt.title('Titanic Survival Rate by Passenger Class')
plt.show()
