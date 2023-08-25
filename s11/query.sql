insert into user (username,email,password,picture) values 
('mohammad','m@gmail.com','123','m.profile.png');

insert into book (name,author,picture) values
('atomic habbits','brian tracy','pic1.png'),
('nation of love','elif ','pic2.png');

select * from book where user_id is null;

update book set user_id=1 where name='atomic habbits';