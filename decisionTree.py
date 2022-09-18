#-------------------------------------------------------------------------
# AUTHOR: Andy Lam
# FILENAME: decisionTree
# SPECIFICATION: Read the file contact_lens.csv and output a decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: About 4 hours
#-----------------------------------------------------------*/
#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
#AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays
#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            db.append (row)
            print(row)
#transform the original categorical training features to numbers and add to the 4D
#array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
for row in db:
    x = []
    for i, value in enumerate(row):
        if i == 0: x.append(1 if value == 'Young' else 2 if value == 'Prepresbyopic' else 3)
        elif i == 1: x.append(1 if value == 'Myope' else 2)
        elif i == 2: x.append(1 if value == 'No' else 2)
        elif i == 3: x.append(1 if value == 'Reduced' else 2)
    X.append(x)

#transfor the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
for row in db:
    Y.append(1 if row[-1] == 'Yes' else 2)

#fiiting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()