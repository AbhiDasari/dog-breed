import numpy as np
import data_handler as dta
import fitter as fit

def get_similar_breeds(target_breed):
    body_size,build,breed=calculate_build_data()
    i_target=np.where(breed==target_breed)[0][0]
    target_size=body_size[i_target]
    build_threshold=0.5
    i_lanky=np.where(build<-build_threshold)[0]
    i_stocky=np.where(build>build_threshold)[0]
    i_medium=np.where(np.logical_and(build>=-build_threshold,build<=build_threshold))[0]
    size_distance=np.abs(body_size-target_size)
    size_distance[i_target]=1e4

    n_results=5
    i_stocky_results=np.argsort(size_distance[i_stocky])[:n_results]
    i_medium_results=np.argsort(size_distance[i_medium])[:n_results]
    i_lanky_results=np.argsort(size_distance[i_lanky])[:n_results]
    
    stocky_results=breed[i_stocky][i_stocky_results]
    medium_results=breed[i_medium][i_medium_results]
    lanky_results=breed[i_lanky][i_lanky_results]

    return stocky_results,medium_results,lanky_results
def calculate_build_data():
    breed,height,mass=dta.get_data()
    model,params=fit.fit_curve(height,mass)
    height_curve,mass_curve=model.to_points(params, heigth)
    height_scale=np.var(height)
    mass_scale=np.var(mass)
    d_path=np.sqrt((np.diif(height_curve)**2)/height_scale+(np.diff(maas_curve)**2)/mass_scale)
    path_position=np.cumsum(d_path)
    distance, size_indices=fit.distance_to_curve(height,mass,height_curve,mass_curve)
    body_size=path_position[size_indeces-1]
    build=10*distance/np.sqrt(body_size)
    estimated_mass=model.evaluate(params,height)
    i_negative=np.where(mass<estimated_mass)[0]
    build[i_negative]=-build[i_negative]
    return body_size,build,breed

    
