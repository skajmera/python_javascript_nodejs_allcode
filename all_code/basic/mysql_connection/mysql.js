// navgurukul@navgurukul-Latitude-E6420:~$ mysql -u root -p
// Enter password: 
// ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
// navgurukul@navgurukul-Latitude-E6420:~$ 
// lnavgurukul@navgurukul-Latitude-E6420:~$ sl

// Command 'sl' not found, but can be installed with:

// sudo apt install sl

// navgurukul@navgurukul-Latitude-E6420:~$ mysql -u root -p
// Enter password: 
// Welcome to the MySQL monitor.  Commands end with ; or \g.
// Your MySQL connection id is 9
// Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

// Copyright (c) 2000, 2021, Oracle and/or its affiliates.

// Oracle is a registered trademark of Oracle Corporation and/or its
// affiliates. Other names may be trademarks of their respective
// owners.

// Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

// mysql> show databases;
// +--------------------+
// | Database           |
// +--------------------+
// | information_schema |
// | learn              |
// | mysql              |
// | performance_schema |
// | sys                |
// +--------------------+
// 5 rows in set (0.02 sec)

// mysql> use learn;
// Reading table information for completion of table and column names
// You can turn off this feature to get a quicker startup with -A

// Database changed
// mysql> show tables;
// +-----------------+
// | Tables_in_learn |
// +-----------------+
// | student         |
// +-----------------+
// 1 row in set (0.00 sec)

// mysql> desc student;
// +---------+--------------+------+-----+---------+-------+
// | Field   | Type         | Null | Key | Default | Extra |
// +---------+--------------+------+-----+---------+-------+
// | id      | int          | NO   | PRI | NULL    |       |
// | name    | varchar(100) | NO   |     | NULL    |       |
// | city    | varchar(50)  | YES  |     | NULL    |       |
// | country | varchar(50)  | YES  |     | NULL    |       |
// +---------+--------------+------+-----+---------+-------+
// 4 rows in set (0.01 sec)

// mysql> select * from student;
// +-------+---------+--------+---------+
// | id    | name    | city   | country |
// +-------+---------+--------+---------+
// |    23 | ankit   | jonpur | ind     |
// |    24 | anand   | jonpur | ind     |
// |    43 | sahyog  | delhi  | ind     |
// |   234 | baljeet | delhi  | ind     |
// |   246 | subhash | mp     | india   |
// | 22346 | sahog   | mp     | india   |
// +-------+---------+--------+---------+
// 6 rows in set (0.00 sec)

// mysql> select country from student;
// +---------+
// | country |
// +---------+
// | ind     |
// | ind     |
// | ind     |
// | ind     |
// | india   |
// | india   |
// +---------+
// 6 rows in set (0.00 sec)

// mysql> select distinct(country)from student;
// +---------+
// | country |
// +---------+
// | ind     |
// | india   |
// +---------+
// 2 rows in set (0.00 sec)

// mysql> select distinct(city)from student;
// +--------+
// | city   |
// +--------+
// | jonpur |
// | delhi  |
// | mp     |
// +--------+
// 3 rows in set (0.00 sec)

// mysql> select distinct(name)from student;
// +---------+
// | name    |
// +---------+
// | ankit   |
// | anand   |
// | sahyog  |
// | baljeet |
// | subhash |
// | sahog   |
// +---------+
// 6 rows in set (0.00 sec)

// mysql> select * from student where country="india" and city="delhi";
// Empty set (0.00 sec)

// mysql> select * from student where country="india" and city="mp";
// +-------+---------+------+---------+
// | id    | name    | city | country |
// +-------+---------+------+---------+
// |   246 | subhash | mp   | india   |
// | 22346 | sahog   | mp   | india   |
// +-------+---------+------+---------+
// 2 rows in set (0.00 sec)

// mysql> select * from student where country="india" and id=246;
// +-----+---------+------+---------+
// | id  | name    | city | country |
// +-----+---------+------+---------+
// | 246 | subhash | mp   | india   |
// +-----+---------+------+---------+
// 1 row in set (0.00 sec)

// mysql> select * from student where country="india" and id=246 and name='subhash';
// +-----+---------+------+---------+
// | id  | name    | city | country |
// +-----+---------+------+---------+
// | 246 | subhash | mp   | india   |
// +-----+---------+------+---------+
// 1 row in set (0.00 sec)

