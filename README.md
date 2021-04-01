# SX project
>Processing JSON and getting bitcoin price APIs

## Technologies
> * Python 3.8<br>
> * Django 3.1.7<br>
> * Django Rest Framework 3.12.4<br>

## Requirements
> 1. Get json input of data list, return sorted data list and add sha256 to each row
> 2. Get json input of bitcoin amount and calculate price based on current orderbook (https://bitbay.net/API/Public/BTCPLN/orderbook.json)

## Testing
>1. 
>>curl -X POST -H "Content-Type: application/json" -d @test_file2.json http://localhost:8000/zadanie1/
>2. 
>>curl -X POST -H "Content-Type: application/json" -d @test_file.json http://localhost:8000/zadanie2/

## Example env file for local development
* There are example env files in /env/dev/.env or /env/prod/., which normally would be excluded from repository
## Run application
> sh start.sh
## Comments
>HTTP used for development purposes -> switch to HTTPS for production deployment



