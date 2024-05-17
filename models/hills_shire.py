from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base


class HillShire(Base):
    __tablename__ = 'hill_shire'

    id = Column(Integer, primary_key=True)
    application_id = Column(String(255), unique=True, nullable=False)
    application_num = Column(String(255), nullable=True, server_default=None)
    lodgement_date = Column(Integer, nullable=True)
    expiry_date = Column(Integer, nullable=True)
    status = Column(String(255), nullable=True, server_default=None)
    address = Column(Text, nullable=True, server_default=None)
    decision = Column(String(255), nullable=True, server_default=None)
    payment_ref_num = Column(String(255), nullable=True, server_default=None)
    costs = Column(String(255), nullable=True, server_default=None)
    documents = Column(Text, nullable=True, server_default=None)
    letters = Column(Text, nullable=True, server_default=None)

    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, server_default=func.now(), onupdate=func.now())