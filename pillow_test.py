from PIL import Image, ImageDraw, ImageFont
from core.pubg import PUBG
from constants.constants import Shard, Events
from utils.utils import get_map_name, maps, get_telemtry_id, get_url
import os, json

def miramar_kills(player_kill):
    print('Kill number:', len(player_kill))
    miramar = Image.open('miramar_original.jpg')
    map_size_x, map_size_y = 816000, 816000
    
    print('Image size:', miramar.size)
    image_size_x, image_size_y = miramar.size
    
    death = Image.open('death.png')
    
    for kill in player_kill:
        ox = int(image_size_x * kill.victim.location.x / map_size_x)
        oy = int(image_size_y * kill.victim.location.y / map_size_y)
        if ox == oy == 0:
            continue
        miramar.paste(death, (ox, oy), death)
        
        draw = ImageDraw.Draw(miramar)
        font = ImageFont.truetype('Headliner.ttf', size=8)
        color = 'rgb(0, 0, 0)' 
        draw.text((ox + 8, oy), kill.victim.name, fill=color, font=font)
            
    miramar.show()
    
def sanhok_kills(player_kill):
    print('Kill number:', len(player_kill))
    sanhok = Image.open('sanhok_original.png')
    map_size_x, map_size_y = 408000, 408000
    
    print('Image size:', sanhok.size)
    image_size_x, image_size_y = sanhok.size
    
    death = Image.open('death.png')
    
    for kill in player_kill:
        ox = int(image_size_x * kill.victim.location.x / map_size_x)
        oy = int(image_size_y * kill.victim.location.y / map_size_y)
        if ox == oy == 0:
            continue 
        sanhok.paste(death, (ox, oy), death)
        
        draw = ImageDraw.Draw(sanhok)
        font = ImageFont.truetype('Headliner.ttf', size=8)
        color = 'rgb(0, 0, 0)' 
        draw.text((ox + 8, oy), kill.victim.name, fill=color, font=font)
            
    sanhok.show()
    
def erangel_kills(player_kill):
    print('Kill number:', len(player_kill))
    erangel = Image.open('erangel_original.png')
    map_size_x, map_size_y = 816000, 816000
    
    print('Image size:', erangel.size)
    image_size_x, image_size_y = erangel.size
    
    death = Image.open('death.png')
    
    for kill in player_kill:
        ox = int(image_size_x * kill.victim.location.x / map_size_x)
        oy = int(image_size_y * kill.victim.location.y / map_size_y)
        if ox == oy == 0:
            continue
        erangel.paste(death, (ox, oy), death)
        
        draw = ImageDraw.Draw(erangel)
        font = ImageFont.truetype('Headliner.ttf', size=8)
        color = 'rgb(0, 0, 0)' 
        draw.text((ox + 8, oy), kill.victim.name, fill=color, font=font)
            
    erangel.show()

def vikendi_kills(player_kill):
    print('Kill number:', len(player_kill))
    vikendi = Image.open('vikendi_original.png')
    map_size_x, map_size_y = 612000, 612000
    
    print('Image size:', vikendi.size)
    image_size_x, image_size_y = vikendi.size
    
    death = Image.open('death.png')
    
    for kill in player_kill:
        ox = int(image_size_x * kill.victim.location.x / map_size_x)
        oy = int(image_size_y * kill.victim.location.y / map_size_y)
        if ox == oy == 0:
            continue
        vikendi.paste(death, (ox, oy), death)
        
        draw = ImageDraw.Draw(vikendi)
        font = ImageFont.truetype('Headliner.ttf', size=8)
        color = 'rgb(0, 0, 0)' 
        draw.text((ox + 8, oy), kill.victim.name, fill=color, font=font)
        
    vikendi.show()

def camp_jackal_kills(player_kill):
    print('Kill number:', len(player_kill))
    camp_jackal = Image.open('camp_jackal_original.png')
    map_size_x, map_size_y = 612000, 612000
    
    print('Image size:', camp_jackal.size)
    image_size_x, image_size_y = camp_jackal.size
    
    death = Image.open('death.png')
    
    for kill in player_kill:
        ox = int(image_size_x * kill.victim.location.x / map_size_x)
        oy = int(image_size_y * kill.victim.location.y / map_size_y)
        if ox == oy == 0:
            continue
        camp_jackal.paste(death, (ox, oy), death)
        
        draw = ImageDraw.Draw(camp_jackal)
        font = ImageFont.truetype('Headliner.ttf', size=8)
        color = 'rgb(0, 0, 0)' 
        draw.text((ox + 20, oy), kill.victim.name, fill=color, font=font)
            
    camp_jackal.show()
    
if '__main__' == __name__:
    
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwMDQzNWU1MC0xODZiLTAxMzctNzM1OC0wZTM1MzFmZGJkNWEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUwNzk3MTU2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctdGVhY2hlciJ9.zM2r5FJZP3IkcRVVFN1ApBDesf-JJn3QPAZyxNr2QR4'
    pubg = PUBG(key, Shard.pc_sa.value)
    
    '''
    url_asset = 'https://telemetry-cdn.playbattlegrounds.com/bluehole-pubg/pc-sa/2019/04/07/00/02/6fc20063-58c8-11e9-b483-0a586463b225-telemetry.json'
    
    with open("txt/telemetries.txt", "r") as reader:
        for url in reader:
            telemetry = pubg.get_telemetry(get_url(url), True, 'json/telemetries/' + get_telemtry_id(url), Events.LogMatchStart, Events.LogPlayerKill)
      
            print('Total events:', len(telemetry.events))
            print('Map name:', maps[telemetry.events[0].mapName])
          
            if maps[telemetry.events[0].mapName] == 'Miramar':
                miramar_kills(telemetry.events[1:])
            
            elif maps[telemetry.events[0].mapName] == 'Erangel':
                erangel_kills(telemetry.events[1:])
            
            elif maps[telemetry.events[0].mapName] == 'Sanhok':
                sanhok_kills(telemetry.events[1:])
        
            elif maps[telemetry.events[0].mapName] == 'Vikendi':
                vikendi_kills(telemetry.events[1:])
                
            elif maps[telemetry.events[0].mapName] == 'Camp Jackal':
                camp_jackal_kills(telemetry.events[1:])
            
            print('----------------------------------------------')
    
    '''
    for file in os.listdir(path='json/telemetries'):
        with open('json/telemetries/' + file) as data:
            telemetry = pubg.get_telemetry_from_json(json.load(data), Events.LogMatchStart, Events.LogPlayerKill)
            
            print('Total events:', len(telemetry.events))
            print('Map name:', maps[telemetry.events[0].mapName])
          
            if maps[telemetry.events[0].mapName] == 'Miramar':
                miramar_kills(telemetry.events[1:])
            
            elif maps[telemetry.events[0].mapName] == 'Erangel':
                erangel_kills(telemetry.events[1:])
            
            elif maps[telemetry.events[0].mapName] == 'Sanhok':
                sanhok_kills(telemetry.events[1:])
        
            elif maps[telemetry.events[0].mapName] == 'Vikendi':
                vikendi_kills(telemetry.events[1:])
                
            elif maps[telemetry.events[0].mapName] == 'Camp Jackal':
                camp_jackal_kills(telemetry.events[1:])
            
            print('----------------------------------------------')
            
        
    