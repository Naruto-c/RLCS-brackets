import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score


forest_clf = RandomForestClassifier(random_state=22)
RLCS_Data = pd.read_csv("/Desktop/Learning/Teams.csv")

y_gt0 = (y > 0)
cross_val_score(forest_clf, XTrain, y_gt0, cv=3, scoring="accuracy")
