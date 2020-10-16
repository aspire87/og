import time
import pickle
import datetime
state_dict={}
nowdate = datetime.datetime.today().strftime("%d-%m-%Y")
lines = [["4", "5", "6"]]
with open(nowdate, "wb") as file:
    state_dict[nowdate]=lines
    pickle.dump(state_dict, file)
with open(nowdate, "rb") as fl:
    d_in = pickle.load(fl)
value=d_in[nowdate]
value.append(дшы)
with open(nowdate, "wb") as file:
    state_dict[nowdate]=value
    pickle.dump(state_dict, file)
with open(nowdate, "rb") as fl:
    d_in = pickle.load(fl)
print(d_in)
