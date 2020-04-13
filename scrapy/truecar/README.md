this scrapy project extract all tesla model 3 announcment on truecar.com with this command:

be sure to be in the project folder before running

scrapy crawl truecar -s USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36' -o truecar.csv
