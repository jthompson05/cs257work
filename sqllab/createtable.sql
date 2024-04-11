DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakedate timestamp,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  rms real,
  place text
);