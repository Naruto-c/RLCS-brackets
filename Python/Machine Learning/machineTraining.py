import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from category_encoders import OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score

le = preprocessing.LabelEncoder()
forest_clf = RandomForestClassifier(random_state=22)
RLCS_Data = pd.read_csv(
    "/Users/ianlai/Downloads/Repo gitkraken/RLCS-Brackets/Python/AccessData/Teams.csv")

model = make_pipeline(
    OrdinalEncoder(),
    SimpleImputer(),
    RandomForestClassifier()
)
X = RLCS_Data['Played']
y = RLCS_Data['Win %']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2)
model.fit(X_train, y_train)
print('THE BASELINE ACCURACY IS: {}'.format(
    y_train.value_counts(normalize=True).max()))

x = accuracy_score(model.predict(X_test), y_test)

print('FOREST MODEL ACCURACY: {}'.format(x))
