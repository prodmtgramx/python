import pandas as pd
import numpy as np

def get_parking_id(nazwa):
	if nazwa == 'Nowy Targ':
		return 1
	if nazwa == 'Parking Hala Stulecia':
		return 2
	if nazwa == 'ul. \u015bw. Antoniego':
		return 3
	if nazwa == 'Narodowe Forum Muzyki':
		return 4

data = pd.read_csv("data_parking.csv", parse_dates = [1], index_col=0)
data = data.drop(columns="Liczba_Poj_Wjezdzajacych")
data = data.drop(columns="Liczba_Poj_Wyjezdzajacych")
 
data['czas_minuty'] = data['Czas_Rejestracji'].map(lambda x: x.minute + x.hour *60)
#data['Nazwa'] = data['Nazwa'].map(lambda nazwa: get_parking_id(nazwa))
def split_data(input_data):
	name_list=data['Nazwa'].unique()
	result={}
	for value in name_list:
		result[str(value)] =  input_data[input_data["Nazwa"] ==value]
	return result
 
data=split_data(data)
 
def predict(time):
	result={}
	for value in data:
		result[str(value)] = np.zeros(shape=1)
 
	for key,value in data.items():
		result[key]=int((np.poly1d(np.polyfit(value['czas_minuty'],value['Liczba_Wolnych_Miejsc'],4))(time)))
	return result
