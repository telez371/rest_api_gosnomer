
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

GET | /PLATE/GENERATE
This endpoint allows you to generate a specified amount of state vehicle registration numbers.

Parameters
<li><code>token</code>: Bearer token for Authorization 65ded53be0a581a8554f340cc3640ee41f9a5525</li>
<li><code>amount</code>: Number of registration numbers to generate in the response</li>

Example Request

<pre>
<span class="key">/PLATE/GENERATE?amount=5</span>
</pre>

Response

<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"1"</span>: <span class="value">"В261СА31"</span>,
<span class="key">"2"</span>: <span class="value">"О022КР93"</span>,
<span class="key">"3"</span>: <span class="value">"О424ТО92"</span>,
<span class="key">"4"</span>: <span class="value">"Р557УН161"</span>,
<span class="key">"5"</span>: <span class="value">"К248КС150"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>
GET | /PLATE/GET
This endpoint allows you to retrieve a specific state vehicle registration number record by its ID.

Parameters
<li><code>token</code>: Bearer token for Authorization 65ded53be0a581a8554f340cc3640ee41f9a5525</li</li>
<li><code>id</code>: ID of the registration number record in the format of uuid4</li>

Example Request

<pre>
<span class="key">/PLATE/GET?id=adc3e6f7-3ba7-42e7-8616-f3b0ed3f9760</span>
</pre>

Response

<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"adc3e6f7-3ba7-42e7-8616-f3b0ed3f9760"</span>: <span class="value">"А777ЕУ77"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>

POST | /PLATE/ADD
This endpoint allows you to add a new state vehicle registration number to the database.
Before adding, the correctness of the registration number is checked.

Parameters
<li><code>token</code>: Bearer token for Authorization 65ded53be0a581a8554f340cc3640ee41f9a5525</li>
<li><code>plate</code>: State vehicle registration number</li>

Example Request
<pre>
<span class="key">/PLATE/ADD?plate=a888еу77</span>
</pre>

Response

<pre>
<span class="key">{</span>
<span class="key"> </span>
<span class="key">"42465c4b-05f7-46bf-810f-c931824fee5c"</span>: <span class="value">"А888ЕУ77"</span>,
<span class="key"> </span>
<span class="key">}</span>
</pre>

## Usage

The application has the following endpoints:

<li><code>GET /PLATE/GENERATE</code>: Generate new car numbers with a specified quantity</li>
<li><code>GET /PLATE/GET</code>: Retrieve a list of generated car numbers</li>
<li><code>POST /PLATE/ADD</code>: Add a new car numbers to the database</li>


## Acknowledgments

<li><a href="https://pypi.org/project/gosnomer/" target="_new">gosnomer</a> library</li>
<li><a href="https://flask.palletsprojects.com/" target="_new">Flask</a></li>
<li><a href="https://www.sqlalchemy.org/" target="_new">SQLAlchemy</a></li>

