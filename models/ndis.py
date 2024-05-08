from sqlalchemy import Column, String, Text, Integer,DateTime,func 
from .metadata_base import Base


class ndis(Base):
    __tablename__ = 'ndis'

    id = Column(Integer, primary_key=True, autoincrement=True)
    app_id = Column(String(255), nullable=True, )
    app_title = Column(String(255), nullable=True, server_default=None)
    location = Column(String(255), nullable=True, server_default=None)
    building_type = Column(String(255), nullable=True, server_default=None)
    design_cat = Column(String(255), nullable=True, server_default=None)
    app_vacancy = Column(String(255), nullable=True, server_default=None)

    app_status = Column(String(255),nullable=True, server_default=None)
    room_num = Column(String(255), nullable=True, server_default=None)
    max_price_per_room = Column(String(255),nullable=True, server_default=None)

    firesprinklers = Column(String(255),nullable=True, server_default=None)
    app_ooa = Column(String(255),nullable=True, server_default=None)
    agent_email = Column(String(255),nullable=True, server_default=None)
    agent_phone = Column(String(255),nullable=True, server_default=None)
    internet_addr = Column(String(255),nullable=True, server_default=None)

    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())