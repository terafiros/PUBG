from PIL import Image
from core.pubg import PUBG
from constants.constants import Shard

key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwMDQzNWU1MC0xODZiLTAxMzctNzM1OC0wZTM1MzFmZGJkNWEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUwNzk3MTU2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctdGVhY2hlciJ9.zM2r5FJZP3IkcRVVFN1ApBDesf-JJn3QPAZyxNr2QR4'
pubg = PUBG(key, Shard.pc_sa.value)

sample = pubg.get_sample()
matches = []
print('sample')

for match_id in sample.matches:
    matches.append(pubg.get_match(match_id))

print('matches')

for match in matches:
    print(match.asset.url)

