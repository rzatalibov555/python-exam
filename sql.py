
# select distinct name, age from autor    // distinct - dublikatlari gosterme

# create table Player (
# 	name varchar(255),
# 	surname varchar(255),
# 	position varchar(255),
# 	age int,
# 	cup_count int,
# 	point int
# )



# select * from Player



# INSERT INTO Player
# VALUES ('Rahim', 'Mammadov', 'demo3', 23, 5, 99)



# select name from Player



# select * from Player where name = 'Rza' AND surname = 'Talibov' or  age = '31'
# select * from Player where (name = 'Rza' AND surname = 'Talibov') or  age = '31'



# select cup_count from Player order by name asc



# select * from Player where (position = 'Rza' AND cup_count = 'Talibov') order by point desc



# select * from Player where (position = 'demo3' AND cup_count = '5') order by point desc





# ===================================================================

# postgressql
# id serial (serial == autoincrenement)

# https://www.w3schools.com/sql/sql_wildcards.asp



# WHERE CustomerName LIKE 'a__%'

# drop table player



# ========================================================


# -- select * from player
 
# -- create table playerBackup(
# -- 	id serial primary key not null,
# -- 	name varchar(200) not null,
# -- 	surname varchar(200) not null,
# -- 	point int null
# -- )
 
# -- select * from playerBackup
 
# -- select * into playerBckp from player
 
# -- select * from playerBckp
 
 
# -- select * into playerBackupTable from player
 
# -- select * from PLAYERBACKUPTABLE
 
 
# -- select * into backupPLayer from player
 
# -- select * from backupPLayer
 
 
# -- insert into playerBackup
# -- select * from player
# -- where point > 50
 
 
# -- select * from playerBackup
 
 
 
# -- create table users(
# -- 	userId serial primary key not null,
# -- 	username varchar(300) not null
# -- )
 
 
# -- create table profiles(
# -- 	profileId serial primary key not null,
# -- 	profileName varchar(300) not null,
# -- 	profileSurname varchar(300) not null,
# -- 	userId int,
# -- 	Foreign Key (userId) References users(userId)
# -- )
 
 
# -- select * from users
 
# -- insert into users(username) values('Fuad');
# -- insert into users(username) values('Eli');
# -- insert into users(username) values('Ferid');
 
# -- select * from profiles
 
 
# -- insert into profiles(profilename, profilesurname, userid) values('Fuad', 'Huseynov', 1);
# -- insert into profiles(profilename, profilesurname, userid) values('Eli', 'Memmedov', 2);
# -- insert into profiles(profilename, profilesurname, userid) values('Ferid', 'Haciyev', 3);
 
# -- SELECT * FROM users
# -- FULL OUTER JOIN profiles
# -- ON users.userid = profiles.userid
 
 
# -- SELECT *,
# -- CASE
# --     WHEN point > 30 THEN 'The point is greater than 30'
# --     WHEN point = 30 THEN 'The point is 30'
# --     ELSE 'The point is under 30'
# -- END AS pointText
# -- FROM player;
 
 
# -- Alter table player
# -- add birthday date
 
 
# -- select * from player
 
 
# -- insert into player(name, surname, point, birthday) values('Neymar', 'Neymar', 98, '1991-02-05')
 
# -- select * from player
 
 
# -- alter table player
# -- drop birthday 



# =============================================================================



# -- select * from person
# -- where age in (
# -- 	select max(age) from person
# -- ) or age in (
# -- 	select min(age) from person
# -- )
 
 
# -- select * from person
# -- where age between (select avg(age) from person) and (select max(age) from person)
 
# -- select surname as username, age as birth
# -- from person
 
 
# -- select * from person
 
# -- select id, concat(surname, ' ', email) as userData from person
 
 
# -- create table player(
# -- 	id serial primary key not null,
# -- 	name varchar(200) not null,
# -- 	surname varchar(200) not null,
# -- 	point int not null check (point<=100)
# -- )
 
 
# -- Insert into player (name, surname, point) values('Ronaldo', 'Cristiano', '99');
# -- Insert into player (name, surname, point) values('Leo', 'Messi', '100');
 
# -- select * from person
# -- INNER JOIN player On person.id=player.id
 
 
# -- select * from person
# -- left join player on player.id=person.id
 
# -- select * from person
# -- right join player on player.id=person.id
 
# -- select * from person
# -- full outer join player on player.id=person.id
 
 
# -- insert into player(id, name, surname, point) values(70, 'Fuad', 'Huseynov', 0)
 
# -- select * from player
 
 
 
# -- select surname, email from person
# -- where id in (1, 2, 3)
# -- Union 
# -- select name, surname from player
# -- where point > 99
 
# -- insert into player values (40, 'Oktay', 'Huseynov', 80)
 
# -- select * from player;
 
# -- select sum(point) as sumPoint, surname from player
# -- group by surname
# -- having sum(point) >= 80
 
# -- select id, email from person
# -- where exists (select id from player where player.id=person.id)
 
 
# -- select * from person
# -- where id = any(select id from player)
 
# -- select * from person
# -- where id = all(select id from player)