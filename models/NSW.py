from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base


class NSW_(Base):
    __tablename__ = 'NSW_'

    id = Column(Integer, primary_key=True, autoincrement=True)

    Record_Type = Column(String(255), nullable=True,server_default=None)
    File_Type = Column(String(255),nullable=True, server_default=None)
    District_Code = Column(String(255), nullable=True, server_default=None)
    Download_Date_time = Column(String(255),nullable=True, server_default=None)
    Submitter_userid = Column(String(255),nullable=True, server_default=None)
    model_pro = Column(String(255),nullable=True, server_default=None)
    model_promax = Column(String(255),nullable=True, server_default=None)
    street_no = Column(String(255),nullable=True, server_default=None)
    street_name = Column(String(255),nullable=True, server_default=None)
    suburb_ = Column(String(255),nullable=True, server_default=None)
    postcode_ = Column(String(255),nullable=True, server_default=None)
    area_ = Column(String(255),nullable=True, server_default=None)
    area_type = Column(String(255),nullable=True, server_default=None)
    purchase_date = Column(String(255),nullable=True, server_default=None)
    settlement_date = Column(String(255),nullable=True, server_default=None)
    price_ = Column(String(255),nullable=True, server_default=None)
    zoning_ = Column(String(255),nullable=True, server_default=None)
    nature_of_property = Column(String(255),nullable=True, server_default=None)
    Primiary_Purchase = Column(String(255),nullable=True, server_default=None)
    Strata_Lot_Number = Column(String(255),nullable=True, server_default=None)
    Component_code = Column(String(255),nullable=True, server_default=None)
    Sale_Code = Column(String(255),nullable=True, server_default=None)
    interest_of_Sale = Column(String(255),nullable=True, server_default=None)
    Dealing_Number = Column(String(255),nullable=True, server_default=None)

    _tid = Column(String(255), nullable=False, server_default=None)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


