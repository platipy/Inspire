
drop table if exists users;
create table users (
    username string primary key,
    visible_name string not null,
    password string not null
);