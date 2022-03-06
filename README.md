# Justin_flask

## This code is used for displaying hardware usage from your docker host on a web page.

##### The hardware usage will refresh every time you refresh the page.

Use `docker build -f .\dockerfile -t my-host .` to build your image.

Use `docker run -d -p 5000:5000 my-host` to run your container. You can take off the `-d` if you want to watch it run in the CLI.

Use `docker ps` to check on the container while running in detached mode.
