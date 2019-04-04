class Player:
    def __init__(self, type = '', id = '', updatedAt = '', name = '', titleId = '', shardId = '', createdAt = '', matches = [], name_search_url = '', id_search_url = '' ):
        self.type = type
        self.id = id
        self.updatedAt = updatedAt
        self.name = name
        self.titleId = titleId
        self.shardId = shardId
        self.createdAt = createdAt
        self.matches = matches
        self.name_search_url = name_search_url
        self.id_search_url = id_search_url

class Season:
    def __init__(self, type = '', id = '', isOffseason = False, isCurrentSeason = False):
        self.id = id
        self.type = type
        self.isOffseason = isOffseason
        self.isCurrentSeason = isCurrentSeason