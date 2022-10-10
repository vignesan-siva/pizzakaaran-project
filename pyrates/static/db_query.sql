create schema pizza;

use pizza;


#orders
create table pizza.orders(id int not null auto_increment primary key ,product_name varchar(50),username varchar(50),
email varchar(50) ,quantity numeric, mobilenumber varchar(50),orderdate varchar(50),
address varchar(100),price int,totalcost int);

insert into pizza.orders(product_name,username,email,quantity,mobilenumber,orderdate,address,price,totalcost)values('pizza','vignesan','vignesh@gmail.com',2,'77272777','2022-05-23','tvm',30,60);

select*from  pizza.orders;

--  drop table pizza.orders;



#survey
create table pizza.survey(id int not null auto_increment primary key ,username varchar(50),city varchar(50),
item varchar(50) ,favday varchar(20), family int,favmonth varchar(20));

select * from pizza.survey;

-- drop table pizza.survey;



#enquiry
create table pizza.enquiry(id int not null auto_increment primary key ,username varchar(50),mobilenumber varchar(20),
email varchar(50) ,typeofproblem varchar(100), message varchar(20));

select* from pizza.enquiry;

-- drop table pizza.enquiry;



#Addpizzaitem
create table pizza.pizzaitems(id int not null auto_increment primary key ,product_code varchar(50),product_name varchar(50),
product_price int(10),product_pic varchar(100));

insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_01','Mushroom corn Pizza',349,'static\\images\\tandoori-mushroom-&-sweet-corn-pan-pizza.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_02','Pepper Onion Pizza',239,'static\\images\\pizza2.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_03','American Pizza',299,'static\\images\\pizza3.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_04','Babycorn Pizza',249,'static\\images\\pizza5.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_05','Corn-n-Chessy Pizza',239,'static\\images\\pizza6.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_06','Panner Pizza',249,'static\\images\\pizza7.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_07','Tandoori Panner Pizza',299,'static\\images\\pizza8.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_08','Spiced Panner Pizza',279,'static\\images\\pizza9.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_09','Momo-n-Chesse Pizza',349,'static\\images\\pizza10.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_10','Momo-n-Corn Pizza',299,'static\\images\\pizza11.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_11','Veggie Pizza',199,'static\\images\\pizza12.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_12','Veggie Panner Pizza',249,'static\\images\\pizza13.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_13','Chicken Supreme',379,'static\\images\\chicken-supreme.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_14','Chicken Tikka Supreme',399,'static\\images\\chicken-tikka-supreme.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_15','chicken-n-corn-delight',349,'static\\images\\chicken-n-corn-delight.jpg');
insert into pizza.pizzaitems(product_code,product_name,product_price,product_pic)values('pizza_16','Chicken Pepper Pizza',599,'static\\images\\pizza1.jpg');

select * from pizza.pizzaitems;
drop table pizza.pizzaitems;



#Addddrinksitems
create table pizza.drinkitems(id int not null auto_increment primary key ,product_code varchar(50),product_name varchar(50),
product_price int(10),product_pic varchar(100));

insert into pizza.drinkitems(product_code,product_name,product_price,product_pic)values('drink_01','Coca cola 200ml',39,'static\\images\\coca-cola.jpg');
insert into pizza.drinkitems(product_code,product_name,product_price,product_pic)values('drink_02','Pepsi 200ml',39,'static\\images\\pepsi.jpg');
insert into pizza.drinkitems(product_code,product_name,product_price,product_pic)values('drink_03','Monster 350ml',79,'static\\images\\Monster.jpg');
insert into pizza.drinkitems(product_code,product_name,product_price,product_pic)values('drink_04','Redbull 200ml',119,'static\\images\\redbull.jpg');
insert into pizza.drinkitems(product_code,product_name,product_price,product_pic)values('drink_05','7up 200ml',29,'static\\images\\7UP.jpg');
insert into pizza.drinkitems(product_code,product_name,product_price,product_pic)values('drink_06','Sprite 200ml',29,'static\\images\\sprite.jpg');
insert into pizza.drinkitems(product_code,product_name,product_price,product_pic)values('drink_07','Mountain dew 200ml',49,'static\\images\\Mountain Dew.jpg');
insert into pizza.drinkitems(product_code,product_name,product_price,product_pic)values('drink_08','Mirinda 200ml',39,'static\\images\\mirinda.jpg');
insert into pizza.drinkitems(product_code,product_name,product_price,product_pic)values('drink_09','Fanta 200ml',39,'static\\images\\fanta.jpg');

