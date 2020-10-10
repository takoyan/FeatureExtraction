import pickle
import pandas as pd
from sklearn import svm, metrics, preprocessing
from sklearn.model_selection import cross_val_score

def predLabel(file_name):
    datas = pd.read_csv("../features/{}.csv".format(file_name))
    with open('../model/model.pickle', mode='wb') as fp:
        clf=pickle.load(fp)

        y_pred = clf.predict(datas)

        new_df=pd.DataFrame(y_pred, columns=['label'])
        new_df.to_csv('../label/{}.csv'.format(file_name), header=None, index=None)

"""
if __name__=='__main__':
    predLabel('5NM4tiger')
"""