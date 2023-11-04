"""import os

path = "notebook/research.ipynb"

dir,file = os.path.split(path)

os.makedirs(dir, exist_ok=True)

with open(file,"w") as f:
    pass"""


from src.DiamondPricePrediction.pipelines.prediction_pipeline import CustomData

CustomDataObject = CustomData(1.52,62.2,58.0,7.27,7.33,4.55,"Premium","F","VS2")

data=CustomDataObject.get_data_as_dataframe()

print(data)