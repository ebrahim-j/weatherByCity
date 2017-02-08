def temperature(city):
	city = input("Enter City: ")
	r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=402c7b6d34f8b5e233a424147c2953bf")
	json_obj = r.json()
	temp_k = float(json_obj['main']['temp'] )
	temp_c = temp_k - 273.15
	return str(temp_c)

if __name__ == '__main__':
	main()
