
## rest_api_gosnomer


<p align="left">
     <a href="https://ibb.co/Bwn5LDD"><img src="https://i.ibb.co/Bwn5LDD/nomer2-1024x363-800x800.png" alt="nomer2-1024x363-800x800" border="0"></a>
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

<p align="left">
      <img src="https://skr.sh/i/280123/0vVOeEw1.jpg?download=1&name=%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2028-01-2023%2015:36:28.jpg">
</p>

GET | /PLATE/GET
This endpoint allows you to retrieve a specific state vehicle registration number record by its ID.

Parameters
<li><code>token</code>: Bearer token for Authorization 65ded53be0a581a8554f340cc3640ee41f9a5525</li</li>
<li><code>id</code>: ID of the registration number record in the format of uuid4</li>

Example Request

<p align="left">
      <img src="https://skr.sh/i/280123/fvQPV0WU.jpg?download=1&name=%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2028-01-2023%2015:44:45.jpg">
</p>

POST | /PLATE/ADD
This endpoint allows you to add a new state vehicle registration number to the database.
Before adding, the correctness of the registration number is checked.

Parameters
<li><code>token</code>: Bearer token for Authorization 65ded53be0a581a8554f340cc3640ee41f9a5525</li>
<li><code>plate</code>: State vehicle registration number</li>

Example Request
<p align="left">
      <img src="https://skr.sh/i/280123/E4RquaMQ.jpg?download=1&name=%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2028-01-2023%2015:51:54.jpg">
</p>

## Usage

The application has the following endpoints:

<li><code>GET /numbers</code>: Retrieve a list of generated car numbers</li>
<li><code>POST /generate</code>: Generate new car numbers with a specified quantity</li>
<li><code>POST /numbers</code>: Add a new car numbers to the database</li>


## Acknowledgments

<li><a href="https://pypi.org/project/gosnomer/" target="_new">gosnomer</a> library</li>
<li><a href="https://flask.palletsprojects.com/" target="_new">Flask</a></li>
<li><a href="https://www.sqlalchemy.org/" target="_new">SQLAlchemy</a></li>

## License

This project is licensed under the MIT License - see the LICENSE file for details.
