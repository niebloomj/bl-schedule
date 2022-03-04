"""
This type stub file was generated by pyright.
"""

from datetime import datetime
from typing import Optional
from zmanim.astronomical_calendar import AstronomicalCalendar

class ZmanimCalendar(AstronomicalCalendar):
    def __init__(self, candle_lighting_offset: int = ..., *args, **kwargs) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def elevation_adjusted_sunrise(self) -> Optional[datetime]:
        ...
    
    def hanetz(self) -> Optional[datetime]:
        ...
    
    def elevation_adjusted_sunset(self) -> Optional[datetime]:
        ...
    
    def shkia(self) -> Optional[datetime]:
        ...
    
    def tzais(self, opts: dict = ...) -> Optional[datetime]:
        ...
    
    def tzais_72(self) -> Optional[datetime]:
        ...
    
    def alos(self, opts: dict = ...) -> Optional[datetime]:
        ...
    
    def alos_72(self) -> Optional[datetime]:
        ...
    
    def chatzos(self) -> Optional[datetime]:
        ...
    
    def candle_lighting(self) -> Optional[datetime]:
        ...
    
    def sof_zman_shma(self, day_start: datetime, day_end: datetime) -> datetime:
        ...
    
    def sof_zman_shma_gra(self) -> datetime:
        ...
    
    def sof_zman_shma_mga(self) -> datetime:
        ...
    
    def sof_zman_tfila(self, day_start: Optional[datetime], day_end: Optional[datetime]) -> Optional[datetime]:
        ...
    
    def sof_zman_tfila_gra(self) -> Optional[datetime]:
        ...
    
    def sof_zman_tfila_mga(self) -> Optional[datetime]:
        ...
    
    def mincha_gedola(self, day_start: Optional[datetime] = ..., day_end: Optional[datetime] = ...) -> Optional[datetime]:
        ...
    
    def mincha_ketana(self, day_start: Optional[datetime] = ..., day_end: Optional[datetime] = ...) -> Optional[datetime]:
        ...
    
    def plag_hamincha(self, day_start: Optional[datetime] = ..., day_end: Optional[datetime] = ...) -> Optional[datetime]:
        ...
    
    def shaah_zmanis(self, day_start: Optional[datetime], day_end: Optional[datetime]) -> Optional[float]:
        ...
    
    def shaah_zmanis_gra(self) -> Optional[float]:
        ...
    
    def shaah_zmanis_mga(self) -> Optional[float]:
        ...
    
    def shaah_zmanis_by_degrees_and_offset(self, degrees: float, offset: float) -> Optional[float]:
        ...
    
    def is_assur_bemelacha(self, current_time: datetime, tzais=..., in_israel: Optional[bool] = ...): # -> bool:
        ...
    

