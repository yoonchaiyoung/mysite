desc user;
-- 잘 만들어졌는 지 확인

-- 조회
select * from user;

-- 회원가입
insert 
into user 
values(null, '둘리', 'dooly@gmail.com', password('1234'), 'male', now());

-- 로그인
select no, name
from user
where email='dooly@gmail.com'
and password=password('1234');

-- 회원정보수정

