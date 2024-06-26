from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base


class Whitehorse(Base):
    __tablename__ = 'whitehorse'

    id = Column(Integer, primary_key=True, autoincrement=True)

    app_number = Column(String(64), nullable=False, unique=True)
    name_details = Column(Text, nullable=True, server_default=None)
    decision_type = Column(String(256), nullable=True, server_default=None)
    decision_date = Column(Integer, nullable=True,)
    app_class = Column(String(256), nullable=True, server_default=None)
    app_type = Column(String(64), nullable=True, server_default=None)
    app_description = Column(String(256), nullable=True, server_default=None)
    location = Column(String(256), nullable=True, server_default=None)
    status = Column(String(256), nullable=True, server_default=None)
    current_decision = Column(Text, nullable=True, server_default=None)
    application_date = Column(Integer, nullable=True,)
    lodgement_date = Column(Integer, nullable=True, )
    to_be_commenced_by_date = Column(Integer, nullable=True,)
    expiry_date = Column(Integer, nullable=True,)
    office = Column(String(256), nullable=True, server_default=None)
    start_date = Column(Integer, nullable=True, )
    document = Column(Text, nullable=True, server_default=None)

    _tid = Column(String(255), nullable=False,server_default=None )
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