// mysql> select * from student where country="india" or  id=246;
// +-------+---------+------+---------+
// | id    | name    | city | country |
// +-------+---------+------+---------+
// |   246 | subhash | mp   | india   |
// | 22346 | sahog   | mp   | india   |
// +-------+---------+------+---------+
// 2 rows in set (0.00 sec)

// mysql> select * from student where country="india" or city='delhi;
//     '> select * from student where country="india" or city='delhi';
//     '> select * from student where country="india" and id=246 and name='subhash';
//     '> 
//     '> 
//     '> exit
//     '> 

// [1]+  Stopped                 mysql -u root -p
// navgurukul@navgurukul-Latitude-E6420:~$ 
// navgurukul@navgurukul-Latitude-E6420:~$ mysql -u root -p
// Enter password: 
// Welcome to the MySQL monitor.  Commands end with ; or \g.
// Your MySQL connection id is 10
// Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

// Copyright (c) 2000, 2021, Oracle and/or its affiliates.

// Oracle is a registered trademark of Oracle Corporation and/or its
// affiliates. Other names may be trademarks of their respective
// owners.

// Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

// mysql> select * from student;
// ERROR 1046 (3D000): No database selected
// mysql> desc student;
// ERROR 1046 (3D000): No database selected
// mysql> show databases;
// +--------------------+
// | Database           |
// +--------------------+
// | information_schema |
// | learn              |
// | mysql              |
// | performance_schema |
// | sys                |
// +--------------------+
// 5 rows in set (0.01 sec)

// mysql> use learn'
// ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''' at line 1
// mysql> use learn;
// Reading table information for completion of table and column names
// You can turn off this feature to get a quicker startup with -A

// Database changed
// mysql> use learn;
// Database changed
// mysql> show tables;
// +-----------------+
// | Tables_in_learn |
// +-----------------+
// | student         |
// +-----------------+
// 1 row in set (0.01 sec)

// mysql> select * from student;
// +-------+---------+--------+---------+
// | id    | name    | city   | country |
// +-------+---------+--------+---------+
// |    23 | ankit   | jonpur | ind     |
// |    24 | anand   | jonpur | ind     |
// |    43 | sahyog  | delhi  | ind     |
// |   234 | baljeet | delhi  | ind     |
// |   246 | subhash | mp     | india   |
// | 22346 | sahog   | mp     | india   |
// +-------+---------+--------+---------+
// 6 rows in set (0.01 sec)

// mysql> select name from student;
// +---------+
// | name    |
// +---------+
// | ankit   |
// | anand   |
// | sahyog  |
// | baljeet |
// | subhash |
// | sahog   |
// +---------+
// 6 rows in set (0.00 sec)

// mysql> select * from student where country='india' or city='delhi';
// +-------+---------+-------+---------+
// | id    | name    | city  | country |
// +-------+---------+-------+---------+
// |    43 | sahyog  | delhi | ind     |
// |   234 | baljeet | delhi | ind     |
// |   246 | subhash | mp    | india   |
// | 22346 | sahog   | mp    | india   |
// +-------+---------+-------+---------+
// 4 rows in set (0.00 sec)

// mysql> select * from student where id >=24 and id <=246;
// +-----+---------+--------+---------+
// | id  | name    | city   | country |
// +-----+---------+--------+---------+
// |  24 | anand   | jonpur | ind     |
// |  43 | sahyog  | delhi  | ind     |
// | 234 | baljeet | delhi  | ind     |
// | 246 | subhash | mp     | india   |
// +-----+---------+--------+---------+
// 4 rows in set (0.00 sec)

// mysql> select * from student where id >=43 and id <=246;
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// |  43 | sahyog  | delhi | ind     |
// | 234 | baljeet | delhi | ind     |
// | 246 | subhash | mp    | india   |
// +-----+---------+-------+---------+
// 3 rows in set (0.00 sec)

// mysql> select * from student id between 43 and 346;
// ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'between 43 and 346' at line 1
// mysql> select * from student id between 43 and 246;
// ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'between 43 and 246' at line 1
// mysql> select * from student where id between 43 and 246;
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// |  43 | sahyog  | delhi | ind     |
// | 234 | baljeet | delhi | ind     |
// | 246 | subhash | mp    | india   |
// +-----+---------+-------+---------+
// 3 rows in set (0.00 sec)