select*from pizza.drinkitems;

-- drop table pizza.drinkitems;



#Addburgeritems
create table pizza.burgeritems(id int not null auto_increment primary key ,product_code varchar(50),product_name varchar(50),
product_price int(10), product_pic varchar(100));

insert into pizza.burgeritems(product_code,product_name,product_price,product_pic)values('burger_01','Chicken Spicy Burger',299,'static\\images\\burger-1.jpg');
insert into pizza.burgeritems(product_code,product_name,product_price,product_pic)values('burger_02','Grilled Chicken Burger',399,'static\\images\\burger-2.jpg');
insert into pizza.burgeritems(product_code,product_name,product_price,product_pic)values('burger_03','Big Smoky Grill Chicken Burger',299,'static\\images\\burger-4.jpg');
insert into pizza.burgeritems(product_code,product_name,product_price,product_pic)values('burger_04','Cripsy Veg Burger',199,'static\\images\\burger5.jpg');
insert into pizza.burgeritems(product_code,product_name,product_price,product_pic)values('burger_05','Crispy Veg Wrap Burger',199,'static\\images\\burger-6.jpg');
insert into pizza.burgeritems(product_code,product_name,product_price,product_pic)values('burger_06','Chicken Double patty Burger',299,'static\\images\\burger7.jpg');
insert into pizza.burgeritems(product_code,product_name,product_price,product_pic)values('burger_07','Crispy Chesse Veg Burger',249,'static\\images\\burger8.jpg');
insert into pizza.burgeritems(product_code,product_name,product_price,product_pic)values('burger_08','Lite Whopper Veg burger',249,'static\\images\\burger9.jpg');
insert into pizza.burgeritems(product_code,product_name,product_price,product_pic)values('burger_09','Lite Whopper Chicken Burger',299,'static\\images\\burger10.jpg');

select*from pizza.burgeritems;

-- drop table pizza.burgeritems;



#Addpastaitems
create table pizza.pastaitems(id int not null auto_increment primary key ,product_code varchar(50),product_name varchar(50),
product_price int(10),product_pic varchar(100));

insert into pizza.pastaitems(product_code,product_name,product_price,product_pic)values('pasta_01','Red Sause pasta',299,'static\\images\\pasta1.jpg');
insert into pizza.pastaitems(product_code,product_name,product_price,product_pic)values('pasta_02','Springed prawn pasta',399,'static\\images\\pasta2.jpg');
insert into pizza.pastaitems(product_code,product_name,product_price,product_pic)values('pasta_03','Spinach-n-Ricotta pasta',299,'static\\images\\pasta3.jpg');
insert into pizza.pastaitems(product_code,product_name,product_price,product_pic)values('pasta_04','Broccoli Sauce pasta',199,'static\\images\\pasta5.jpg');
insert into pizza.pastaitems(product_code,product_name,product_price,product_pic)values('pasta_05','Vegetable pasta',199,'static\\images\\pasta6.jpg');
insert into pizza.pastaitems(product_code,product_name,product_price,product_pic)values('pasta_06','Veggie Scramble pasta',249,'static\\images\\pasta7.jpg');
insert into pizza.pastaitems(product_code,product_name,product_price,product_pic)values('pasta_07','Chilli Creamy pasta',229,'static\\images\\pasta8.jpg');
insert into pizza.pastaitems(product_code,product_name,product_price,product_pic)values('pasta_08','Tomato pasta',249,'static\\images\\pasta9.jpg');
insert into pizza.pastaitems(product_code,product_name,product_price,product_pic)values('pasta_09','Greeny Grilled pasta',299,'static\\images\\pasta10.jpg');

select*from pizza.pastaitems;

-- drop table pizza.pastaitems;



#Admin
create table pizza.admin(username varchar(50),password varchar(50));

insert into pizza.admin(username,password) values('admin','admin');

select * from pizza.admin;

-- drop table pizza.admin;



#Registers
create table pizza.registers(firstname  varchar(50),lastname varchar(50), email varchar(50) ,password varchar(50),mobilenumber varchar(50), address varchar(100));

select * from pizza.registers;

drop table pizza.registers;



#addcart 
create table pizza.cart(produt_name varchar(50),quantity varchar(50), price int,totalcost int);

select * from pizza.cart;

#happy customers

create table pizza.customers(branch int,awards int, customer int,staff int);

insert into pizza.customers(branch,awards,customer,staff)values(100,500,500000,10000);
select * from pizza.customers;



