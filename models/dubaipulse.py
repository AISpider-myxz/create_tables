from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base

class Dubaipulse(Base):
    __tablename__ = 'dubaipulse'
    id = Column(Integer, primary_key=True)
    property_id = Column(Text, nullable=True)
    area_id = Column(Text, nullable=True)
    zone_id = Column(Text, nullable=True)
    area_name_ar = Column(Text, nullable=True)
    area_name_en = Column(Text, nullable=True)
    land_number = Column(Text, nullable=True)
    land_sub_number = Column(Text, nullable=True)
    building_number = Column(Text, nullable=True)
    common_area = Column(Text, nullable=True)
    actual_common_area = Column(Text, nullable=True)
    floors = Column(Text, nullable=True)
    rooms = Column(Text, nullable=True)
    rooms_ar = Column(Text, nullable=True)
    rooms_en = Column(Text, nullable=True)
    car_parks = Column(Text, nullable=True)
    built_up_area = Column(Text, nullable=True)
    bld_levels = Column(Text, nullable=True)
    shops = Column(Text, nullable=True)
    flats = Column(Text, nullable=True)
    offices = Column(Text, nullable=True)
    swimming_pools = Column(Text, nullable=True)
    elevators = Column(Text, nullable=True)
    actual_area = Column(Text, nullable=True)
    property_type_id = Column(Text, nullable=True)
    property_type_ar = Column(Text, nullable=True)
    property_type_en = Column(Text, nullable=True)
    property_sub_type_id = Column(Text, nullable=True)
    property_sub_type_ar = Column(Text, nullable=True)
    property_sub_type_en = Column(Text, nullable=True)
    parent_property_id = Column(Text, nullable=True)
    creation_date = Column(Integer, nullable=True)  # time
    parcel_id = Column(Text, nullable=True)
    is_free_hold = Column(Text, nullable=True)
    is_lease_hold = Column(Text, nullable=True)
    is_registered = Column(Text, nullable=True)
    pre_registration_number = Column(Text, nullable=True)
    master_project_id = Column(Text, nullable=True)
    master_project_en = Column(Text, nullable=True)
    master_project_ar = Column(Text, nullable=True)
    project_id = Column(Text, nullable=True)
    project_name_ar = Column(Text, nullable=True)
    project_name_en = Column(Text, nullable=True)
    land_type_id = Column(Text, nullable=True)
    land_type_ar = Column(Text, nullable=True)
    land_type_en = Column(Text, nullable=True)
    company_name_ar = Column(Text, nullable=True)
    company_name_en = Column(Text, nullable=True)
    phone = Column(Text, nullable=True)
    email = Column(Text, nullable=True)
    latitude = Column(Text, nullable=True)
    longitude = Column(Text, nullable=True)
    procedure_id = Column(Text, nullable=True)
    procedure_name_ar = Column(Text, nullable=True)
    procedure_name_en = Column(Text, nullable=True)
    procedure_year = Column(Text, nullable=True)
    procedure_number = Column(Text, nullable=True)
    instance_date = Column(Integer, nullable=True)  # time
    actual_worth = Column(Text, nullable=True)
    row_status_code = Column(Text, nullable=True)
    procedure_area = Column(Text, nullable=True)
    property_total_value = Column(Text, nullable=True)
    first_date_of_month = Column(Integer, nullable=True)  # time
    all_monthly_index = Column(Text, nullable=True)
    all_quarterly_index = Column(Text, nullable=True)
    all_yearly_index = Column(Text, nullable=True)
    flat_monthly_index = Column(Text, nullable=True)
    flat_quarterly_index = Column(Text, nullable=True)
    flat_yearly_index = Column(Text, nullable=True)
    villa_monthly_index = Column(Text, nullable=True)
    villa_quarterly_index = Column(Text, nullable=True)
    villa_yearly_index = Column(Text, nullable=True)
    all_monthly_price_index = Column(Text, nullable=True)
    all_quarterly_price_index = Column(Text, nullable=True)
    all_yearly_price_index = Column(Text, nullable=True)
    flat_monthly_price_index = Column(Text, nullable=True)
    flat_quarterly_price_index = Column(Text, nullable=True)
    flat_yearly_price_index = Column(Text, nullable=True)
    villa_monthly_price_index = Column(Text, nullable=True)
    villa_quarterly_price_index = Column(Text, nullable=True)
    villa_yearly_price_index = Column(Text, nullable=True)
    participant_id = Column(Text, nullable=True)
    authority_id = Column(Text, nullable=True)
    license_number = Column(Text, nullable=True)
    commerce_registry_number = Column(Text, nullable=True)
    chamber_commerce_number = Column(Text, nullable=True)
    trade_name_arabic = Column(Text, nullable=True)
    trade_name_english = Column(Text, nullable=True)
    issue_date = Column(Text, nullable=True)
    expiry_date = Column(Text, nullable=True)
    cancel_date = Column(Text, nullable=True)
    status_id = Column(Text, nullable=True)
    status_arabic = Column(Text, nullable=True)
    status_english = Column(Text, nullable=True)
    legal_type_id = Column(Text, nullable=True)
    legal_type_arabic = Column(Text, nullable=True)
    legal_type_english = Column(Text, nullable=True)
    rent_contract_no = Column(Text, nullable=True)
    print_rmker_arabic = Column(Text, nullable=True)
    activity_type_id = Column(Text, nullable=True)
    ded_activity_code = Column(Text, nullable=True)
    activity_name_ar = Column(Text, nullable=True)
    activity_name_en = Column(Text, nullable=True)
    fz_company_number = Column(Text, nullable=True)
    fz_company_name_ar = Column(Text, nullable=True)
    fz_company_name_en = Column(Text, nullable=True)
    license_source_id = Column(Text, nullable=True)
    license_source_ar = Column(Text, nullable=True)
    license_source_en = Column(Text, nullable=True)
    license_issue_date = Column(Integer, nullable=True)  # time
    license_expiry_date = Column(Integer, nullable=True)  # time
    webpage = Column(Text, nullable=True)
    transaction_id = Column(Text, nullable=True)
    trans_group_id = Column(Text, nullable=True)
    trans_group_ar = Column(Text, nullable=True)
    trans_group_en = Column(Text, nullable=True)
    property_usage_ar = Column(Text, nullable=True)
    property_usage_en = Column(Text, nullable=True)
    reg_type_id = Column(Text, nullable=True)
    reg_type_ar = Column(Text, nullable=True)
    reg_type_en = Column(Text, nullable=True)
    building_name_ar = Column(Text, nullable=True)
    building_name_en = Column(Text, nullable=True)
    project_number = Column(Text, nullable=True)
    nearest_landmark_ar = Column(Text, nullable=True)
    nearest_landmark_en = Column(Text, nullable=True)
    nearest_metro_ar = Column(Text, nullable=True)
    nearest_metro_en = Column(Text, nullable=True)
    nearest_mall_ar = Column(Text, nullable=True)
    nearest_mall_en = Column(Text, nullable=True)
    has_parking = Column(Text, nullable=True)
    meter_sale_price = Column(Text, nullable=True)
    rent_value = Column(Text, nullable=True)
    meter_rent_price = Column(Text, nullable=True)
    no_of_parties_role_1 = Column(Text, nullable=True)
    no_of_parties_role_2 = Column(Text, nullable=True)
    no_of_parties_role_3 = Column(Text, nullable=True)
    service_year = Column(Text, nullable=True)
    service_month = Column(Text, nullable=True)
    service_name_ar = Column(Text, nullable=True)
    service_name_en = Column(Text, nullable=True)
    service_location_ar = Column(Text, nullable=True)
    service_location_en = Column(Text, nullable=True)
    total_no_of_tickets = Column(Text, nullable=True)
    average_wating_time = Column(Text, nullable=True)
    target_waiting_time = Column(Text, nullable=True)
    grandparent_property_id = Column(Text, nullable=True)
    request_id = Column(Text, nullable=True)
    percent_waiting_time_in_target = Column(Text, nullable=True)
    average_service_time = Column(Text, nullable=True)
    target_service_time = Column(Text, nullable=True)
    percent_service_time_in_target = Column(Text, nullable=True)
    course_code = Column(Text, nullable=True)
    cource_title_ar = Column(Text, nullable=True)
    cource_title_en = Column(Text, nullable=True)
    course_date = Column(Integer, nullable=True)  # time
    course_to = Column(Integer, nullable=True)  # time
    course_time_from = Column(Text, nullable=True)
    course_time_to = Column(Text, nullable=True)
    age_group = Column(Text, nullable=True)
    trainee_gender = Column(Text, nullable=True)
    no_of_trainees = Column(Text, nullable=True)
    munc_zip_code = Column(Text, nullable=True)
    munc_number = Column(Text, nullable=True)
    separated_from = Column(Text, nullable=True)
    separated_reference = Column(Text, nullable=True)
    unit_number = Column(Text, nullable=True)
    unit_balcony_area = Column(Text, nullable=True)
    unit_parking_number = Column(Text, nullable=True)
    parking_allocation_type = Column(Text, nullable=True)
    parking_allocation_type_ar = Column(Text, nullable=True)
    parking_allocation_type_en = Column(Text, nullable=True)
    floor = Column(Text, nullable=True)
    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())