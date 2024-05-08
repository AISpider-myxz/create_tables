from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base


class Strathbogie(Base):
    __tablename__ = 'strathbogie_shire_council'
    id = Column(Integer, primary_key=True, autoincrement=True)
    app_num = Column(String(255), nullable=False,unique=True)
    address = Column(String(255), nullable=True, server_default=None)
    description = Column(String(255), nullable=True, server_default=None)
    date = Column(Integer, nullable=True)
    documents = Column(Text, nullable=True,server_default=None)

    _tid = Column(String(255), nullable=False, server_default=None)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
