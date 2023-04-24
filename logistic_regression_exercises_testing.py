import numpy as np
import pandas as pd
import math

from sklearn.metrics import classification_report, confusion_matrix
import itertools
import numpy as np
import acquire
import prepare
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


def titanic_survived_linear_regression(train, validate, test, list_of_columns, the_C = 1):
    
    logit1 = LogisticRegression(C =the_C, max_iter=1000)
    logit1
    train


    X_train = train.loc[: , list_of_columns]
    y_train = train.survived


    X_validate = validate.loc[: , list_of_columns]
    y_validate = validate.survived

    X_test = test.loc[: , list_of_columns]
    y_test = test.survived

    logit1.fit(X_train, y_train)


    train_score = logit1.score(X_train, y_train)

    validate_score = logit1.score(X_validate, y_validate)

    test_score = logit1.score(X_test, y_test)
    
    return train_score, validate_score, test_score

dict_for_dataframe = {}

df = acquire.get_titanic_data()
df = prepare.prep_titanic(df)

df['age'] = df['age'].replace(np.nan,0)



train, validate, test = prepare.split_data(df, 'survived')
list_of_columns = train.columns

the_c_list = [.01, .1, 1, 10, 100, 1000]
train_list = []
validate_list = []
features= []
for c_value in the_c_list:
    for num_cols in range(2, len(list_of_columns)+1):
        
        for i in itertools.combinations(list_of_columns, num_cols):
            print(i)
            train_score, validate_score, test_score = titanic_survived_linear_regression(train, validate, test, i, the_C = c_value)
            train_list.append(train_score)
            validate_list.append(validate_score)
            features.append(i)


the_dataframe = pd.DataFrame({'train':train_list,
             'validate':validate_list,
             'features':features
             }
             )

the_dataframe['difference'] = abs(the_dataframe.train - the_dataframe.validate)
the_dataframe = the_dataframe.sort_values(by='difference')

print(the_dataframe[the_dataframe.difference > 0])

plt.plot(range(0, len(the_dataframe.train)), the_dataframe.train)
plt.show()