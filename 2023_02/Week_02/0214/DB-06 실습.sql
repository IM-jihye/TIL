-- 문제 1
-- 필드 정보를 참고해서 테이블 users 를 생성하시오.
CREATE table users(
userId int auto_increment,
first_name varchar(20) not null,
last_name varchar(20) not null,
birthday date not null,
city varchar(100),	
country	varchar(100),
email varchar(100),
created_at DATETIME NOT NULL DEFAULT NOW(),
primary key(userId));
SHOW COLUMNS from users;

-- 문제 2
-- 레코드 정보를 보고 테이블 users 에 데이터를 입력하시오.
INSERT INTO users(first_name,last_name,birthday,city,country,email)
VALUES('Beemo','Jeong',1000-01-01,'','','beemo@hphk.kr'),
	  ('Jieun','Lee','1993-05-16','Seoul','Korea',''),
	  ('Dami','Kim','1995-04-09','Seoul','Korea',''),
	  ('Kwangsoo','Lee','1985-07-14','Seoul','Korea','');

-- 문제 3
-- 테이블 users 에 임의로 데이터 5개를 입력하시오.
INSERT INTO users(first_name,last_name,birthday,city,country,email)
VALUES('ji','kim','1985-05-09','Seoul','Korea','minji@naver.com'),
	  ('hyeji','kang','1955-05-09','Seoul','Korea','mm@naver.com'),
      ('kwangmin','yoon','1785-03-09','Seoul','Korea',''),
	  ('min','park','1455-07-10','Seoul','Korea',''),
	  ('bomi','bang','1998-09-15','Seoul','Korea','hjr@naver.com');

-- 문제 4
-- 2번 레코드의 first_name, last_name, birthday 필드 값을 자신의 이름, 성, 생년월일로 변경하시오.
UPDATE users 
set first_name = 'jihye', last_name = 'im', birthday = '1997-04-29'
where userId= 2;

-- 문제 5
-- 테이블 users 에서 country 필드가 NULL 인 모드 레코드의 country 필드 값을 Korea 로 변경하시오.
update user 
set country = 'Korea'
where country is NULL;

-- 문제 6
-- 테이블 users 에서 first_name 필드가 Beemo 인 레코드를 삭제하시오.
DELETE from users
where first_name = 'Beemo';

-- 문제 7
-- 테이블 users 에서 first_name 필드가 Kwangsoo, last_name 필드가 Lee 인 레코드를 삭제하시오.
DELETE from users
where first_name ='Kwangsoo' and last_name = 'Lee';

-- 문제 8
-- 테이블 users 에서 가장 나중에 생성한 레코드 1개를 삭제하시오.
DELETE from users
ORDER BY userId desc
limit 1;







