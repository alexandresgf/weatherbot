# Weather Bot

Weather bot was built to extract weather information from ClimaTempo website

## How to run?

1. Requirements

- Python 3.8 (or latest)
- Pipenv (latest)
- Git client
- Docker (latest)
- Docker-Compose (latest)

2. Clone the repository using a git client

`git clone https://github.com/alexandresgf/weatherbot.git`

3. Get into the folder

`cd /path/to/weatherbot`

4. Install the dependencies using Pipenv

`pipenv install`

5. Copy the environment file to the config folder

Place the `.env` file into the folder `/path/to/weatherbot/config`.

6. Start the docker containers

`docker-compose up`

7. Get into the virtualenv shell using Pipenv

Inside the Weather Bot folder run the command: `pipenv shell`

8. Use the scrapyd-deploy to deploy the Scrapy Project to the Scrapyd service

Inside the Pipenv Shell and in the Weather Bot root folder, run the command: `scrapyd-deploy`

9. Do the first run

Run all the available spiders from the Weather Bot project: `scrapyd-client schedule -p weatherbot \*`

## Notes

- It should be done a first run to check if the bot is running correctly