// mysql> select * from student where id between 43 and 1223;
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// |  43 | sahyog  | delhi | ind     |
// | 234 | baljeet | delhi | ind     |
// | 246 | subhash | mp    | india   |
// +-----+---------+-------+---------+
// 3 rows in set (0.01 sec)

// mysql> select * from student where id=24 or id=234 or id=246;
// +-----+---------+--------+---------+
// | id  | name    | city   | country |
// +-----+---------+--------+---------+
// |  24 | anand   | jonpur | ind     |
// | 234 | baljeet | delhi  | ind     |
// | 246 | subhash | mp     | india   |
// +-----+---------+--------+---------+
// 3 rows in set (0.00 sec)

// mysql> select * from student where id in(24,234,246);
// +-----+---------+--------+---------+
// | id  | name    | city   | country |
// +-----+---------+--------+---------+
// |  24 | anand   | jonpur | ind     |
// | 234 | baljeet | delhi  | ind     |
// | 246 | subhash | mp     | india   |
// +-----+---------+--------+---------+
// 3 rows in set (0.00 sec)

// mysql>  select * from student;
// +-------+---------+--------+---------+
// | id    | name    | city   | country |
// +-------+---------+--------+---------+
// |    23 | ankit   | jonpur | ind     |
// |    24 | anand   | jonpur | ind     |
// |    43 | sahyog  | delhi  | ind     |
// |   234 | baljeet | delhi  | ind     |
// |   246 | subhash | mp     | india   |
// | 22346 | sahog   | mp     | india   |
// +-------+---------+--------+---------+
// 6 rows in set (0.00 sec)

// mysql> select * from student limit 4;
// +-----+---------+--------+---------+
// | id  | name    | city   | country |
// +-----+---------+--------+---------+
// |  23 | ankit   | jonpur | ind     |
// |  24 | anand   | jonpur | ind     |
// |  43 | sahyog  | delhi  | ind     |
// | 234 | baljeet | delhi  | ind     |
// +-----+---------+--------+---------+
// 4 rows in set (0.00 sec)

// mysql> select * from student limit 2 offset 2;
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// |  43 | sahyog  | delhi | ind     |
// | 234 | baljeet | delhi | ind     |
// +-----+---------+-------+---------+
// 2 rows in set (0.00 sec)

// mysql> select * from student limit 2 offset 3;
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// | 234 | baljeet | delhi | ind     |
// | 246 | subhash | mp    | india   |
// +-----+---------+-------+---------+
// 2 rows in set (0.00 sec)

// mysql> select * from student limit 3offset 2;
// ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '2' at line 1
// mysql> select * from student limit 3 offset 2;
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// |  43 | sahyog  | delhi | ind     |
// | 234 | baljeet | delhi | ind     |
// | 246 | subhash | mp    | india   |
// +-----+---------+-------+---------+
// 3 rows in set (0.00 sec)

// mysql> select * from student limit 3 offset 1;
// +-----+---------+--------+---------+
// | id  | name    | city   | country |
// +-----+---------+--------+---------+
// |  24 | anand   | jonpur | ind     |
// |  43 | sahyog  | delhi  | ind     |
// | 234 | baljeet | delhi  | ind     |
// +-----+---------+--------+---------+
// 3 rows in set (0.00 sec)

// mysql> select * from student limit 3 offset 2;
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// |  43 | sahyog  | delhi | ind     |
// | 234 | baljeet | delhi | ind     |
// | 246 | subhash | mp    | india   |
// +-----+---------+-------+---------+
// 3 rows in set (0.00 sec)

// mysql> select * from student;
// +-------+---------+--------+---------+
// | id    | name    | city   | country |
// +-------+---------+--------+---------+
// |    23 | ankit   | jonpur | ind     |
// |    24 | anand   | jonpur | ind     |
// |    43 | sahyog  | delhi  | ind     |
// |   234 | baljeet | delhi  | ind     |
// |   246 | subhash | mp     | india   |
// | 22346 | sahog   | mp     | india   |
// +-------+---------+--------+---------+
// 6 rows in set (0.00 sec)

// mysql> select * from student order by id;
// +-------+---------+--------+---------+
// | id    | name    | city   | country |
// +-------+---------+--------+---------+
// |    23 | ankit   | jonpur | ind     |
// |    24 | anand   | jonpur | ind     |
// |    43 | sahyog  | delhi  | ind     |
// |   234 | baljeet | delhi  | ind     |
// |   246 | subhash | mp     | india   |
// | 22346 | sahog   | mp     | india   |
// +-------+---------+--------+---------+
// 6 rows in set (0.01 sec)

