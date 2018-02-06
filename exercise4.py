import json, requests

movie = raw_input("Choose the movie you would like:  ");

url = "http://www.omdbapi.com/?t=%s" %movie
print("Url : " +url);
response = requests.get(url)


python_dictionary_values = json.loads(response.text) 
while (python_dictionary_values["Response"] == "False"):
     print("No movie found with name " +movie+ " Please try again ");
     movie =  raw_input("Choose the movie you would like:  ");
     url = "http://www.omdbapi.com/?t=%s" %movie
     response = requests.get(url)
     python_dictionary_values = json.loads(response.text);
#print python_dictionary_values;


print("Movie Name : " +movie+ "");
print ("Movie Rating : "+python_dictionary_values["imdbRating"]);
print("Awards and Nominations : "+python_dictionary_values["Awards"]);
