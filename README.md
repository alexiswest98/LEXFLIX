![lexflix_logo](https://user-images.githubusercontent.com/96459347/211291604-ed5fba36-a5cd-4653-9e5d-f3644a944519.png)

# About

LEXFLIX is a Full Stack web application clone of Netflix. Similar to the original website, LEXFLIX allows you to sign up, create profiles, review Movies, and watch trailers.

## Check out the live site:
https://lexflix.onrender.com

<img width="1420" alt="Screenshot 2023-01-09 at 3 02 16 AM" src="https://user-images.githubusercontent.com/96459347/211293784-359c1935-7842-4781-9870-e86a530347be.png">
<img width="1414" alt="Screenshot 2023-01-09 at 3 02 44 AM" src="https://user-images.githubusercontent.com/96459347/211293803-8d804b5b-5366-4e8b-9dc1-c4bff7a05d78.png">
<img width="915" alt="Screenshot 2023-01-09 at 3 02 57 AM" src="https://user-images.githubusercontent.com/96459347/211293835-26fa473a-8f6b-4b92-94bb-fb9338ef5391.png">


## Project Wiki
- [Database Schema](https://github.com/alexiswest98/LEXFLIX/wiki/DB-Diagram-Schema)
- [Feature List](https://github.com/alexiswest98/LEXFLIX/wiki/Feature-List)
- [User Stories](https://github.com/alexiswest98/LEXFLIX/wiki/User-Stroies)
- [Wire Frames](https://github.com/alexiswest98/LEXFLIX/wiki/Wire-Frames)

#### Frameworks, Platforms, & Libraries:
- ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
- ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
- ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
- ![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)
- ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
- ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
- ![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)
- ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

 #### Editors, IDEs, & Misc:
 - ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
 - ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)


#### Database:
- ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

1. Clone the repo:

    HTTPS Authentification:
    git clone https://github.com/alexiswest98/LEXFLIX.git

    SSH Authentification with SSH:
    git clone git@github.com:alexiswest98/LEXFLIX.git

2. Install dependencies: pipenv install -r requirements.txt
 
3. Navigate to the root: pipenv install
  
4. Create a .env file in the root of the backend folder and copy the contents from the .env.example file:
    cp .env.example .env

4. Migrate and seed the files. Enter the shell via pipenv shell, then:
    flask db upgrade
    flask seed all
    
5. Utilize pipenv shell in the root folder.
    pipenv shell
    flask run
 
6. Navigate to the frontend react folder and npm install.
    npm install
    
7. Utilize npm start in the front-end folder and you will be directed to: http://localhost:3000/
    npm start

## Feature Roadmap

- [x] Profiles
    - [x] Create a profile
    - [x] Load all profiles
    - [x] Create a profile
    - [x] Update a profile
    - [x] Delete a profiles
- [x] Movies
    - [x] View Movie carousel
    - [x] See individual movie details on hover
    - [x] See individual movie details modal
    - [x] Delete a task
- [x] Movie Reviews
    - [x] Create a review for a movie
    - [x] View existing reviews for movies
    - [x] Create a movie review
    - [x] Update a movie review
    - [x] Delete a movie review


## Get in touch!
- [Alexis' GitHub](https://github.com/alexiswest98)
- [Alexis' Linkedin](https://www.linkedin.com/in/alexis-west-596a6b203/)
