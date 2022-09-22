import pickle
import Orange
from sklearn2pmml import sklearn2pmml
from sklearn2pmml import PMMLPipeline


with open('random_model.pkcls', 'rb') as model:
    random_model = pickle.load(model)

print(random_model)
print(type(random_model))

data = Orange.data.Table('adult_pre.tab')

print("-------------------")
print(random_model(data))
print("-------------------")










