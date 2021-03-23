from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class Attribute(Base):
    id = Column(Integer, primary_key=True, index=True)
    attribute_name = Column(String, index=True)
    description = Column(String, index=True)