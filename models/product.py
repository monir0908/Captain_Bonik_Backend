from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .category import Category  # noqa: F401


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    description = Column(String)
    created_at = Column(String)

    # when child
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="products")



    # when parent
    product_attributes = relationship("ProductAttribute", back_populates="product")