// mysql> select * from student order by id desc;
// +-------+---------+--------+---------+
// | id    | name    | city   | country |
// +-------+---------+--------+---------+
// | 22346 | sahog   | mp     | india   |
// |   246 | subhash | mp     | india   |
// |   234 | baljeet | delhi  | ind     |
// |    43 | sahyog  | delhi  | ind     |
// |    24 | anand   | jonpur | ind     |
// |    23 | ankit   | jonpur | ind     |
// +-------+---------+--------+---------+
// 6 rows in set (0.00 sec)

// mysql> select * from student order by name;
// +-------+---------+--------+---------+
// | id    | name    | city   | country |
// +-------+---------+--------+---------+
// |    24 | anand   | jonpur | ind     |
// |    23 | ankit   | jonpur | ind     |
// |   234 | baljeet | delhi  | ind     |
// | 22346 | sahog   | mp     | india   |
// |    43 | sahyog  | delhi  | ind     |
// |   246 | subhash | mp     | india   |
// +-------+---------+--------+---------+
// 6 rows in set (0.00 sec)

// mysql> select * from student order by name desc;
// +-------+---------+--------+---------+
// | id    | name    | city   | country |
// +-------+---------+--------+---------+
// |   246 | subhash | mp     | india   |
// |    43 | sahyog  | delhi  | ind     |
// | 22346 | sahog   | mp     | india   |
// |   234 | baljeet | delhi  | ind     |
// |    23 | ankit   | jonpur | ind     |
// |    24 | anand   | jonpur | ind     |
// +-------+---------+--------+---------+
// 6 rows in set (0.00 sec)

// mysql> select * from student order by id desc limit 2;
// +-------+---------+------+---------+
// | id    | name    | city | country |
// +-------+---------+------+---------+
// | 22346 | sahog   | mp   | india   |
// |   246 | subhash | mp   | india   |
// +-------+---------+------+---------+
// 2 rows in set (0.00 sec)

// mysql> update student set name='sahyog verma' where id 22346;
// ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '22346' at line 1
// mysql> update student set name='sahyogverma' where id 22346;
// ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '22346' at line 1
// mysql> update student set name='sahyogverma' where id=22346;
// Query OK, 1 row affected (0.16 sec)
// Rows matched: 1  Changed: 1  Warnings: 0

// mysql> select * from student;
// +-------+-------------+--------+---------+
// | id    | name        | city   | country |
// +-------+-------------+--------+---------+
// |    23 | ankit       | jonpur | ind     |
// |    24 | anand       | jonpur | ind     |
// |    43 | sahyog      | delhi  | ind     |
// |   234 | baljeet     | delhi  | ind     |
// |   246 | subhash     | mp     | india   |
// | 22346 | sahyogverma | mp     | india   |
// +-------+-------------+--------+---------+
// 6 rows in set (0.00 sec)

// mysql> select name from student;
// +-------------+
// | name        |
// +-------------+
// | ankit       |
// | anand       |
// | sahyog      |
// | baljeet     |
// | subhash     |
// | sahyogverma |
// +-------------+
// 6 rows in set (0.00 sec)

// mysql> 
// mysql> select * from student where name like 'a%';
// +----+-------+--------+---------+
// | id | name  | city   | country |
// +----+-------+--------+---------+
// | 23 | ankit | jonpur | ind     |
// | 24 | anand | jonpur | ind     |
// +----+-------+--------+---------+
// 2 rows in set (0.00 sec)

// mysql> select * from student where name like 's%';
// +-------+-------------+-------+---------+
// | id    | name        | city  | country |
// +-------+-------------+-------+---------+
// |    43 | sahyog      | delhi | ind     |
// |   246 | subhash     | mp    | india   |
// | 22346 | sahyogverma | mp    | india   |
// +-------+-------------+-------+---------+
// 3 rows in set (0.00 sec)

// mysql> select * from student where city like 'd%';
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// |  43 | sahyog  | delhi | ind     |
// | 234 | baljeet | delhi | ind     |
// +-----+---------+-------+---------+
// 2 rows in set (0.01 sec)

// mysql> select * from student where city like 'dil%';
// Empty set (0.01 sec)

// mysql> select * from student where city like 'del%';
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// |  43 | sahyog  | delhi | ind     |
// | 234 | baljeet | delhi | ind     |
// +-----+---------+-------+---------+
// 2 rows in set (0.00 sec)

