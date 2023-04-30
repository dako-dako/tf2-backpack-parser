import argparse
from enum import Enum
from bp_acc import Account
from bp_api import Backpack
from setup import (
    collector_webhook,
    quick_switch_webhook,
    morning_glory_webhook,
    death_at_dusk_webhook,
    frostbite_webhook,
    roboactive_webhook,
    anti_freeze_webhook,
    time_warp_webhook,
    green_black_hole_webhook,
    ghastly_ghosts_jr_webhook,
    haunted_phantasm_jr_webhook,
)

from config import BACKPACK_API_KEY, CLIENT_ID, CLIENT_SECRET

acc = Account(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, api_key=BACKPACK_API_KEY
)
bp = Backpack(acc=acc)
parser = argparse.ArgumentParser()


class SubCommand(Enum):
    listings_to_db = "listings-to-db"
    listings_sync = "listings-sync"

    def __str__(self):
        return self.value


subparsers = parser.add_subparsers(
    help="Action",
    required=True,
    dest="action",
)

parser_listings_to_db = subparsers.add_parser(
    "listings-to-db", help="Adding all listings to DB"
)
parser_listings_sync = subparsers.add_parser(
    "listings-sync",
    help="Updating listings in DB and " "sending notifications in Discord",
)


def main():
    args = parser.parse_args()
    match SubCommand(args.action):
        case SubCommand.listings_to_db:
            bp.get_collectors_classifieds(page_size=30)  # Getting all collector weapons
            bp.get_all_quick_switch_classifieds(
                page_size=30, particle=""
            )  # Getting all Quick Switch unusuals
            bp.get_unusual_classifieds_by_effect(
                page_size=30, particle="89"
            )  # Getting all unusuals with Morning Glory
            bp.get_unusual_classifieds_by_effect(
                page_size=30, particle="90"
            )  # Getting all unusuals with Death At Dusk
            bp.get_unusual_classifieds_by_effect(
                page_size=30, particle="87"
            )  # Getting all unusuals with Frostbite
            bp.get_unusual_classifieds_by_effect(
                page_size=30, particle="72"
            )  # Getting all unusuals with Roboactive
            bp.get_unusual_classifieds_by_effect(
                page_size=30, particle="69"
            )  # Getting all unusuals with Anti-Freeze
            bp.get_unusual_classifieds_by_effect(
                page_size=30, particle="70"
            )  # Getting all unusuals with Time Warp
            bp.get_unusual_classifieds_by_effect(
                page_size=30, particle="71"
            )  # Getting all unusuals with Green Black Hole
            bp.get_unusual_classifieds_by_effect(
                page_size=30, particle="85"
            )  # Getting all unusuals with Ghastly Ghosts Jr
            bp.get_unusual_classifieds_by_effect(
                page_size=30, particle="86"
            )  # Getting all unusuals with Haunted Phantasm Jr

        case SubCommand.listings_sync:
            # COLLECTOR ITEMS
            bp.get_collectors_classifieds(
                discord_webhook=collector_webhook, page_size=30
            )
            print("FINISH COLLECTORS")

            # QUICK SWITCH ITEMS
            bp.get_all_quick_switch_classifieds(
                discord_webhook=quick_switch_webhook, page_size=30, particle=""
            )
            print("FINISH QUICK SWITCHES")

            # EOTL EFFECTS
            bp.get_unusual_classifieds_by_effect(
                discord_webhook=morning_glory_webhook, page_size=30, particle="89"
            )
            print("FINISH MORNING GLORY")
            bp.get_unusual_classifieds_by_effect(
                discord_webhook=death_at_dusk_webhook, page_size=30, particle="90"
            )
            print("FINISH DEATH AT DUSK")
            bp.get_unusual_classifieds_by_effect(
                discord_webhook=frostbite_webhook, page_size=30, particle="87"
            )
            print("FINISH FROSTBITE")

            # ROBO EFFECTS
            bp.get_unusual_classifieds_by_effect(
                discord_webhook=roboactive_webhook, page_size=30, particle="72"
            )
            print("FINISH ROBOACTIVE")
            bp.get_unusual_classifieds_by_effect(
                discord_webhook=anti_freeze_webhook, page_size=30, particle="69"
            )
            print("FINISH ANTI-FREEZE")
            bp.get_unusual_classifieds_by_effect(
                discord_webhook=time_warp_webhook, page_size=30, particle="70"
            )
            print("FINISH TIME WARP")
            bp.get_unusual_classifieds_by_effect(
                discord_webhook=green_black_hole_webhook, page_size=30, particle="71"
            )
            print("FINISH GREEN BLACK HOLE")

            # MISC EFFECTS
            bp.get_unusual_classifieds_by_effect(
                discord_webhook=ghastly_ghosts_jr_webhook, page_size=30, particle="85"
            )
            print("FINISH GHASTLY GHOSTS JR")
            bp.get_unusual_classifieds_by_effect(
                discord_webhook=haunted_phantasm_jr_webhook, page_size=30, particle="86"
            )
            print("FINISH HAUNTED PHANTASM JR")


if __name__ == "__main__":
    main()
