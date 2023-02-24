create table testday_msc
(
    velobike_id char(10) null,
    timestamp timestamp null,
    ordinarybikes_delta_taken smallserial,
    ordinarybikes_delta_returned smallserial
);

create index timestamp_msc
    on testday_msc (timestamp, velobike_id);

create table stations_metadata_msc
(
    velobike_id char(10) PRIMARY KEY,
    lon float(24),
    lat float(24)
);

create table testday_nn
(
    velobike_id char(10) null,
    timestamp timestamp null,
    ordinarybikes_delta_taken smallserial,
    ordinarybikes_delta_returned smallserial
);

create index timestamp_nn
    on testday_nn (timestamp, velobike_id);

create table stations_metadata_nn
(
    velobike_id char(10) PRIMARY KEY,
    lon float(24),
    lat float(24)
);

create table testday_mrm
(
    velobike_id char(10) null,
    timestamp timestamp null,
    ordinarybikes_delta_taken smallserial,
    ordinarybikes_delta_returned smallserial
);

create index timestamp_mrm
    on testday_mrm (timestamp, velobike_id);

create table stations_metadata_mrm
(
    velobike_id char(10) PRIMARY KEY,
    lon float(24),
    lat float(24)
);

create table testday_tmn
(
    velobike_id char(10) null,
    timestamp timestamp null,
    ordinarybikes_delta_taken smallserial,
    ordinarybikes_delta_returned smallserial
);

create index timestamp_tmn
    on testday_tmn (timestamp, velobike_id);

create table stations_metadata_tmn
(
    velobike_id char(10) PRIMARY KEY,
    lon float(24),
    lat float(24)
);

create table counters
(
    name char(20),
    count_value integer
);
