from core.pubg import PUBG
import requests
from PIL import Image, ImageDraw
from telemetry.telemetry import Telemetry
from constants.constants import Events
import json


def sem_api():
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwMDQzNWU1MC0xODZiLTAxMzctNzM1OC0wZTM1MzFmZGJkNWEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUwNzk3MTU2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctdGVhY2hlciJ9.zM2r5FJZP3IkcRVVFN1ApBDesf-JJn3QPAZyxNr2QR4'
    plat = 'steam'
    pubg = PUBG(key, plat)
    
    miramar = Image.open('miramar_original.jpg')
    kill = Image.open('Death.png')
    position = Image.open('position.png')

    #t = Telemetry(telemetry.json(), Events.LogPlayerKill)
    
    with open('json/telemetry_1.json') as data:
        t = pubg.get_telemetry_from_json(json.load(data), Events.LogPlayerKill)
        for event in t.events:
            x, y = event.victim.location.x, event.victim.location.y
            miramar.paste(kill, (int(8000 * x / 816000), int(8000 * y / 816000)), kill)
        
    '''
    count = 0
    verify = 0

    for ox, oy in t.player_kill():
        miramar.paste(kill, (int(ox), int(oy)), kill)

    for ox, oy, r in t.safety_zone_position():
        draw = ImageDraw.Draw(miramar)
        draw.ellipse((ox - r, oy - r, ox + r, oy + r), outline='green')

    
        if tele['_T'] == 'LogPlayerPosition':
            if tele['character']['name'] == 'Tecnosh':
                x = tele['character']['location']['x']
                y = tele['character']['location']['y']

                ox = 2048 * x / 816000
                oy = 2048 * y / 816000
                print(ox, oy)
                erangel.paste(position, (int(ox), int(oy)), position)
    '''
    
    miramar.show()
    
if __name__ == '__main__':
    sem_api()