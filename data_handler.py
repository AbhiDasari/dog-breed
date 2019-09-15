import pickle
import pandas as pd
def get_data():
    data_filename="dog_breeds.csv"
    data=pd.read_csv(data_filename)
    breed=data["Breed"].values
    height=data["height_cm"].values
    mass=data["mass_kg"].values
    return breed,height,mass
