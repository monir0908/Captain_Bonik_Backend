from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Color(Base):
    id = Column(Integer, primary_key=True, index=True)
    color_name = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(String)

    # when parent
    product_attributes = relationship("ProductAttribute", back_populates="color")