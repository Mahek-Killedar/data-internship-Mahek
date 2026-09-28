create database demo;
use demo;
create table customers (
  customer_id int,
  name varchar(50),
  city varchar(50),
  phone varchar(15),
  email varchar(50)
);
insert into customers (customer_id, name, city, phone, email) values
(101, 'Rahul Sharma', 'Pune', '9876543210', 'rahul@example.com'),
(102, 'Priya Deshmukh', 'Mumbai', '9823456780', 'priya@example.com'),
(103, 'Amit Kumar', 'Pune', '9812345678', 'amit@example.com'),
(104, 'Sneha Patil', 'Nagpur', '9898989898', 'sneha@example.com'),
(105, 'Karan Mehta', 'Delhi', '9765432109', 'karan@example.com');

create table products (
  product_id int,
  product_name varchar(50),
  category varchar(30),
  price decimal(10,2),
  stock int
);
insert into products (product_id, product_name, category, price, stock) values
(201, 'Laptop', 'Electronics', 55000, 10),
(202, 'Mobile Phone', 'Electronics', 15000, 25),
(203, 'Office Chair', 'Furniture', 4500, 0),
(204, 'Desk Lamp', 'Furniture', 800, 40),
(205, 'Bluetooth Speaker', 'Electronics', 2500, 15);

create table orders (
  order_id int,
  customer_id int,
  product_id int,
  quantity int,
  order_amount decimal(10,2),
  order_date date
);
insert into orders (order_id, customer_id, product_id, quantity, order_amount, order_date) values
(301, 101, 201, 1, 55000, '2025-01-05'),
(302, 102, 202, 2, 30000, '2025-01-06'),
(303, 103, 205, 1, 2500, '2025-01-07'),
(304, 101, 204, 3, 2400, '2025-01-10'),
(305, 104, 202, 1, 15000, '2025-01-12'),
(306, 105, 201, 1, 55000, '2025-01-15'),
(307, 102, 205, 2, 5000, '2025-01-16'),
(308, 103, 202, 1, 15000, '2025-01-18'),
(309, 101, 202, 1, 15000, '2025-01-20'),
(310, 104, 204, 5, 4000, '2025-01-22');

# 1. Find all customers
select * from customers;

# 2. Find customers from Pune
select * from customers where city = 'Pune';

# 3. Find total number of customers
select count(*) as total_customers from customers;

# 4. Find a customer using their email
select * from customers where email = 'raj@example.com';

# 5. Find customers sorted by name (A to Z)
select * from customers order by name asc;

# 6. Find all products
select * from products;

# 7. Find products in the Electronics category
select * from products where category = 'Electronics';

# 8. Find products with price above ₹1,000
select * from products where price > 1000;

# 9. Find products that are out of stock
select * from products where stock = 0;

# 10. Find the top 5 most expensive products
select * from products order by  price desc limit 5;

# 11. Find total number of products in each category
select category, count(*) as total_products from products group by category;

 # 12. Find all orders
select * from orders;


# 13. Find orders above ₹5,000
select * from orders where order_amount > 5000;

# 14. Find orders placed by one particular customer
select * from orders where customer_id = 101;

# 15. Find orders placed on a particular date
select * from orders where order_date = '2025-01-15';

# 16. Find total number of orders
select count(*) as total_orders from orders;

# 17. Find the most recent orders first
select * from orders order by  order_date desc;




# 18. Calculate total sales
select sum(order_amount) as total_sales from orders;

# 19. Calculate average order value
select avg(order_amount) as average_order_value from orders;


# 20. Find the highest order amount
select max(order_amount) as highest_order from orders;


#Day 8 
#A) Problem 1 – Top 3 Customers
# 1.	Top 3 customers by total spending, using RANK()
WITH customer_totals AS (
  SELECT c.customer_id, c.name, SUM(o.order_amount) AS total_spent
  FROM customers c
  JOIN orders o ON c.customer_id = o.customer_id
  GROUP BY c.customer_id, c.name
),
ranked AS (
  SELECT name, total_spent,
    RANK() OVER (ORDER BY total_spent DESC) AS customer_rank
  FROM customer_totals
)
SELECT name, total_spent, customer_rank
FROM ranked
WHERE customer_rank <= 3;

B) Problem 2 – Top 3 Products per Category

1.	Top 3 most expensive products in each category, using ROW_NUMBER()
WITH ranked_products AS (
  SELECT product_name, category, price,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) AS rn
  FROM products
)
SELECT product_name, category, price
FROM ranked_products
WHERE rn <= 3;

C) Problem 3 – Customer Ranking
1.	Rank all customers by their total spending, using RANK()
SELECT c.name, SUM(o.order_amount) AS total_spent,
  RANK() OVER (ORDER BY SUM(o.order_amount) DESC) AS spend_rank
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name;

D) Problem 4 – Monthly Revenue
1.	Find total revenue earned in each month
SELECT DATE_FORMAT(order_date, '%Y-%m') AS order_month,
  SUM(order_amount) AS monthly_revenue
FROM orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY order_month;

#E) Problem 5 – Previous Month's Revenue
1.	Show each month's revenue next to the previous month's revenue, using LAG()
WITH monthly_revenue AS (
  SELECT DATE_FORMAT(order_date, '%Y-%m') AS order_month,
    SUM(order_amount) AS revenue
  FROM orders
  GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT order_month, revenue,
  LAG(revenue) OVER (ORDER BY order_month) AS previous_month_revenue
FROM monthly_revenue;

F) Problem 6 – Month-over-Month Growth
1.	Calculate month-over-month revenue growth percentage
WITH monthly_revenue AS (
  SELECT DATE_FORMAT(order_date, '%Y-%m') AS order_month,
    SUM(order_amount) AS revenue
  FROM orders
  GROUP BY DATE_FORMAT(order_date, '%Y-%m')
),
with_previous AS (
  SELECT order_month, revenue,
    LAG(revenue) OVER (ORDER BY order_month) AS previous_revenue
  FROM monthly_revenue
)
SELECT order_month, revenue, previous_revenue,
  ROUND(((revenue - previous_revenue) / previous_revenue) * 100, 2) AS growth_percent
FROM with_previous;

G) Problem 7 – Employee Salary Ranking
1.	Rank employees by salary, using RANK()
SELECT name, department, salary,
  RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;

2.	Rank employees by salary, using DENSE_RANK()
SELECT name, department, salary,
  DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_dense_rank
FROM employees;

3.	Rank employees by salary within their own department
SELECT name, department, salary,
  RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_salary_rank
FROM employees;



CREATE TABLE employees (
  employee_id INT PRIMARY KEY,
  name VARCHAR(50),
  department VARCHAR(30),
  salary DECIMAL(10,2)
);

INSERT INTO employees (employee_id, name, department, salary) VALUES
(1, 'Rohan Verma', 'Sales', 45000),
(2, 'Ananya Iyer', 'Sales', 52000),
(3, 'Vikram Singh', 'IT', 60000),
(4, 'Neha Joshi', 'IT', 75000),
(5, 'Arjun Rao', 'HR', 40000),
(6, 'Kavita Nair', 'HR', 48000);

SELECT name, department, salary,
  RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;


SELECT name, department, salary,
  RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_salary_rank
FROM employees;


