Using the Open Weather Map API, this program checks to see if rain is in the forecast within the next 12 hours from when 
the program is run. If rain is in the forecast, Twilio would text me that it would rain that day, and to bring an 
umbrella. Here's an example of the text you'd get:

![alt text](https://raw.githubusercontent.com/SauerVonKraut/Rain_Alert/main/Screen%20Shot%202021-12-13%20at%201.40.34%20PM.png)

The API is checking the weather based on my latitude and longitude (right now it reads the coordinates for Buffalo, NY),
and one could plug in their own city's coordinates to use it wherever.

To run the program tailored to your locality, you'll need the Open Weather API and a Twilio account to send you messgaes:

https://openweathermap.org/api

https://www.twilio.com/