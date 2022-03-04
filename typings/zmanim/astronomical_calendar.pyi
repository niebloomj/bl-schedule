"""
This type stub file was generated by pyright.
"""

from datetime import date, datetime
from typing import Optional
from zmanim.util.astronomical_calculations import AstronomicalCalculations
from zmanim.util.geo_location import GeoLocation
from zmanim.util.math_helper import MathHelper

class AstronomicalCalendar(MathHelper):
    GEOMETRIC_ZENITH = ...
    CIVIL_ZENITH = ...
    NAUTICAL_ZENITH = ...
    ASTRONOMICAL_ZENITH = ...
    __sentinel = ...
    def __init__(self, geo_location: Optional[GeoLocation] = ..., date: Optional[date] = ..., calculator: Optional[AstronomicalCalculations] = ...) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def sunrise(self) -> Optional[datetime]:
        ...
    
    def sea_level_sunrise(self) -> Optional[datetime]:
        ...
    
    def sunrise_offset_by_degrees(self, offset_zenith: float) -> Optional[datetime]:
        ...
    
    def sunset(self) -> Optional[datetime]:
        ...
    
    def sea_level_sunset(self) -> Optional[datetime]:
        ...
    
    def sunset_offset_by_degrees(self, offset_zenith: float) -> Optional[datetime]:
        ...
    
    def utc_sunrise(self, zenith: float) -> Optional[float]:
        ...
    
    def utc_sea_level_sunrise(self, zenith: float) -> Optional[float]:
        ...
    
    def utc_sunset(self, zenith: float) -> Optional[float]:
        ...
    
    def utc_sea_level_sunset(self, zenith: float) -> Optional[float]:
        ...
    
    def temporal_hour(self, sunrise: Optional[datetime] = ..., sunset: Optional[datetime] = ...) -> Optional[float]:
        ...
    
    def sun_transit(self) -> Optional[datetime]:
        ...
    


