# Test dockerizing Django with Postgres and Travis.ci
## Want to use this project?
### Development

Uses the default Django development server.

1. Update the environment variables in the *docker-compose.yml* file.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.
    
### Production

Uses gunicorn + nginx.