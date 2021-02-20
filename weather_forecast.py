import requests
import datetime

DARKSKY_API_ENDPOINT = 'https://api.darksky.net/forecast/'
DARKSKY_SECRET_KEY = 'daf75c2187a8f88c0f50be1501168d61'


class weatherForecast:
    def __init__(self):
        self.weekly_summary = ""
        self.icon = ""
        self.temperature = ""
        self.daily = ""
        self.daily_data = ""
        self.formatted_address = ""
        self.formatted_date = ""
        self.hourly_data = ""

    def darksky_api_call(self, lat, lng, time):
        return DARKSKY_API_ENDPOINT + DARKSKY_SECRET_KEY + '/' + str(lat) + ',' + str(
            lng) + ',' + time  # "2018-11-02T00:00:00"

    def getResult(self, lat, lng, time):

        # monday is 0
        current_day = datetime.datetime.now()  # .weekday() + 1

        evaluated_day = 0
        format_date = True

        if time == "XXXX-WXX-1T00:00:00":  # Monday
            evaluated_day = 1
        elif time == "XXXX-WXX-2T00:00:00":  # Tuesday
            evaluated_day = 2
        elif time == "XXXX-WXX-3T00:00:00":  # Wednesday
            evaluated_day = 3
        elif time == "XXXX-WXX-4T00:00:00":  # Thursday
            evaluated_day = 4
        elif time == "XXXX-WXX-5T00:00:00":  # Friday
            evaluated_day = 5
        elif time == "XXXX-WXX-6T00:00:00":  # Saturday
            evaluated_day = 6
        elif time == "XXXX-WXX-7T00:00:00":  # Sunday
            evaluated_day = 7
        else:
            format_date = False

        if format_date:
            date_diff = evaluated_day - (current_day.weekday() + 1)  # apply date difference
            time = current_day + datetime.timedelta(days=date_diff)  # refactor time
            time = time.replace(microsecond=0)  # remove milliseconds
            time = str(time).replace(' ', 'T')  # format string

        weather_response = requests.get(self.darksky_api_call(lat, lng, str(time)))

        weather_response_json_payload = weather_response.json()

        self.formatted_date = time.split("T")[0]

        # example: https://api.darksky.net/forecast/daf75c2187a8f88c0f50be1501168d61/37.8267,-122.4233
        print(weather_response_json_payload)
        if 'code' in weather_response_json_payload:
            if weather_response_json_payload['code'] == 400:
                print("date time format error")
        else:
            self.weekly_summary = weather_response_json_payload['currently']['summary']
            self.icon = weather_response_json_payload['currently']['icon']
            self.temperature = weather_response_json_payload['currently']['temperature']
            self.daily = weather_response_json_payload['daily']
            self.daily_data = self.daily['data']
            self.hourly_data = weather_response_json_payload['hourly']['data']

    def printResult(self):
        return_result = ''
        return_result += '\nWeather in ' + self.formatted_address + ' on ' + str(
            datetime.datetime.utcfromtimestamp(int(self.daily_data[0]['time'])).strftime('%m/%d/%Y')) + '\n'
        return_result += 'Expected forecast: '+ self.weekly_summary + ' ' + str(self.temperature) + '\n'
        # do we want to print weekly summary or is it just part of the debugging process
        # return_result += 'Weekly summary: ' + self.daily
        # for d in self.daily_data:
        #   return_result += str(datetime.datetime.utcfromtimestamp(int(d['time'])).strftime('%m-%d-%Y')) + ' : ' + d['summary'] + "\n" #%H:%M:%S

        # i = 0
        # for d in self.hourly_data:
        #     return_result += str(datetime.datetime.utcfromtimestamp(int(d['time'])).strftime('%m-%d-%Y %H:%M:%S')) +  " : " + d['summary'] + ","
        #     # i = i + 1
        #     # if i % 3 == 0:
        #     return_result += "\n"

        print('\nWeather at: ', self.formatted_address)
        print(self.weekly_summary, '\n', self.temperature)

        # print('Weekly summary: ', self.daily)

        for d in self.daily_data:
            print(self.formatted_date, ' : ', d['summary'])
        return return_result
