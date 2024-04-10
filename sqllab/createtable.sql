DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakedate date,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  rms real,
  place text,
);