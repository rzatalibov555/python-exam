
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