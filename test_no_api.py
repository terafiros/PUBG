def sem_api():
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

    player = pubg.get_player('terafiros')
    match = pubg.get_match(player.matches_ids[0])

    print(match.mapName)
    print(match.duration)
    print(match.gameMode)

    # 4326
    erangel = Image.open('maps/nova.png')
    miramar = Image.open('maps/miramar.jpg')

    print(miramar.mode)

    kill = Image.open('maps/Death.png')
    position = Image.open('maps/position.png')

    telemetry = requests.get(match.asset.URL)
    print(match.asset.URL)

    t = Telemetry(telemetry.json())

    count = 0
    verify = 0

    for ox, oy in t.player_kill():
        miramar.paste(kill, (int(ox), int(oy)), kill)

    for ox, oy, r in t.safety_zone_position():
        draw = ImageDraw.Draw(miramar)
        draw.ellipse((ox - r, oy - r, ox + r, oy + r), outline='green')

    '''
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