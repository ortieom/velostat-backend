from fastapi import HTTPException
import app.db.models as m
import re


def select_city_models(city: str):
    """
    Returns corresponding testday and stations_metadata models for specified city.
    Raises error 400 if city is invalid.

    :param city:
    :return:
    """
    if city == 'msc':
        return m.TestdayMsc, m.StationsMetadataMsc
    if city == 'mrm':
        return m.TestdayMrm, m.StationsMetadataMrm
    if city == 'tmn':
        return m.TestdayTmn, m.StationsMetadataTmn
    if city == 'nn':
        return m.TestdayNn, m.StationsMetadataNn

    raise HTTPException(status_code=400, detail=f'{city} is not a valid city')
