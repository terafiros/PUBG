maps = {
    "Desert_Main": "Miramar",
    "DihorOtok_Main": "Vikendi",
    "Erangel_Main": "Erangel",
    "Range_Main": "Camp Jackal",
    "Savage_Main": "Sanhok"
    }
    
def get_map_name(convert):
    return maps[convert]

def save_json(path, file_json):
    file = open(path, 'w+')
    file.write(file_json)
    file.close()

def get_telemtry_id(url):
    index = url.rindex('/')
    url = url[index + 1:]
    return url.rstrip()

def get_url(url):
    return url.rstrip()
    
    
