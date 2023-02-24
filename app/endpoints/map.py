from typing import Any, List, Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, cast, Date, func

from fastapi import APIRouter, Depends, Response

import json

from datetime import date

from app.db.base import get_session
from app.db import models as m
from app import commons

router = APIRouter()


@router.get('/total_counter')
async def get_total_counter(session: AsyncSession = Depends(get_session)):
    """
    Returns value of total counter for Moscow.
    """
    async with session.begin():
        q = select(m.Counter.count_value).where(m.Counter.name == "total_taken")
        res = await session.execute(q)

    return res.one_or_none().count_value


@router.get('/cities')
async def get_cities():
    """
    Returns hardcoded list of available cities with coordinates.
    """
    output = [{"city_name": "msc", "coordinates": [55.755821, 37.617635]},
              {"city_name": "mrm", "coordinates": [68.970663, 33.074918]},
              {"city_name": "nn", "coordinates": [56.326797, 44.006516]},
              {"city_name": "tmn", "coordinates": [57.152985, 65.541227]}]

    return output


@router.get('/map')
async def get_map_data(city: str,
                       start_date: date,
                       end_date: date,
                       show_taken: bool,
                       show_returned: bool,
                       session: AsyncSession = Depends(get_session)):
    """
    Returns sum of taken/returned for every station in specified range of dates.
    If show_taken and show_returned both False, returns nothing
    """
    testday, stations_metadata = commons.select_city_models(city)

    if show_returned:
        term = testday.ordinarybikes_delta_returned
    elif show_taken:
        term = testday.ordinarybikes_delta_taken
    else:
        return

    async with session.begin():
        q = select(testday.velobike_id, stations_metadata.lon, stations_metadata.lat,
                       func.sum(term).label('sum')) \
            .where(and_(testday.velobike_id == stations_metadata.velobike_id,
                        cast(testday.timestamp, Date).between(start_date, end_date)))\
            .group_by(testday.velobike_id, stations_metadata.lon, stations_metadata.lat)
        res = await session.execute(q)

    # preparing geojson points
    features = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [lon, lat],
            },
            'properties': {
                'Id': velobike_id,
                'Value': float(value),
            }
        }
        for (velobike_id, lon, lat, value) in filter(lambda x: x[3] is not None and x[3] != 0, res)
    ]
    # forming geojson
    output = '{"type":"FeatureCollection","features":' + \
             json.dumps(features, separators=(',', ':'), ensure_ascii=False, default=int) + \
             '}'
    return Response(content=output, media_type="application/json")
