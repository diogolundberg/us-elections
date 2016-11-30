create table us_elections (
    id serial not null,
    county varchar(255),
    fips varchar(255),
    cand varchar(255),
    st varchar(255),
    votes bigint,
    total_votes bigint,
    lead varchar(255),
    primary key (id)
)
