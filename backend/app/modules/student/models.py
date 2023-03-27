import os
import sys
from dotenv import load_dotenv

from app.core.config.db.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Date


class Student(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    subject = Column(Subject, uselist=True)
