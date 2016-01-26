-- Images Table
drop table if exists tbl_images;
create table tbl_images (
  id integer primary key autoincrement,
  title string not null,
  url string,
  timestamp  string DEFAULT CURRENT_TIMESTAMP
);

--ALTER TABLE tbl_images ALTER COLUMN url SET DEFAULT '#';

-- Motto 's Tabel
drop table if exists tbl_motto;
create table tbl_motto (
  id integer primary key autoincrement,
  title string not null,
  url string,
  timestamp  string DEFAULT CURRENT_TIMESTAMP
);

--ALTER TABLE tbl_motto ALTER COLUMN url SET DEFAULT '#';

-- Advice 's Tabel
drop table if exists tbl_advice;
create table tbl_advice (
  id integer primary key autoincrement,
  title string not null,
  url string,
  timestamp  string DEFAULT CURRENT_TIMESTAMP
);

--ALTER TABLE tbl_advice ALTER COLUMN url SET DEFAULT '#';