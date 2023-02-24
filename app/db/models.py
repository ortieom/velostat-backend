from sqlalchemy import Column, Integer, Text, Float, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class Counter(BaseModel):
    __tablename__ = "counters"
    name = Column(Text(10), primary_key=True)
    count_value = Column(Integer)


class StationsMetadataMsc(BaseModel):
    __tablename__ = "stations_metadata_msc"
    velobike_id = Column(Text(10), primary_key=True)
    lon = Column(Float(24))
    lat = Column(Float(24))


class TestdayMsc(BaseModel):
    __tablename__ = "testday_msc"
    id = Column(Integer, primary_key=True, autoincrement=True)
    velobike_id = Column(Text(10))
    timestamp = Column(DateTime)
    ordinarybikes_delta_taken = Column(Integer)
    ordinarybikes_delta_returned = Column(Integer)

Index("timestamp_msc", TestdayMsc.timestamp, TestdayMsc.velobike_id)


class StationsMetadataMrm(BaseModel):
    __tablename__ = "stations_metadata_mrm"
    velobike_id = Column(Text(10), primary_key=True)
    lon = Column(Float(24))
    lat = Column(Float(24))


class TestdayMrm(BaseModel):
    __tablename__ = "testday_mrm"
    id = Column(Integer, primary_key=True, autoincrement=True)
    velobike_id = Column(Text(10))
    timestamp = Column(DateTime)
    ordinarybikes_delta_taken = Column(Integer)
    ordinarybikes_delta_returned = Column(Integer)

Index("timestamp_mrm", TestdayMrm.timestamp, TestdayMrm.velobike_id)


class StationsMetadataNn(BaseModel):
    __tablename__ = "stations_metadata_nn"
    velobike_id = Column(Text(10), primary_key=True)
    lon = Column(Float(24))
    lat = Column(Float(24))


class TestdayNn(BaseModel):
    __tablename__ = "testday_nn"
    id = Column(Integer, primary_key=True, autoincrement=True)
    velobike_id = Column(Text(10))
    timestamp = Column(DateTime)
    ordinarybikes_delta_taken = Column(Integer)
    ordinarybikes_delta_returned = Column(Integer)

Index("timestamp_nn", TestdayNn.timestamp, TestdayNn.velobike_id)


class StationsMetadataTmn(BaseModel):
    __tablename__ = "stations_metadata_tmn"
    velobike_id = Column(Text(10), primary_key=True)
    lon = Column(Float(24))
    lat = Column(Float(24))


class TestdayTmn(BaseModel):
    __tablename__ = "testday_tmn"
    id = Column(Integer, primary_key=True, autoincrement=True)
    velobike_id = Column(Text(10))
    timestamp = Column(DateTime)
    ordinarybikes_delta_taken = Column(Integer)
    ordinarybikes_delta_returned = Column(Integer)

Index("timestamp_tmn", TestdayTmn.timestamp, TestdayTmn.velobike_id)
