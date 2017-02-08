import requests

def temperature():
	#getting input from user
	city = input("Enter City: ")
	#making an API call to openweathermap
	r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=402c7b6d34f8b5e233a424147c2953bf")
	json_obj = r.json() #retrieving JSON data and saving to json_obj
	#to check for unavailable data
    #if json_obj == None:
    #    print("Oops! We don't know this city!")
    #else:
	temp_k = float(json_obj['main']['temp']) #parsing json 
	temp_c = temp_k - 273.15 #converting temperature to Celcius
	print ("The current temperature is: "+ str(temp_c) + "C")


def main():
	temperature()

if __name__ == '__main__':
	main()
