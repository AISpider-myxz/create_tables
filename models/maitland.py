from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base

class Maitland(Base):
    __tablename__ = 'maitland'

    id = Column(Integer, primary_key=True, autoincrement=True)

    type_ = Column(String(255), nullable=True, server_default=None)
    app_num = Column(String(255), nullable=False, unique=True)
    lodged = Column(Integer, nullable=True, server_default=None)
    work_value = Column(String(255), nullable=True, server_default=None)
    officer = Column(String(255),nullable=True, server_default=None)
    status_ = Column(String(255),nullable=True, server_default=None)

    property_ = Column(Text, nullable=True, server_default=None)
    title = Column(String(255), nullable=True, server_default=None)

    applicant = Column(Text, nullable=True, server_default=None)
    pca = Column(Text, nullable=True, server_default=None)

    details = Column(Text, nullable=True, server_default=None)
    determination = Column(String(255), nullable=True, server_default=None)
    determined = Column(Integer, nullable=True, server_default=None)

    updated_on = Column(Integer, nullable=True, server_default=None)
    notification_from = Column(Integer, nullable=True, server_default=None)
    notification_to = Column(Integer, nullable=True, server_default=None)

    _tid = Column(String(255), nullable=False, server_default=None)
    document = Column(Text, nullable=True, server_default=None)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
