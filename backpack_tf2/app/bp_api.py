import misc
from bp_acc import Account
from entities import ListingObject
from helpers import (
    del_multiple_keys,
    pop_multiple_keys,
    currency_parser,
)
from listings_repo import ListingsRepository
from typing import Optional
from discord_webhook import DiscordWebhook, DiscordEmbed
import urllib.parse
import json
import requests
import hashlib
import time


class Backpack:
    """Backpack class is responsible for interaction with Backpack.tf API."""

    collection_unusual_hats = ListingsRepository("unusualHats")
    collection_collector_weps = ListingsRepository("collectorWeps")
    collection_unusual_weps = ListingsRepository("unusualWeps")

    def __init__(self, acc: Account):
        self.acc = acc

    def search_classifieds(
        self,
        intent: Optional[str] = "dual",
        page_size: Optional[int] = 10,
        fold: Optional[int] = 0,
        quality: Optional[int] = 5,
        particle: Optional[str] = "",
        page: Optional[int] = 1,
        slot: Optional[str] = "misc",
        class_: Optional[str] = "",
        item: Optional[str] = "",
    ):
        """
        :param intent: Filter listings by intent. Default: dual. Valid options: sell, buy, dual. Takes str as input
        :param page_size: Modify the page size used to paginate. Must be >= 1 and <= 30.
        Use the "page" parameter to paginate. Default: 10. Takes int as input
        :param fold: If set to 0, disables listing folding. Takes int as input
        :param quality: Filters listings by quality of item. Takes int as input
        (e.g. unusual quality converts to value of 5).
        :param particle: Filter listings by particle ID. Takes int as input.
        (e.g. burning flames particle converts to value of 13). Read more --> https://backpack.tf/developer/particles.
        :param page: The page number you want to view. Takes int as input
        :param slot: Filter listings by slot (e.g.: misc, )
        :param class_: Filter listings by TF2 classes (e.g.: scout,soldier,pyro etc). P.S. Write without spaces
        :param item: Filter listings by item name.
        :return: dict of filtered classifieds
        """
        payload = {
            "key": self.acc.api_key,
            "intent": intent,
            "page": page,
            "page_size": page_size,
            "fold": fold,
            "quality": quality,
            "particle": str(particle),
            "slot": slot,
            "class": class_,
            "item": item,
        }

        encoded = urllib.parse.urlencode(payload)

        r = requests.get("https://backpack.tf/api/classifieds/search/v1?" + encoded)
        jsondata = json.loads(r.text)

        return jsondata

    def get_all_classifieds(
        self,
        collection_: ListingsRepository,
        discord_webhook: Optional[DiscordWebhook] = None,
        page_size: Optional[int] = 10,
        quality: Optional[int] = 5,
        particle: Optional[str] = "89",
        slot: Optional[str] = "",
        class_: Optional[str] = "",
        item: Optional[str] = "",
    ):
        embed_counter = 0
        page_to_parse = 1
        classifieds = self.search_classifieds(
            page=page_to_parse,
            page_size=page_size,
            quality=quality,
            slot=slot,
            class_=class_,
            item=item,
            particle=particle,
        )
        repeat = classifieds["sell"]["total"]
        while repeat > 0:
            classifieds = self.search_classifieds(
                page=page_to_parse,
                page_size=page_size,
                quality=quality,
                slot=slot,
                class_=class_,
                item=item,
                particle=particle,
            )
            for listing in classifieds["sell"]["listings"]:
                pop_multiple_keys(listing, ["automatic", "promoted"])
                del_multiple_keys(
                    listing, ["appid", "offers", "buyout", "created", "bump", "intent"]
                )
                listing_id = listing.pop("id", None)
                md5_hash = hashlib.md5(
                    json.dumps(listing, sort_keys=True).encode("utf-8")
                ).hexdigest()
                listing_instance = ListingObject(
                    listing_id=listing_id, data_md5=md5_hash, data=listing
                )
                db_record = collection_.get_by_filter(
                    {"data_md5": listing_instance.data_md5}
                )
                if db_record is not None:
                    pass
                else:
                    collection_.create(listing_instance)
                    if discord_webhook:
                        if embed_counter == 8:
                            discord_webhook.execute(remove_embeds=True)
                            embed_counter = 0
                        else:
                            item_name = listing_instance.data["item"]["name"]
                            description = listing_instance.data["details"]
                            profile_link = "https://steamcommunity.com/profiles/" + str(
                                listing_instance.data["steamid"]
                            )
                            currency = currency_parser(
                                listing_instance.data["currencies"]
                            )
                            embed = DiscordEmbed(title=f"**{item_name}**", color=242424)
                            embed.set_author(
                                name="Seller's Steam profile",
                                url=profile_link,
                                icon_url="https://media.istockphoto.com/id/163011987/photo/dollar-bill-bundles-pile.jpg?s=612x612&w=0&k=20&c=VlIOlrsfqb7WWAPsmOID4ILguRX9bS4MqNsg_S7WhRE=",
                            )
                            embed.add_embed_field(name="Price", value=f"{currency}")
                            if description == "":
                                pass
                            else:
                                embed.add_embed_field(
                                    name="Description", value=description
                                )
                            embed.set_timestamp()
                            discord_webhook.add_embed(embed)
                            embed_counter += 1
                repeat -= 1

            if discord_webhook and embed_counter != 0:
                discord_webhook.execute(remove_embeds=True)
                embed_counter = 0
            page_to_parse += 1

    def get_unusual_classifieds_by_effect(
        self,
        discord_webhook: Optional[DiscordWebhook] = None,
        page_size: Optional[int] = 10,
        particle: str = "",
    ):
        self.get_all_classifieds(
            discord_webhook=discord_webhook,
            collection_=self.collection_unusual_hats,
            page_size=page_size,
            class_="scout,soldier,pyro",
            particle=particle,
            slot="misc",
        )
        self.get_all_classifieds(
            discord_webhook=discord_webhook,
            collection_=self.collection_unusual_hats,
            page_size=page_size,
            class_="demoman,heavy,engineer",
            particle=particle,
            slot="misc",
        )
        self.get_all_classifieds(
            discord_webhook=discord_webhook,
            collection_=self.collection_unusual_hats,
            page_size=page_size,
            class_="medic,sniper,spy",
            particle=particle,
            slot="misc",
        )
        for item in misc.all_class_hats:
            self.get_all_classifieds(
                discord_webhook=discord_webhook,
                collection_=self.collection_unusual_hats,
                page_size=30,
                item=item,
                particle=particle,
            )
            time.sleep(1.4)

    def get_all_quick_switch_classifieds(
        self,
        discord_webhook: Optional[DiscordWebhook] = None,
        page_size: Optional[int] = 10,
        particle: str = "",
    ):
        for item in misc.quick_switch_hats:
            self.get_all_classifieds(
                discord_webhook=discord_webhook,
                collection_=self.collection_unusual_hats,
                page_size=page_size,
                item=item,
                particle=particle,
            )
            time.sleep(1.4)

    def get_collectors_classifieds(
        self,
        discord_webhook: Optional[DiscordWebhook] = None,
        page_size: Optional[int] = 10,
    ):
        self.get_all_classifieds(
            discord_webhook=discord_webhook,
            collection_=self.collection_collector_weps,
            page_size=page_size,
            quality=14,
            particle="",
            slot="primary,secondary,melee",
        )
