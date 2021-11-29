from urllib.request import urlopen
import json
import ssl

class Subscribe:
    '''
    ThingSpeak Cloud subscribe
    '''

    def __init__(self):
        # Chennel API (result=1 :: take most current data / last entry)
        self.URL = 'https://api.thingspeak.com/channels/1385704/feeds.json?results=1'
        self.context = ssl._create_unverified_context()

        # Test
        # self.URL = 'https://api.thingspeak.com/channels/1385093/feeds.json?results=1'

    def fetch_update(self):
        # function to fetch date from Chennel API

        with urlopen(self.URL,context=self.context) as url:
            # parse JSON
            data = json.loads(url.read().decode())
            
            return data

if __name__ == '__main__':
    source = Subscribe()
    f = open('/home/data.json','w')
    f.write(json.dumps(source.fetch_update(),indent = 1))
    f.close()