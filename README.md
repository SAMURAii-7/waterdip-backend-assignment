# Waterdip AI Backend Assignment

## Installation

1. Clone the repo
    ```sh
    git clone
    ```
2. Create a virtual environment
    ```sh
    python3 -m venv env
    ```
3. Activate the virtual environment
    ```sh
     source .venv/Scripts/activate
    ```
4. Install requirements
    ```sh
    pip install -r requirements.txt
    ```
5. Run the server
    ```sh
    flask run
    ```
6. Run the tests
    ```sh
    pytest test.py
    ```
7. Open the browser and go to the URL:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Build and Run using Docker

-   Build the docker image
    ```sh
    docker build -t waterdip .
    ```
-   Run the docker image
    ```sh
    docker run -it --rm -p 5000:80 waterdip
    ```
-   Open the browser and go to the URL: [http://localhost:5000](http://localhost:5000)

## Postman Collection

-   Import the postman collection using the json file in the repo
-   The collection contains all the requests with sample request data
