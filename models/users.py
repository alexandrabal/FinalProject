from sqlalchemy import Column, func
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from __init__ import Base

#tablename is
#this class in inherited to across all

class User(Base):

""""tablename is the name of the table. static attributes are given below to reflect table columns"""

    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    first_name = Column(VARCHAR(225), nullable=False)
    last_name = Column(VARCHAR(225), nullabl=False)
    email = Column(VARCHAR(255), nullable = False, unique = True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), server_onupdate=func.now())




