-- 문제1
-- 테이블 customers 에서 country 필드의 중복을 제거한 데이터를 조회하시오.
-- 단, country 기준 오름차순으로 정렬하세요.

select DISTINCT country
FROM customers
order by country;

-- 문제2
-- 테이블 customers 에서 state 필드의 중복을 제거한 데이터를 조회하시오.
-- 단, state 기준 내림차순으로 정렬하세요.

select DISTINCT state
from  customers 
order by state desc;

-- 문제3
-- 테이블 customers 에서 country 가 USA 가 아닌 customerNumber , customerName , country 필드의 데이터를 조회하시오.
-- 단, customerNumber 기준 내림차순으로 정렬하세요.

select customerNumber , customerName , country
from customers
where country != 'usa'
order by customerNumber desc;

-- 문제4
-- 테이블 offices 에서 city 가 Paris 인 데이터를 조회하시오.
select *
from offices
where city = 'paris';

-- 문제5
-- 테이블 customers 에서 country 가 USA 고, state 가 CA 인 customerNumber , customerName , country , state 필드의 데이터를 조회하시오.
-- 단, customerName 기준 내림차순으로 정렬하세요.
select customerNumber , customerName , country , state
from customers
where  country = 'USA' and state = 'CA'
ORDER BY customerName desc;

-- 문제6 
-- 테이블 customers 에서 country 가 USA 고, state 가 CA 또는 NY 인 customerNumber , customerName , country , state 필드의 데이터를 조회하시오.
-- 단, customerNumber 기준 내림차순으로 정렬하세요.
select  customerNumber , customerName , country , state
from customers
where country = 'USA' and state in ('CA' ,'NY')
ORDER BY customerNumber desc;

-- 문제7
-- 테이블 customers 에서 state 가 CA 또는 NY 또는 CT 또는 PA 인 customerNumber , customerName , state 필드의 데이터를 조회하시오.
-- 단, customerNumber 기준 내림차순으로 정렬하세요.
select  customerNumber , customerName , state
from customers 
where state in ('CA', 'NY','CT', 'PA')
ORDER BY customerNumber desc;

-- 문제8 
-- 테이블 products 에서 quantityInStock 가 1000 미만인 productCode , productName , quantityInStock 필드의 데이터를 조회하시오.
-- 단, quantityInStock 기준 오름차순으로 정렬하세요.

select productCode, productName, quantityInStock
from  products 
where quantityInStock < 1000
order by quantityInStock;

-- 문제9
-- 테이블 products 에서 quantityInStock 가 2000 과 3000 사이인 productCode , productName , quantityInStock 필드의 데이터를 조회하시오.
-- 단, quantityInStock 기준 내림차순으로 정렬하세요.

select productCode , productName , quantityInStock
from products
where quantityInStock BETWEEN 2000 and 3000
order by quantityInStock desc;

-- 문제10
-- 테이블 customers 에서 phone 가 555 로 끝나는 customerNumber , customerName , phone 필드의 데이터를 조회하시오.
-- 단, customerName 기준 내림차순으로 정렬하세요.

select customerNumber , customerName , phone 
from customers 
where phone like '%555'
order by customerName  desc;

-- 문제11
-- 테이블 products 에서 quantityInStock 필드가 높은 5개의 productCode , quantityInStock 필드의 데이터를 조회하시오.
-- 단, quantityInStock 기준 내림차순으로 정렬하세요.

select productCode , quantityInStock
from products
order by quantityInStock desc
LIMIT 5;

-- 문제12
-- 테이블 employees 에서 jobTitle 필드를 그룹화하여 각 그룹에 대한 개수를 조회하시오.
-- 단, 인원 수 기준 내림차순, jobTitle 기준 내림차순으로 정렬하세요.

select jobTitle, count(jobTitle) as count_job
from employees
GROUP BY jobTitle
order by count(jobTitle) desc,jobTitle desc;

-- 문제13
-- 테이블 customers 에서 country 필드를 그룹화하여 각 그룹에 대한 개수를 조회하시오.
-- 단, 인원 수 기준 내림차순 country 기준 내림차순으로 정렬하세요.

select country, count(country) as count_country
from customers 
GROUP BY  country
ORDER BY count_country desc, country desc;

-- 문제14
-- 테이블 orderdetails 에서 orderNumber 필드를 그룹화하여 각 그룹에 대한 quantityOrdered * priceEach 의 합을 조회하시오.
-- 단, quantityOrdered * priceEach 의 합 기준 내림차순으로 정렬하세요.

select orderNumber,sum(quantityOrdered * priceEach) as total
from orderdetails
GROUP BY orderNumber
order by total desc;

-- 문제15 
-- 테이블 orders 에서 년도별(year)로 그룹화하여 orderNumber 필드의 개수를 조회하시오.

select year(orderDate) ,count(orderNumber) 
from orders
GROUP BY year(orderDate);

-- 문제 16
-- 테이블 products 에서 productLine 필드를 그룹화하여 각 그룹에 대한 quantityInStock 필드의 최댓값을 조회하시오.
-- 단, 최댓값이 9000 미만인 데이터만 조회하시오.

select productLine, max(quantityInStock) as max_stock
from  products
GROUP BY productLine
having max_stock < 9000;

-- 문제 17
-- 테이블 orderdetails 에서 ordernumber 필드를 그룹화하여 각 그룹에 대한 quantityOrdered 필드의 합과 priceeach * quantityOrdered 의 합을 조회하시오.
-- 단, quantityOrdered 합이 500 이상, priceeach * quantityOrdered 합이 50000 이상인 데이터만 조회하시오.

select orderNumber, sum(quantityOrdered) as itemsCount, sum(priceeach * quantityOrdered) as total
from orderdetails
GROUP BY orderNumber
having itemsCount >= 500 and total >= 50000;