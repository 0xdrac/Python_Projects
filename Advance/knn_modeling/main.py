from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

df = pd.read_csv("random_distinct_names.csv")

df["Gender"] = df["Gender"].map({"M": 0, "F": 1})

x = df[["Age", "Gender"]]
y = df["Infected"]

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.01, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

print(classification_report(y_test,y_pred))
print("Accuracy:", accuracy_score(y_test,y_pred))

