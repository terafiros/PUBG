from pubg import PUBG
import requests
from PIL import Image, ImageDraw

if __name__ == '__main__':

    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwMDQzNWU1MC0xODZiLTAxMzctNzM1OC0wZTM1MzFmZGJkNWEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUwNzk3MTU2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctdGVhY2hlciJ9.zM2r5FJZP3IkcRVVFN1ApBDesf-JJn3QPAZyxNr2QR4'
    plat = 'steam'
    pubg = PUBG(key, plat)
    header = {
        'Authorization': 'Bearer ' + key,
        'Accept': 'application/vnd.api+json'
    }
    # url = "https://api.pubg.com/shards/steam/matches/11e5041a-71a5-4612-9587-0ad22cf7b954" 2019-03-09T03:05:38Z
    url = 'https://api.pubg.com/shards/steam/samples'  # ?filter[createdAt-start]=2019-03-23T10:49:00Z'
    rsp = requests.get(url, headers=header)
    m_id = 'e54ce173-3fe1-4059-982c-f260d737b177'

    # player = pubg.get_player('Tecnosh')
    match = pubg.get_match(m_id)

    print(match.mapName)
    print(match.duration)
    print(match.gameMode)

    # 4326
    erangel = Image.open('nova.png')
    kill = Image.open('Death.png')
    position = Image.open('position.png')

    position.convert(mode="RGBA").save('position.png')

    print(position)

    telemetry = requests.get(match.asset.URL)
    tele_json = telemetry.json()

    count = 0
    verify = 0

    for tele in tele_json:
        if tele['_T'] == 'LogPlayerKill':
            count += 1

            x = tele['victim']['location']['x']
            y = tele['victim']['location']['y']

            ox = 2048 * x / 816000
            oy = 2048 * y / 816000

            erangel.paste(kill, (int(ox), int(oy)), kill)

        if tele['_T'] == 'LogGameStatePeriodic':
            if tele['common']['isGame'] > verify:

                verify += 1
                safe_x = tele['gameState']['safetyZonePosition']['x']
                safe_y = tele['gameState']['safetyZonePosition']['y']
                radius = tele['gameState']['safetyZoneRadius']

                safe_ox = 2048 * safe_x / 816000
                safe_oy = 2048 * safe_y / 816000
                radius_o = 2048 * radius / 816000

                draw = ImageDraw.Draw(erangel)
                draw.ellipse((safe_ox - radius_o, safe_oy - radius_o, safe_ox + radius_o, safe_oy + radius_o), outline='white')

        if tele['_T'] == 'LogPlayerPosition':
            if tele['character']['name'] == 'Tecnosh':
                x = tele['character']['location']['x']
                y = tele['character']['location']['y']

                ox = 2048 * x / 816000
                oy = 2048 * y / 816000
                print(ox, oy)
                erangel.paste(position, (int(ox), int(oy)), position)


    print(count)
    erangel.show()
