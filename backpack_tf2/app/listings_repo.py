from setup import db
from entities import ListingObject
import pymongo


class ListingsRepository:
    def __init__(self, collection_name):
        self.collection_name: pymongo.collection.Collection = db[collection_name]

    def get_by_filter(self, getfilter: dict) -> ListingObject | None:
        """
        Get info about ListingObject using MongoDB find filter.
        If ListingObject record exists -> return ListingObject instance.
        If ListingObject record doesn't exist -> return None.
        """
        data = self.collection_name.find_one(getfilter)
        if data is not None:
            return ListingObject(**data)
        return None

    def create(self, instance: ListingObject) -> ListingObject:
        """
        Receive ListingObject instance without id.
        Add record to db.
        """
        instance_to_dict = instance.dict()
        self.collection_name.insert_one(instance_to_dict)
        return instance
