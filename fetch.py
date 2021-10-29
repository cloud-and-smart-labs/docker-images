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

            # return data in format -> (Date,Time,Temperature,Humidity)
            return (
                data['feeds'][-1]['created_at'].split('T')[0],
                data['feeds'][-1]['created_at'].split('T')[1][:-1],
                data['feeds'][-1]['field1'],
                data['feeds'][-1]['field2']
            )

if __name__ == '__main__':
    source = Subscribe()
    print(source.fetch_update())