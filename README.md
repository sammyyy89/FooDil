# FooDil 
© 2022 Saemi An <saemi0809@gmail.com>

<img src="https://img.shields.io/badge/Django-0C9D58?style=flat-square&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white"/> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=Javascript&logoColor=white"/> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=white"/> <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white"/>

Web application for online food ordering system created with Django, Python, HTML, CSS, JavaScript, Bootstrap and SQLite 

#

### :tulip: Project Demo
<a href="https://drive.google.com/file/d/1FrY3DlAPn8p6kDoCgq32KBbh5W5e86Vl/view?usp=sharing">Click Me</a> 

#

### :question: Why I Chose Django for this Project
Django's official documentation introduces Django as "the web framework for perfectionists with deadlines". Django seemed to have many advantages to build a quality application within limited time. Below are the main reasons why I chose Django to develop FooDil.  

1. Highly Secure  
  Django has built-in protection for some common security issues such as cross site scripting (XSS), cross site request forgery (CSRF), session security, and SQL injection. Django also automatically encrypts the passwords with a security key while transmitting data.
  
2. Good Official Documentation   
The documentation provided by Django is very helpful because it is well-organized with example code.

3. Built with Python    
Python is the language I use most frequently and Django works on Python. 

4. Admin Panel by Default  
Unlike most other frameworks, Django offers the admin panel by default so that developers can create/read/update/delete the application's database objects. This saves so much time and effort. 

5. Scalable   
FooDil would ideally be used by multiple users. Popular websites like Spotify, YouTube, and Netflix use Django and this shows that Django has the capacity to handle numerous users at a time. 

#

### :bulb: Introduction
  FooDil is...
  - An independent and self-contained system
  - Limited to New York City area for localized and focused service
  - Developed for both customers and restaurant owners

#

### :crystal_ball: Purpose
To help customers place an order at a restaurant conveniently and assist restaurants manage their data such as menu, business hours, and orders from various customers easily. 
By ordering virtually at any time using our system, customers can save time and money spent on travelling to pick up the food.

#

###  :pushpin: Primary Functions 
  #### :family: Customer
  - Registration: Customer can create a FooDil account. 
  - Login: Customer whose information exists in the database can login.
  - Search: Customer can view and find specific restaurants and their menu items.
  - Order: Customer can place an order by adding items in cart.
  - Payment: Customer can pay with cash or PayPal.
  
  #### :hamburger: Restaurant
   - Registration: Restaurant staff can create a FooDil business account.
   - Login: Restaurant staff whose information exists in the database can login.
   - Restaurant Data Management: Restaurant staff can add, read, update, or delete their data such as menu items 
   - Order Status Update: Restaurant staff can update customers' order status, which will be seen by the customers 
   
   #
   
### :pencil2: Entity-Relationship (ER) Diagram for the Database
   <img width="300" src="https://user-images.githubusercontent.com/28698521/202060698-861577b0-0e26-4cb3-a483-705af797bb0c.JPG">
   
   #
   
### :bookmark: Assumptions 
   1. Users must be trained for basic computer functionalities 
   2. Users must have the basic knowledge of English 
   3. The user interface of system must be easy and simple to use 
   4. The system must respond to every request within reasonable time (within 5 seconds)
    
# 
    
 ### :seedling: System Models

<a href="https://drive.google.com/file/d/1cJKBRBSwp8MVQAK-Mxb2FSYGbtq9G_PT/view?usp=sharing">Context Model</a>, <a href="https://drive.google.com/file/d/1uwkxhNAlNEOFve6XMCWlAFGN1QEVgDKo/view?usp=sharing">Use Case</a>, <a href="https://drive.google.com/file/d/1JtOK6CidasSFGg2jxIHS56k8pdLzzZa-/view?usp=sharing">Activity Model</a>, <a href="https://drive.google.com/file/d/1TENP4ck-o4Z5-ODqLmb4IMkBAVhp_65p/view?usp=sharing">Sequence Model</a>

#

### :paw_prints: Architectural Pattern
Model-View-Template (MVT) architecture. 






    
