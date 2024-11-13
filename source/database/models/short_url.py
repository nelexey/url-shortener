from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.sql import func

from source.database.main import Database

class ShortURL(Database.BASE):
    __tablename__ = 'short_urls'

    id = Column(Integer, primary_key=True)
    original_url = Column(String(2048), nullable=False)  # Длинный URL
    short_code = Column(String(6), unique=True, nullable=False)  # Сокращённый код
    clicks = Column(BigInteger, default=0)  # Количество переходов
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Дата создания

    def __repr__(self):
        return f"<ShortURL(id={self.id}, short_code='{self.short_code}', original_url='{self.original_url}', clicks={self.clicks})>"