// mysql> select * from student where city like '__l%';
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// |  43 | sahyog  | delhi | ind     |
// | 234 | baljeet | delhi | ind     |
// +-----+---------+-------+---------+
// 2 rows in set (0.00 sec)

// mysql> select * from student where city like '_e%';
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// |  43 | sahyog  | delhi | ind     |
// | 234 | baljeet | delhi | ind     |
// +-----+---------+-------+---------+
// 2 rows in set (0.00 sec)

// mysql> select * from student where naame like '_u%';
// ERROR 1054 (42S22): Unknown column 'naame' in 'where clause'
// mysql> select * from student where name like '_u%';
// +-----+---------+------+---------+
// | id  | name    | city | country |
// +-----+---------+------+---------+
// | 246 | subhash | mp   | india   |
// +-----+---------+------+---------+
// 1 row in set (0.00 sec)

// mysql> select * from student where name like '%h_';
// Empty set (0.00 sec)

// mysql> select * from student where name like '%_h';
// +-----+---------+------+---------+
// | id  | name    | city | country |
// +-----+---------+------+---------+
// | 246 | subhash | mp   | india   |
// +-----+---------+------+---------+
// 1 row in set (0.00 sec)

// mysql> select * from student where city like '%h_';
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// |  43 | sahyog  | delhi | ind     |
// | 234 | baljeet | delhi | ind     |
// +-----+---------+-------+---------+
// 2 rows in set (0.00 sec)

// mysql> select * from student where city like '%i';
// +-----+---------+-------+---------+
// | id  | name    | city  | country |
// +-----+---------+-------+---------+
// |  43 | sahyog  | delhi | ind     |
// | 234 | baljeet | delhi | ind     |
// +-----+---------+-------+---------+
// 2 rows in set (0.01 sec)

// mysql> select * from student;
// +-------+-------------+--------+---------+
// | id    | name        | city   | country |
// +-------+-------------+--------+---------+
// |    23 | ankit       | jonpur | ind     |
// |    24 | anand       | jonpur | ind     |
// |    43 | sahyog      | delhi  | ind     |
// |   234 | baljeet     | delhi  | ind     |
// |   246 | subhash     | mp     | india   |
// | 22346 | sahyogverma | mp     | india   |
// +-------+-------------+--------+---------+
// 6 rows in set (0.00 sec)

// mysql> select sum(id) from student;
// +---------+
// | sum(id) |
// +---------+
// |   22916 |
// +---------+
// 1 row in set (0.03 sec)

// mysql> select sum(id) as "total salary" from student;
// +--------------+
// | total salary |
// +--------------+
// |        22916 |
// +--------------+
// 1 row in set (0.00 sec)

// mysql> select AVG(id) from student;
// +-----------+
// | AVG(id)   |
// +-----------+
// | 3819.3333 |
// +-----------+
// 1 row in set (0.00 sec)

// mysql> select count(id) from student;
// +-----------+
// | count(id) |
// +-----------+
// |         6 |
// +-----------+
// 1 row in set (0.00 sec)

// mysql> select count(name) from student;
// +-------------+
// | count(name) |
// +-------------+
// |           6 |
// +-------------+
// 1 row in set (0.01 sec)

// mysql> select min(id) from student;
// +---------+
// | min(id) |
// +---------+
// |      23 |
// +---------+
// 1 row in set (0.00 sec)

// mysql> select name from student where id=(select min(id)from student);
// +-------+
// | name  |
// +-------+
// | ankit |
// +-------+
// 1 row in set (0.12 sec)

// mysql> select name from student where id=(select max(id)from student);
// +-------------+
// | name        |
// +-------------+
// | sahyogverma |
// +-------------+
// 1 row in set (0.00 sec)

// mysql> select name from student where id=(select MAX(id)from student);
// +-------------+
// | name        |
// +-------------+
// | sahyogverma |
// +-------------+
// 1 row in set (0.01 sec)

// mysql> show tables;
// +-----------------+
// | Tables_in_learn |
// +-----------------+
// | student         |
// +-----------------+
// 1 row in set (0.00 sec)

