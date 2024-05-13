from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base

class Realestate(Base):
    __tablename__ = 'realestate'

    id = Column(Integer, primary_key=True)
    name = Column(String(512), nullable=True, server_default=None)
    area = Column(String(512), nullable=True)
    address = Column(String(512), nullable=True, server_default=None)
    size = Column(String(512), nullable=True)
    href = Column(Text, nullable=True)
    style = Column(String(512), nullable=True)
    type = Column(String(126), nullable=True)
    price = Column(String(512), nullable=True)
    completion_date = Column(String(126), nullable=True)
    working = Column(String(512), nullable=True)
    introduction = Column(Text, nullable=True)
    description_content = Column(Text, nullable=True)
    bedrooms = Column(String(126), nullable=True)
    bathroom = Column(String(126), nullable=True)
    parkingspaces = Column(String(126), nullable=True)
    price_else = Column(String(512), nullable=True)
    address_else = Column(String(512), nullable=True)
    bedrooms_else = Column(String(126), nullable=True)
    bathroom_else = Column(String(126), nullable=True)
    parkingspaces_else = Column(String(126), nullable=True)
    href_else = Column(Text, nullable=False)
    style_else = Column(String(512), nullable=True)
    title_else = Column(String(512), nullable=True)
    area_else = Column(String(126), nullable=True)
    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())