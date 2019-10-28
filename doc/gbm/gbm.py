import sys
import scipy as sp
import matplotlib
import seaborn as sns
import sklearn as sk
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
import keras
from keras.preprocessing import image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tqdm import tqdm


train = pd.read_csv('train_set/label.csv') 
print(train.head())
print(train.columns)

train_image = []
for i in tqdm(range(train.shape[0])):
    img = image.load_img('train_set/images/' + str(train['Index'][i]).zfill(4) +'.jpg',target_size=(400,400,3))
    img = image.img_to_array(img)
    img = img/255
    train_image.append(img)
X = np.array(train_image)
X = X.reshape(2500, 480000) 
#print(X.shape)
#plt.imshow(X[1000])

#elim = [2]
#y = np.array(train.drop([0, 1, 2], axis = 1))
#y = np.delete(train, elim)
#y = train['emotion_idx']

trainarr = np.array(train)
y = np.delete(trainarr, [0,1,2,4,5], axis=1)
#print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

gbm = GradientBoostingClassifier(learning_rate=0.1, n_estimators=100,max_depth=3, min_samples_split=2, min_samples_leaf=1, subsample=1,max_features='sqrt', random_state=10)
#baseline.fit(X_train,y_train.ravel())
gbm.fit(X_train,y_train)
print('Accuracy of the GBM on test set: {:.3f}'.format(gbm.score(X_test, y_test)))
pred=gbm.predict(X_test)
print(classification_report(y_test, pred))