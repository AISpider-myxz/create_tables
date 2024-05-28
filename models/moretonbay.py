
from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base

class MoretonBay(Base):
    __tablename__ = 'moretonbay'

    id = Column(Integer, primary_key=True, autoincrement=True,)
    application_id = Column(String(255), nullable=True,server_default=None)
    da_number = Column(String(255), nullable=False,unique=True)
    lodged_date = Column(Integer, nullable=True)
    description = Column(Text, nullable=True,server_default=None)
    site_name = Column(String(255), nullable=True,server_default=None)
    statuses = Column(String(255), nullable=True,server_default=None)
    properties = Column(Text, nullable=True,server_default=None)
    parcel_lot_plan = Column(Text, nullable=True,server_default=None)
    activity_level = Column(String(255), nullable=True,server_default=None)
    applicant_name = Column(String(255), nullable=True,server_default=None)
    documents = Column(Text, nullable=True,server_default=None)

    _tid = Column(String(255), nullable=False, server_default=None)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())