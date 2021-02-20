import requests
class LUIS:
    
    def __init__(self, key):
        self.intent=""
        self.input=""
        self.APIkey=key
        self.link="https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/7f58c0cb-8b08-4c85-9074-56e4c7b6c946?subscription-key="+self.APIkey+"&timezoneOffset=-360&q="
        
        #access the API
        
        
    def GetJson(self, response):
        #do the initialization of Luis with the API key
        query=self.link+response
        try:
        #r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/7f58c0cb-8b08-4c85-9074-56e4c7b6c946?subscription-key=9d556518bc2b49489a61ddbdc98884a3&timezoneOffset=-360&q=weather in tallahassee')
            r= requests.get(query)
       
    
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return r.json()
            
        
    def GetIntent(self, response):
        #use response to get the intent
        x = self.GetJson(response)
        return x['topScoringIntent']
    
    def GetEntities(self, response):
        x = self.GetJson(response)
        return x['entities']
    
    
    
    


if __name__ == "__main__":
    y=LUIS("9d556518bc2b49489a61ddbdc98884a3")
    x=y.GetIntent("weather in 8 hour")
    #x=y.GetEntities("weather in tallhassee tomorrow")
    print(x['intent'])


    
   
            