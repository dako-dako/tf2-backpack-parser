from pydantic import BaseModel


class ListingObject(BaseModel):
    listing_id: str
    data_md5: str
    data: dict
