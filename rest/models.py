from sqlalchemy import Column, String, UniqueConstraint, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
import uuid
from sqlalchemy.dialects.postgresql import UUID


engine = create_engine('postgresql://XXXXXX:XXXXXX@localhost:5432/numbers_db')

Base = declarative_base()
metadata = MetaData()


class Numbers(Base):
    __tablename__ = 'numbers_id'
    number_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    auto_numbers = Column(String, unique=True)
    __table_args__ = (UniqueConstraint('auto_numbers', name='_name_auto_numbers_uc'),)


Base.metadata.create_all(bind=engine)
