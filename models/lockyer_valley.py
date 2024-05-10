from sqlalchemy import Column, String, Text, Integer, DateTime, func, UniqueConstraint
from .metadata_base import Base


class LockyerValley(Base):
    __tablename__ = 'lockyer_valley'
    id = Column(Integer, primary_key=True)
    application_id = Column(String(255),unique=True, nullable=False)
    application_group = Column(String(255), nullable=True, server_default=None)
    application_type = Column(String(255), nullable=True, server_default=None)
    assessment_type = Column(String(255), nullable=True, server_default=None)
    lodgement_date = Column(Integer, nullable=True,)
    description = Column(Text, nullable=True)
    status = Column(String(255), nullable=True, default=None)
    decision = Column(String(255), nullable=True, server_default=None)
    finalised_date = Column(Integer,nullable=True,)
    associated_name = Column(String(255), nullable=True, server_default=None)
    association = Column(String(255), nullable=True, server_default=None)
    address = Column(Text, nullable=True, server_default=None)
    land_description = Column(Text, nullable=True, server_default=None)
    documents = Column(Text, nullable=True, server_default=None)

    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

  
