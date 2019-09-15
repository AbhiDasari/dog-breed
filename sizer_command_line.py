import sys
import numpy as np
import data_handler as dta
import dog_sizer as siz


breed,height,mass=dta.get_data()

if len(sys.argv)<2 or sys.argv[1] not in breed:
    print()
    print("Usage:")
    print("invalid breed")
    print()
    print("some suggestions for you")
    print(" ",",".join(np.random.choice(breed,size=5)))
else:
    stocky, medium, lanky=siz.get_similar_breeds(sys.argv[1])
    print("stocky :",", ".join(stocky))
    print("medium :",", ".join(medium))
    print("lanky :",", ".join(lanky))
