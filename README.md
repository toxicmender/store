# Simpl

A short Full Stack demo app for implementing a simple e-commerce site

## Instructions for local deployment

1. Create a `python3` virtual environment:
    > Minimum Python version 3.6+, recommended 3.10+

    ```sh
    virtualenv env
    ```

    > if your system still has python2 as default python make sure you have python3 and then:

    ```sh
    virtualenv env -p python3
    ```

2. Activate the virtualenv:
   - for Mac/Linux (use the extension for your respective shells, like `.sh`, `.bash`, `.zsh`, etc)

      ```sh
      source env/bin/activate
      ```

   - for windows

     ```sh
     .\env\Scripts\activate.ps1
     ```

3. Install the dependencies from [`requirements.txt`](https://raw.githubusercontent.com/toxicmender/SB-FullStack-Task/main/requirements.txt)

    ```sh
    pip install -r requirements.txt
    ```

4. Run django `makemigration`s and then `migrate` for initializing the database (SQLite3)

    ```sh
    python ./manage.py makemigrations
    ```

    ```sh
    python ./manage.py migrate
    ```

5. Create a superuser for admin interface

    ```sh
    python manage.py createsuperuser
    ```

6. Run the server

    ```sh
    python ./manage.py runserver
    ```

7. Install storefront dependencies

    ```sh
    cd storefront
    npm install
    ```

8. Run the server

    ```sh
    npm run dev
    ```
