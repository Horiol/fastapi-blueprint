from typing import Optional

from sqlalchemy import Column, ForeignKey, Integer, String
from models.base import Base


class Location(Base):
    __tablename__ = "locations"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False, unique=True)

    # tasks: list["Task"] = relationship("Task", lazy="joined", back_populates="location")


class Task(Base):
    __tablename__ = "tasks"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False)
    location_id: Optional[int] = Column(Integer, ForeignKey(Location.id), nullable=True)

    # location: Optional[Location] = relationship(Location, lazy="joined", back_populates="tasks")
