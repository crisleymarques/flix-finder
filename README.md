<h1 align="center"> 
	Flix Finder 📽️
</h1> 

<h4 align="center"> 
	🎬🎟  Movie and Series Recommender 📺🍿
</h4>

<p align="center">
 <a href="#description">Description</a> •
 <a href="#technologies">Technologies</a> •
 <a href="#how-to-run">How to run</a> • 
 <a href="#authors">Authors</a>
</p>

## Description 📋
Flix Finder is a movie and TV series recommendation tool. Discover your next binge-worthy content based on genres, styles, decades, or your favorite references. Built using the powerful GPT-3.5 model for personalized recommendations.

## Technologies 🛠
[![Python](https://img.shields.io/badge/Python-336d9d?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GPT](https://img.shields.io/badge/GPT--3.5-75ac9d?style=for-the-badge&logo=openai&logoColor=white)](https://chat.openai.com/)
[![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)


## How to run 💻
### - Prerequisites
You need to have installed on your machine [Git](https://git-scm.com), [Python3](https://www.python.org/), [Docker](https://www.docker.com/), and [Nodejs](https://nodejs.org/en).

### Clone this repository
```bash
git clone https://github.com/crisleymarques/flix-finder.git
```

### Set up your OpenAI API Key
1. Create an account on [OpenAI](https://beta.openai.com/).
2. Create an API Key and copy it.
3. Go to the project folder and create a file named .env substituting the 'your_openai_api_key' with your API Key.
```bash
echo "OPENAI_API_KEY = 'your_openai_api_key'" > src/.env
```
### Running the Backend
1. Go to the project folder and build the docker image.
```bash
docker build -t fastapi/flixfinder . 
```
2. Run the docker image.
```bash
docker run -p 8000:8000 fastapi/flixfinder
```
The backend will be accessible at http://localhost:8000.

### Running the Frontend
1. Go to the front folder:
```bash	
cd front
```
2. Install the dependencies
```bash
npm install 
```
2. Run the project.
```bash
npm run dev
```
The Frontend will be accessible at http://localhost:5173/.

Enjoy! 🎉

## Authors 🧑‍💻

| [<img src="https://avatars.githubusercontent.com/u/44072771?s=400&u=b17d945fa43dec67a69d1cb11e2f23a7b2e0ad95&v=4" width="120px;"/><br /><sub><b>Crisley Marques</b></sub>](https://github.com/crisleymarques) <br/> | [<img src="https://avatars.githubusercontent.com/u/62178110?v=4" width="120px;" /><br /><sub><b>Luiz Carlos</b></sub>](https://github.com/LuizCarlosXavier) <br/> | 
| :---: | :---: | 
