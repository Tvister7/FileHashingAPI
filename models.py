from typing import Optional
from sqlalchemy.dialects.postgresql import UUID
from db_config import Base
from sqlalchemy import Integer, Column, String
from db_config import db_session

db = db_session.session_factory()


def get_hash_by_id(hash_id: str) -> Optional[str]:
    hash_by_id = db.query(CryptoFile.hash).filter(CryptoFile.file_id == hash_id).first()
    if hash_by_id:
        return hash_by_id
    else:
        return None


def create_crypto(file_id, file_hash: str) -> None:
    db_file_hash = CryptoFile(hash=file_hash, file_id=file_id)
    db.add(db_file_hash)
    db.commit()
    db.refresh(db_file_hash)


class CryptoFile(Base):
    __tablename__ = "md5files"
    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(UUID)
    hash = Column(String)


