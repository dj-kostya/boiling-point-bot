from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field


class ListItem(BaseModel):
    id: int
    name: str
    photo: Optional[str]


class Participants(BaseModel):
    count: int
    list: List[ListItem]


class Stat(BaseModel):
    participants: Participants


class Photo(BaseModel):
    full: str


class Photo1(BaseModel):
    url: Optional[str]


class Theme(BaseModel):
    id: int
    name: str
    visible: bool
    updated_at: Optional[str]
    createdBy: int
    priority: int
    status: int
    keywords: List[str]
    photos: Union[List, Photo]
    old_type: Optional[str]
    gid: int
    code: Optional[str]
    parentId: Optional[int]
    childCount: int
    moderatedBy: Optional[int]
    moderatedAt: Optional[str]
    photo: Photo1


class Type(BaseModel):
    id: int
    name: str


class Thumb(BaseModel):
    field_180: str = Field(..., alias="180")
    field_360: str = Field(..., alias="360")
    field_520: str = Field(..., alias="520")


class Photo2(BaseModel):
    full: str
    thumb: Thumb


class SocialNetwork(BaseModel):
    url: str
    alias: str


class Stat1(BaseModel):
    participantCount: int
    active_participants: int
    uniqueUsers: int
    participantAverage: str
    regionScope: int
    monthEventCount: int
    ntiPercent: float
    moderationTime: str


class Tz(BaseModel):
    value: str
    minutes: int


class Address(BaseModel):
    id: int
    city_id: int
    region_id: int
    country_id: int
    post_code: Optional[str]
    street: str
    house: Optional[str]
    building: Optional[str]
    wing: Any
    apartment: Any
    place: Any
    geo_point: str
    geo_point_zoom: Any
    letter: Any
    user_id: Any
    city: str
    region: str
    country: str
    title: str
    timezone: str
    tz: Tz


class Space(BaseModel):
    id: int
    phone: str
    phoneExtension: Optional[str]
    addressId: int
    active: bool
    kworkingState: Any
    agenda: List[str]
    square: str
    email: str
    name: str
    description: str
    rating: Any
    type: str
    minimalPeriod: int
    photos: List[Photo2]
    tags: List[str]
    socialNetworks: List[SocialNetwork]
    scheduleOnRequest: bool
    stat: Stat1
    createdAt: str
    updatedAt: str
    restrictEventOwnerOfflineConfirm: bool
    address: Address


class Networking(BaseModel):
    spaceIds: List[int]
    broadcast: str


class Thumb1(BaseModel):
    field_360: str = Field(..., alias="360")
    field_520: str = Field(..., alias="520")


class Photo3(BaseModel):
    full: str
    thumb: Thumb1


class Hall(BaseModel):
    id: int
    name: str
    capacity: int
    type: str
    square: str
    tags: List[str]
    preparePeriod: int
    photos: List[Photo3]


class Timezone(BaseModel):
    value: str
    minutes: int


class EventItem(BaseModel):
    id: int
    createdBy: int
    live_public: bool
    live: Optional[List[str]]
    stat: Stat
    themes: List[Theme]
    type: Type
    info: Any
    moderation: str
    status: str
    full_info: str
    full_name: str
    date_start: str
    date_end: str
    format: str
    space: Space
    place: Any
    schedules: List
    networking: Networking
    participation_format: str
    team_size_min: Optional[int]
    team_size_max: Optional[int]
    team_type: Any
    finished: bool
    afterQuizId: Any
    needFeedback: bool
    hash_tags: List[str]
    network_parent_id: Any
    city: str
    city_id: int
    halls: List[Hall]
    photo: str
    photo_520: str
    photo_360: str
    photo_180: str
    timezone: Timezone
    needStartNotification: bool
    delivered: bool
    indexedAt: int
    isFavorite: bool


class MetaInfo(BaseModel):
    totalCount: int
    pageCount: int
    currentPage: int
    perPage: int


class Data(BaseModel):
    items: List[EventItem]
    meta: MetaInfo


class SearchResponse(BaseModel):
    data: Optional[Data] = None
