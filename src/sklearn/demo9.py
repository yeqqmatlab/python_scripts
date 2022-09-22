# import package
import pandas as pd
from sklearn.datasets import load_iris
from sklearn2pmml.pipeline import PMMLPipeline
from sklearn2pmml import sklearn2pmml
from sklearn.linear_model import LogisticRegression
import numpy as np

# generate dataset
data = load_iris()
x = pd.DataFrame(data.data, columns=['slength', 'swidth', 'plength', 'pwidth'])
y = pd.DataFrame(data.target, columns=['y'])

# create pipeline and train
lr = LogisticRegression()
pipeline = PMMLPipeline([('lr', lr)])
pipeline.fit(X=x, y=np.ravel(y))
pipeline.verify(x.sample(n=15))

# export to pmml file
sklearn2pmml(pipeline, 'testpmml.pmml', with_repr=True)
