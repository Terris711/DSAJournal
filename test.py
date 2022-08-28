import pickle

list = ["a", "b", "c"]

with open("test.pkl", "wb") as f:
    a = pickle.dump(list, f)
    print(a)
f.close()

with open("test.pkl", "rb") as f:
    b = pickle.load(f)
    print(f)
