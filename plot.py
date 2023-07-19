import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

for column in columns:
  #print(column)
  sns.countplot(x=column,data=df)
  plt.xticks(rotation=30,fontsize=10)
  plt.xlabel(column,fontsize=12)
  plt.title(column+' Value Counts')
  sns.countplot(df[column],order=df[column].value_counts().index)
  plt.show()
  plt.clf()


Close=0
Crowded=0

for i in df['Gill Spacing']:
  if i == 'Close':
    Close+=1
  else:
    Crowded+=1
#print('Convex :',Convex,' Conical: ',Conical)   
labels = 'Close', 'Crowded'
sizes = [Close,Crowded]


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')  
plt.title("Gill Spacing")

plt.show()
plt.clf()
 