// mysql> select * from student;
// +-------+-------------+--------+---------+
// | id    | name        | city   | country |
// +-------+-------------+--------+---------+
// |    23 | ankit       | jonpur | ind     |
// |    24 | anand       | jonpur | ind     |
// |    43 | sahyog      | delhi  | ind     |
// |   234 | baljeet     | delhi  | ind     |
// |   246 | subhash     | mp     | india   |
// | 22346 | sahyogverma | mp     | india   |
// +-------+-------------+--------+---------+
// 6 rows in set (0.00 sec)

// mysql> create table laptops(lid int primary key, lmodel varchar(200), studentid int, foreign key(studentid) references student (id));
// Query OK, 0 rows affected (1.46 sec)

// mysql> show tables;
// +-----------------+
// | Tables_in_learn |
// +-----------------+
// | laptops         |
// | student         |
// +-----------------+
// 2 rows in set (0.01 sec)

// mysql> desc student;
// +---------+--------------+------+-----+---------+-------+
// | Field   | Type         | Null | Key | Default | Extra |
// +---------+--------------+------+-----+---------+-------+
// | id      | int          | NO   | PRI | NULL    |       |
// | name    | varchar(100) | NO   |     | NULL    |       |
// | city    | varchar(50)  | YES  |     | NULL    |       |
// | country | varchar(50)  | YES  |     | NULL    |       |
// +---------+--------------+------+-----+---------+-------+
// 4 rows in set (0.01 sec)

// mysql> desc laptops;
// +-----------+--------------+------+-----+---------+-------+
// | Field     | Type         | Null | Key | Default | Extra |
// +-----------+--------------+------+-----+---------+-------+
// | lid       | int          | NO   | PRI | NULL    |       |
// | lmodel    | varchar(200) | YES  |     | NULL    |       |
// | studentid | int          | YES  | MUL | NULL    |       |
// +-----------+--------------+------+-----+---------+-------+
// 3 rows in set (0.01 sec)

// mysql> insert into laptops values(143, 'hp', 23);
// Query OK, 1 row affected (0.07 sec)

// mysql> select * from laptops;
// +-----+--------+-----------+
// | lid | lmodel | studentid |
// +-----+--------+-----------+
// | 143 | hp     |        23 |
// +-----+--------+-----------+
// 1 row in set (0.00 sec)

// mysql> insert into laptops values(143, 'dell', 24);
// ERROR 1062 (23000): Duplicate entry '143' for key 'laptops.PRIMARY'
// mysql> select * from laptops;
// +-----+--------+-----------+
// | lid | lmodel | studentid |
// +-----+--------+-----------+
// | 143 | hp     |        23 |
// +-----+--------+-----------+
// 1 row in set (0.00 sec)

// mysql> insert into laptops values(1431, 'dell', 24);
// Query OK, 1 row affected (0.10 sec)

// mysql> select * from laptops;
// +------+--------+-----------+
// | lid  | lmodel | studentid |
// +------+--------+-----------+
// |  143 | hp     |        23 |
// | 1431 | dell   |        24 |
// +------+--------+-----------+
// 2 rows in set (0.00 sec)

// mysql> select * from student;
// +-------+-------------+--------+---------+
// | id    | name        | city   | country |
// +-------+-------------+--------+---------+
// |    23 | ankit       | jonpur | ind     |
// |    24 | anand       | jonpur | ind     |
// |    43 | sahyog      | delhi  | ind     |
// |   234 | baljeet     | delhi  | ind     |
// |   246 | subhash     | mp     | india   |
// | 22346 | sahyogverma | mp     | india   |
// +-------+-------------+--------+---------+
// 6 rows in set (0.00 sec)

// mysql> select student.name,student.city,laptops.lmodel from student,laptops where student.id=laptops.studentid;
// +-------+--------+--------+
// | name  | city   | lmodel |
// +-------+--------+--------+
// | ankit | jonpur | hp     |
// | anand | jonpur | dell   |
// +-------+--------+--------+
// 2 rows in set (0.00 sec)

// mysql> select student.name,student.city,laptops.lmodel from student,laptops where student.id=laptops.studentid and student.name='ankit';
// +-------+--------+--------+
// | name  | city   | lmodel |
// +-------+--------+--------+
// | ankit | jonpur | hp     |
// +-------+--------+--------+
// 1 row in set (0.00 sec)

// mysql> select student.name, laptops.lmodel from student inner join laptops on student.id=laptops.studentid;
// +-------+--------+
// | name  | lmodel |
// +-------+--------+
// | ankit | hp     |
// | anand | dell   |
// +-------+--------+
// 2 rows in set (0.00 sec)
