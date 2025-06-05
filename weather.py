import sys
import requests
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QLineEdit, QLabel, QVBoxLayout, QWidget,)
from PyQt5.QtCore import Qt
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:" , self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel( self)
        self.emoji_label = QLabel( self)
        self.description_label = QLabel( self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 300)
        #  vertical layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)
        # align center

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter )
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
    #     styling the button

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        
        self.setStyleSheet("""
             QLabel,QPushButton {
                 font-family: Arial, sans-serif;           
             }
              QLabel#city_label {
                 font-weight: bold;
                 font-size: 40px;
                 font-style: italic;
                 color: #333;    
                 font-style: capitalize;                          
             }                   
              QLineEdit#city_input {
                font-size: 40px;                        
             }                  
               QPushButton#get_weather_button {
               font-size: 20px;
                font-weight: bold;
                                                      
             }
             QLabel#temperature_label{
                           font-size: 70px;

                           }     
              QLabel#emoji_label {
                           font-size: 80px;
                           font-family: Segoe UI Emoji;
                           }                      
              QLabel#description_label {
                           font-size: 30px;
                           color: #555;
                           font-style: italic;
                           }
""")

        self.get_weather_button.clicked.connect(self.get_weather)


    def get_weather(self):
        api_key = "b60c93304ca2691ed8e2e8d7cb27e4bd" 
        city = self.city_input.text()
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" 
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["cod"] == 200:
                self.display_weather(data)
            else:
                self.display_error(data.get("message", "Error fetching weather data.")) 
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 404:
                    self.display_error("City not found. Please enter a valid city name.")
                case 401:
                    self.display_error("Invalid API key. Please check your API key.")
                case 400:
                    self.display_error("Bad request. Please check the city name.")
                case 500:
                    self.display_error("Internal server error. Please try again later.")
                case 403:
                    self.display_error("Invalid API key. Please check your API key.")
                case 502:
                    self.display_error("Bad gateway. Please try again later.")
                case 503:
                    self.display_error("Service unavailable. Please try again later.")
                case 504:
                    self.display_error("Gateway timeout. Please try again later.")
                case _:
                    self.display_error(f"HTTP error: {response.status_code}")

        except requests.exceptions.RequestException:
            self.display_error("Network error. Please check your internet connection.")

    def display_error(self,message):
        self.temperature_label.setText(message)
        self.temperature_label.setStyleSheet("color: red; font-size: 30px;")

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("color: black; font-size: 70px;")
        tempracher = data["main"]["temp"]
        tempracher_c = tempracher - 273.15
        print(tempracher_c)
        self.temperature_label.setText(f"{tempracher_c:.0f} °C")

        description = data["weather"][0]["description"].title()
        self.description_label.setText(description)

        icon = data["weather"][0]["main"]
        emoji = {
            "Clear": "☀️",
            "Clouds": "☁️",
            "Rain": "🌧️",
            "Drizzle": "🌦️",
            "Thunderstorm": "⛈️",
            "Snow": "❄️",
            "Mist": "🌫️"
        }.get(icon, "🌡️") 

        self.emoji_label.setText(emoji)
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
