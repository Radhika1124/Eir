from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    age = Column(Integer)
    gender = Column(String(20))
    medical_history = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    prescriptions = relationship("Prescription", back_populates="patient")


class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    original_image_path = Column(String(255))
    ocr_text = Column(Text)
    extracted_medications = Column(Text) # JSON string representation
    confidence_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    patient = relationship("Patient", back_populates="prescriptions")


class FederatedNode(Base):
    __tablename__ = "federated_nodes"
    
    id = Column(Integer, primary_key=True, index=True)
    node_name = Column(String(100), unique=True, index=True)
    status = Column(String(50)) # e.g., "active", "training", "offline"
    last_sync = Column(DateTime, default=datetime.utcnow)
    data_samples_count = Column(Integer, default=0)
