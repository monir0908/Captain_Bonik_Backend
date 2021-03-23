from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .product import Product  # noqa: F401
    from .color import Color  # noqa: F401


class ProductAttribute(Base):
    id = Column(Integer, primary_key=True, index=True)
    
    # when child
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="product_attributes")

    # when child
    color_id = Column(Integer, ForeignKey("color.id"))
    color = relationship("Color", back_populates="product_attributes")
