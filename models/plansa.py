from sqlalchemy import Column, String, Text, Integer, DateTime, func, Date, UniqueConstraint
from .moretonbay import Base


class PlanSA(Base):
    __tablename__ = 'plansa'
    id = Column(Integer, primary_key=True)
    application_id = Column(String(128), nullable=False, unique=True)
    application_number = Column(String(128), nullable=True, server_default=None)
    assessment_pathway = Column(String(255), nullable=True, server_default=None)

    lodged = Column(Integer, nullable=True)

    council_area = Column(String(255), nullable=True, server_default=None)
    land = Column(String(128), nullable=True, server_default=None)
    plan_parcel = Column(String(128), nullable=True, default=None)
    names = Column(String(255), nullable=True, server_default=None)
    building_work = Column(Text, nullable=True, server_default=None)
    planning_consent_status = Column(String(128), nullable=True, default=None)
    planning_consent_contact = Column(String(128), nullable=True, default=None)

    planning_consent_date = Column(Integer, nullable=True)
    planning_consent_date_lodged = Column(Integer, nullable=True)
    planning_consent_date_submitted = Column(Integer, nullable=True)
    planning_consent_date_verified = Column(Integer, nullable=True)

    planning_consent_decision = Column(String(128), nullable=True, default=None)
    planning_consent_decision_authority = Column(String(255), nullable=True, server_default=None)
    building_consent_status = Column(String(128), nullable=True, default=None)
    building_consent_contact = Column(String(128), nullable=True, default=None)

    building_consent_date = Column(Integer, nullable=True)
    building_consent_date_lodged = Column(Integer, nullable=True)
    building_consent_date_submitted = Column(Integer, nullable=True)
    building_consent_date_verified = Column(Integer, nullable=True)

    building_consent_decision = Column(String(128), nullable=True, default=None)
    building_consent_decision_authority = Column(String(255), nullable=True, server_default=None)
    description = Column(Text, nullable=True, server_default=None)
    address = Column(String(255), nullable=True, server_default=None)
    documents = Column(Text, nullable=True, server_default=None)
    status = Column(String(255), nullable=True, server_default=None)

    _tid = Column(String(255), nullable=False, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
