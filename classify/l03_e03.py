from sklearn import datasets, model_selection, metrics, svm

from sklearn.naive_bayes import GaussianNB

from sklearn.neighbors import KNeighborsClassifier

import matplotlib.pyplot as pp

import seaborn as sn

# Load Iris dataset

iris = datasets.load_iris()

# Train / test split

x_train, x_test, y_train, y_test = model_selection.train_test_split(
    iris.data,
    iris.target,
    test_size=0.20
)  # Data (x_train, y_train) | classes (x_test, y_test)

# Models predicted

predicted = {}

# Knn

knn_model = KNeighborsClassifier(n_neighbors=8)

knn_model.fit(x_train, y_train)

predicted.update({'Knn': knn_model.predict(x_test)})

# Bayes

bayes_model = GaussianNB()

bayes_model.fit(x_train, y_train)

predicted.update({'Naive Bayes': bayes_model.predict(x_test)})

# Svm

svm_model = svm.SVC()

svm_model.fit(x_train, y_train)

predicted.update({'Svm': svm_model.predict(x_test)})

# Confusion matrix, report and plots

fig, ax = pp.subplots(1, 3, figsize=(12, 4))

counter = 0

for k, v in predicted.items():
    # Confusion matrix

    confusion = metrics.confusion_matrix(y_test, v)

    print(f'\n {k} | \033[34mConfusion matrix \033[m : \n\n{confusion}')

    sn.heatmap(confusion, annot=True, ax=ax[counter])

    ax[counter].set_title(k)
    
    counter += 1

    # Report

    print(f'\n {k} | \033[34mClassification report\033[m : \n\n{metrics.classification_report(y_test, v)}', end='\n')

pp.show()