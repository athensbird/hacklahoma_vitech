from __future__ import division
from sklearn import datasets
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split as tts

wine = datasets.load_wine()

features = wine.data
labels = wine.target

train_feats, test_feats, train_labels, test_labels = tts(features, labels, test_size=0.2)

clf = svm.SVC(kernel='linear')

# train
clf.fit(train_feats, train_labels)

# predictions
predictions = clf.predict(test_feats)
print predictions

score = 0
for i in range(len(predictions)):
    if predictions[i] == test_labels[i]:
        score +=1
print score/len(predictions)

# print "Number of entries: ", len(train_feats)
# for featurename in wine.feature_names:
#     print featurename[:10], "    \t",
# print "Class"
# for feature, label in zip(train_feats, train_labels):
#     for f in feature:
#         print f, "\t\t",
#     print label
