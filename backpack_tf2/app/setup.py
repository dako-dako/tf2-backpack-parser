import pymongo
from config import (
    MONGODB_IP,
    MONGODB_PORT,
    MONGO_DB_NAME,
)
from discord_webhook import DiscordWebhook

db_connect = pymongo.MongoClient(MONGODB_IP, MONGODB_PORT)

db = db_connect[MONGO_DB_NAME]

collector_content = "New classified listing with Collector's item"
quick_switch_content = "New classified listing with Unusual Quick Switch"
morning_glory_content = "New classified listing with Morning Glory Hat"
death_at_dusk_content = "New classified listing with Death At Dusk Hat"
frostbite_content = "New classified listing with Frostbite Hat"
roboactive_content = "New classified listing with Roboactive Hat"
anti_freeze_content = "New classified listing with Anti-Freeze Hat"
time_warp_content = "New classified listing with Time Warp Hat"
green_black_hole_content = "New classified listing with Green Black Hole Hat"
ghastly_ghosts_jr_content = "New classified listing with Ghastly Ghosts Jr Hat"
haunted_phantasm_jr_content = "New classified listing with Haunted Phantasm Jr Hat"

# COLLECTOR ITEMS
collector_webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1085586773649932358/AJQLNtXrrodAUeUXoGJ1P4q02jO2uf_slg838ZDIlz3M6O7SZNVnCkc48IXKF1cVA0BA",
    content=collector_content,
)

# UNUSUAL QUICK SWITCHES
quick_switch_webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1102158467189444688/C1_zq3IDLcZ3xo-yt0RaOZ_5at0SsnQNuHEeuWSpEPz9scHLcxwPPZtFx1uIwwECQ0K4",
    content=quick_switch_content,
)

# EOTL EFFECTS
morning_glory_webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1085588920902877244/uwbEdf99a5M04vXcOvyO-8MQLft4YTpwwzbkdMIejtHg2pzwvhkwMGaGEFNnEp8VAUwO",
    content=morning_glory_content,
)
death_at_dusk_webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1085589012175147028/825UGkl6RoNI7fGb3wXZ2NpFvhLbXNgElh2yipkupfEd5akKZv4Cso1vQozTlm9eVqtf",
    content=death_at_dusk_content,
)
frostbite_webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1085589134195822642/Eqisw1O3f2vxFCsrsICHiwaqS0JbLPMc3GjjqtF8d98s1uHUqsN9Ppbj9xT29_6kB1-l",
    content=frostbite_content,
)

# ROBO EFFECTS
roboactive_webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1085589416527016057/vodO0f0NJTHpnVo6bqsL_prXS9E8uXOC53iJj5LhhAW8Lgb6lFTB6E199areAdckbk0u",
    content=roboactive_content,
)
anti_freeze_webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1085589508508106772/e_-h0UnpkKnzfFJh1dyF0fgCqmmtfvdSf9AiHe6H1Pz88qsxCqCvKUO2xnGECCYtSDv9",
    content=anti_freeze_content,
)
time_warp_webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1085589647981293669/sOAz7lA0cqFMIiQKJ4qCLKE4bMCxdkuF4GMddONO6y_2mpW9vTOnemJYikyxO_mpKVhb",
    content=time_warp_content,
)
green_black_hole_webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1085589750238421183/aVElA1G1KiRNk63g8iEXq-SVybyuMQXMbzQRgkfk818ko8evypQFnGM4N9PU1Nhc4A4R",
    content=green_black_hole_content,
)

# MISC EFFECTS
ghastly_ghosts_jr_webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1085589878051446865/yiCY8eGP-PAG5lfQGH11s9rhZJTxomGHteWazvOUwYynHRRVxkLJsLivAuV5PCDdi-WE",
    content=ghastly_ghosts_jr_content,
)
haunted_phantasm_jr_webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1085589985274638367/puw9I7t02G8Q9vX7eQN_K7cG8mpDXMjZFtrfdq_JeJ065w2kanr-RbJYYuE1Uqj5R1UG",
    content=haunted_phantasm_jr_content,
)
