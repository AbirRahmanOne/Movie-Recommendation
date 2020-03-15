# Movie Recommendation #
## This is a Django based [Web App](https://prince004.pythonanywhere.com/) for finding similar Movies or Tv Series. ##

### Movie Search ##
* Type the name of a movie in **search bar** & the **search result** consist of:
  * Similar movie **names** ( Similarity found by Genre,Story,Director,Movie Cast )
  * IMDB & Rotten Tomatoes **rating** (If available)
  * **Box office** collections (If available)
  * Official **trailer** link (If available)
  * Movie **genre** (If available)

### Installation: ###
* Clone the repository.
* Run the requirements.txt file.
``` pip install -r requirements.txt```
* Open .env file then perform following instructions:
  * Set **SECRET_KEY** of your project. It is like set your password & it will be anything that you like, but don't share it with other for security purpose.In .env file I already generate a secret key that you can use but changing SECRET_KEY is highly recommendable.
  * To run this project you need 2 api service:
    * [ Tastedive ](https://tastedive.com/) provide similar movie name.
    * [ OMDB Api ](http://www.omdbapi.com/apikey.aspx?__EVENTTARGET=freeAcct&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKLTIwNDY4MTIzNQ9kFgYCAQ9kFgICBw8WAh4HVmlzaWJsZWhkAgIPFgIfAGhkAgMPFgIfAGhkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQtwYXRyZW9uQWNjdAUIZnJlZUFjY3QFCGZyZWVBY2N0x0euvR%2FzVv1jLU3mGetH4R3kWtYKWACCaYcfoP1IY8g%3D&__VIEWSTATEGENERATOR=5E550F58&__EVENTVALIDATION=%2FwEdAAU5GG7XylwYou%2BzznFv7FbZmSzhXfnlWWVdWIamVouVTzfZJuQDpLVS6HZFWq5fYpioiDjxFjSdCQfbG0SWduXFd8BcWGH1ot0k0SO7CfuulN6vYN8IikxxqwtGWTciOwQ4e4xie4N992dlfbpyqd1D&at=freeAcct&Email=) provide movie detail.
  * Open a free account & apply for api key.
  * Copy & paste the api key in .env file section on a specific variable.(Detail instruction given into .env file)

* Example for **movie** search **Forrest gump**:

![Movie](https://github.com/Mazhar004/movie_recommendation/blob/master/readme_data/Movie.png)
* Example for **tv series** search **Person of interest**:

![Movie](https://github.com/Mazhar004/movie_recommendation/blob/master/readme_data/Tv%20Series.png)


