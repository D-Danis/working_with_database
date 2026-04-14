from sqlalchemy import Column, Integer, String, BigInteger, DateTime, func
from database import Base


class SpimexTradingResult(Base):
    __tablename__ = "spimex_trading_results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    exchange_product_id = Column(String(11), nullable=False)
    exchange_product_name = Column(String(500), nullable=False)
    oil_id = Column(String(4), nullable=False)
    delivery_basis_id = Column(String(3), nullable=False)
    delivery_basis_name = Column(String(300), nullable=False)
    delivery_type_id = Column(String(1), nullable=False)
    volume = Column(Integer, nullable=False)
    total = Column(BigInteger, nullable=False)
    count = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    created_on = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_on = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
