import datetime

import requests
from domain.clients.leader_id import SearchResponse


class LeaderIdClient:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    def get_events(
        self,
        start_date: datetime.datetime | None = None,
        end_date: datetime.datetime | None = None,
        place_id: int | None = None,
    ) -> SearchResponse:
        resp = requests.get(
            url=f"{self._base_url}/api/v4/events/search",
            params={
                "dateFrom": start_date.strftime("%Y-%m-%d") if start_date else None,
                "dateTo": end_date.strftime("%Y-%m-%d") if end_date else None,
                "placeIds[]": place_id,
            },
            timeout=1,
        )
        if resp.status_code != requests.codes.ok:
            raise RuntimeError("Cant get events")
        return SearchResponse.model_validate(resp.json())
