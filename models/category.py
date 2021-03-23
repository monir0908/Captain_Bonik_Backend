from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .product import Product  # noqa: F401


class Category(Base):
    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(String)

    # when parent
    products = relationship("Product", back_populates="category")