from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
import pickle

input_file = "./trips/sample_trips.csv"

df = pd.read_csv(input_file, header=0)
df = df.loc[(df["total_amount"] < 20) & (df["trip_distance"] < 100)]

distance = df["trip_distance"]
hours = df["tpep_pickup_datetime"].apply(lambda x : datetime.strptime(x, "%Y-%m-%d %H:%M:%S").hour)

data = pd.concat([hours, distance], axis = 1)

target = df["total_amount"]

train_x, test_x, train_y, test_y = train_test_split(
    data,
    target,
    test_size = 0.2,
    random_state = 24
)

lr = LinearRegression()
lr.fit(train_x, train_y)

prediction = lr.predict(test_x)

with open("model.pkl", "wb") as f:
    pickle.dump(lr, f)