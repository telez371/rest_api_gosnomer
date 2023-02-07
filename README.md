
## rest_api_gosnomer


<p align="left">
     <a href="https://ibb.co/Bwn5LDD"><img src="https://i.ibb.co/Bwn5LDD/nomer2-1024x363-800x800.png" alt="nomer2-1024x363-800x800" border="0"></a>
</p>

<p align="left">
   <img src="https://img.shields.io/badge/flask-2.2.2-blueviolet" alt="flask Version" >
   <img src="https://img.shields.io/badge/uuid-1.30-blue" alt="uuid Version">
   <img src="https://img.shields.io/badge/PostgreSQL-14-orange" alt="PostgreSQL Version">
   <img src="https://img.shields.io/badge/LICENSE-MIT-brightgreen" alt="License">
</p>

## Description

This project is a web application built with Flask, a micro web framework for Python. The application allows users to generate and store unique car numbers using the gosnomer library. The application utilizes a SQLAlchemy ORM to interact with a database PostgreSQL and handle data.

## Documentation

swagger documentation.


Example Request

<pre>
<span class="key">/swagger-ui</span>
</pre>



POST | /PLATE/REGISTER
Registration for receiving a Bearer Token.


Example Request

<pre>
<span class="key">/PLATE/REGISTER</span>
</pre>



Parameters
<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"email"</span>: <span class="value">"test@gmail.com"</span>,
<span class="key">"name"</span>: <span class="value">"TestUser"</span>,
<span class="key">"password"</span>: <span class="value">"qwertyui"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>

Response

<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"access_token"</span>: <span class="value">"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVza
CI6ZmFsc2UsImlhdCI6MTY3NTc3MzE3NSwianRpIjoiMjQzMjBiMWUtMmFhNS00MGYxLTkwMWQtNjUyMDA3ZWM4NjAwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6M
iwibmJmIjoxNjc1NzczMTc1LCJleHAiOjE2Nzc4NDY3NzV9.cH9dvtlcC77_OpA-_kEseueXwp0vztEoUDtKiWzB-Xw"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>


POST | /PLATE/LOGIN
Authorization.


Example Request

<pre>
<span class="key">/PLATE/LOGIN</span>
</pre>



Parameters
<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"email"</span>: <span class="value">"test@gmail.com"</span>,
<span class="key">"password"</span>: <span class="value">"qwertyui"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>

Response

<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"access_token"</span>: <span class="value">"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVza
CI6ZmFsc2UsImlhdCI6MTY3NTc3MzE3NSwianRpIjoiMjQzMjBiMWUtMmFhNS00MGYxLTkwMWQtNjUyMDA3ZWM4NjAwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6M
iwibmJmIjoxNjc1NzczMTc1LCJleHAiOjE2Nzc4NDY3NzV9.cH9dvtlcC77_OpA-_kEseueXwp0vztEoUDtKiWzB-Xw"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>

GET | /PLATE/GENERATE
This endpoint allows you to generate a specified amount of state vehicle registration numbers.


Example Request

<pre>
<span class="key">/PLATE/GENERATE?amount=5</span>
</pre>



Parameters
<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"amount"</span>: <span class="value">"2"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>

Response

<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"generate_car_numbers"</span>: <span class="value">"[{1: 'О166ВЕ90', 2: 'О507УР44'}]"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>

GET | /PLATE/GET
This endpoint allows you to retrieve a specific state vehicle registration number record by its ID.


<li><code>id</code>: ID of the registration number record in the format of uuid4</li>

Example Request

<pre>
<span class="key">/PLATE/GET?id=0e9b309b-7821-4c43-9b07-9f5bb63107af</span>
</pre>

Parameters
<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"id"</span>: <span class="value">"0e9b309b-7821-4c43-9b07-9f5bb63107af"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>

Response

<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"auto_numbers"</span>: <span class="value">"А463ЕА799"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>

POST | /PLATE/ADD
This endpoint allows you to add a new state vehicle registration number to the database.
Before adding, the correctness of the registration number is checked.


Parameters
<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"auto_numbers"</span>: <span class="value">"А465eА799"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>

Response

<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"auto_numbers"</span>: <span class="value">"А465ЕА799"</span>,
<span class="key">"id"</span>: <span class="value">"37750d34-f01b-472b-8d67-34b9fe9e8581"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>

## Usage

The application has the following endpoints:
<li><code>GET /swagger-ui</code>: swagger documentation</li>
<li><code>GET /PLATE/GENERATE</code>: Generate new car numbers with a specified quantity</li>
<li><code>GET /PLATE/GET</code>: Retrieve a list of generated car numbers</li>
<li><code>POST /PLATE/ADD</code>: Add a new car numbers to the database</li>
<li><code>GET /PLATE/REGISTER</code>: Registration for receiving a Bearer Token</li>
<li><code>POST /PLATE/LOGIN</code>: Authorization</li>
