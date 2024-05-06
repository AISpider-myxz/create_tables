from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base

class Dubai(Base):
    __tablename__ = 'dubai'
    id = Column(Integer, primary_key=True)
    app_number = Column(String(128), nullable=True)
    transaction_date = Column(Integer, nullable=True, server_default=None)
    transaction_type = Column(Text, nullable=True)
    transaction_sub_type = Column(Text, nullable=True)
    registration_type = Column(Text, nullable=True)
    free_hold = Column(Text, nullable=True)
    usage_ = Column(Text, nullable=True)
    area_ = Column(Text, nullable=True)
    property_type = Column(Text, nullable=True)
    property_sub_type = Column(Text, nullable=True)
    amount_ = Column(Text, nullable=True)
    transaction_size = Column(Text, nullable=True)
    property_size = Column(Text, nullable=True)
    rooms = Column(Text, nullable=True)
    parking = Column(Text, nullable=True)
    nearest_metro = Column(Text, nullable=True)
    nearest_mall = Column(Text, nullable=True)
    nearest_landmark = Column(Text, nullable=True)
    no_of_buyer = Column(Text, nullable=True)
    no_of_seller = Column(Text, nullable=True)
    master_project = Column(Text, nullable=True)
    project_ = Column(Text, nullable=True)
    registration = Column(Text, nullable=True)
    start_date = Column(Integer, nullable=True, server_default=None)
    end_date = Column(Integer, nullable=True, server_default=None)
    contract_amount = Column(Text, nullable=True)
    annual_amount = Column(Text, nullable=True)
    number_rooms = Column(Text, nullable=True)
    no_of_units = Column(Text, nullable=True)
    project_name = Column(Text, nullable=True)
    developer_number = Column(String(128), nullable=True)
    developer_name = Column(Text, nullable=True)
    adeption_date = Column(Integer, nullable=True, server_default=None)
    project_type = Column(Text, nullable=True)
    project_value = Column(Text, nullable=True)
    escrow_number = Column(String(128), nullable=True)
    project_status = Column(Text, nullable=True)
    completed = Column(Text, nullable=True)
    inspection_date = Column(Integer, nullable=True, server_default=None)
    completed_date = Column(Integer, nullable=True, server_default=None)
    description = Column(Text, nullable=True, server_default=None)
    zone_authority = Column(Text, nullable=True)
    total_lands = Column(Text, nullable=True)
    total_buildings = Column(Text, nullable=True)
    total_villas = Column(Text, nullable=True)
    total_units = Column(Text, nullable=True)
    property_total_type = Column(Text, nullable=True)
    procedure_year = Column(String(128), nullable=True)
    land_number = Column(String(128), nullable=True)
    land_sub_number = Column(String(128), nullable=True)
    land_type = Column(Text, nullable=True)
    registration_number = Column(String(128), nullable=True)
    zip_code = Column(Text, nullable=True)
    municipality_number = Column(String(128), nullable=True)
    separated_form = Column(Text, nullable=True)
    separated_reference = Column(Text, nullable=True)
    project_number = Column(String(128), nullable=True)
    zone_ = Column(Text, nullable=True)
    unit_number = Column(String(128), nullable=True)
    balcony_area = Column(Text, nullable=True)
    common_area = Column(Text, nullable=True)
    actual_common_area = Column(Text, nullable=True)
    floor_ = Column(Text, nullable=True)
    room_type = Column(Text, nullable=True)
    parking_allocation_type = Column(Text, nullable=True)
    creation_date = Column(Integer, nullable=True, server_default=None)
    lease_hold = Column(Text, nullable=True)
    building_number = Column(Text, nullable=True)
    broker_number = Column(String(128), nullable=True)
    broker_name = Column(Text, nullable=True)
    gender_ = Column(Text, nullable=True)
    website = Column(Text, nullable=True)
    phone = Column(String(126), nullable=True)
    fax_ = Column(Text, nullable=True)
    real_estate_number = Column(String(128), nullable=True)
    real_estate_name = Column(Text, nullable=True)
    registration_date = Column(Integer, nullable=True, server_default=None)
    license_source = Column(Text, nullable=True)
    license_type = Column(Text, nullable=True)
    license_number = Column(String(128), nullable=True)
    license_lssue_date = Column(Integer, nullable=True, server_default=None)
    license_expiry_date = Column(Integer, nullable=True, server_default=None)
    chamber_commerce = Column(Text, nullable=True)
    
    _tid = Column(String(255), nullable=False,server_default=None )
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())