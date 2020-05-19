Build docker image so you can use TA-lib using python.

See https://mrjbq7.github.io/ta-lib/

# Note: You may need "sudo" before this command.
docker build -t ta-lib-docker:latest .

# You can run your local scripts like this:
# (which will volume mount the current directory as "/ta" on the docker container)
docker run -it -v $(pwd):/ta mkinney/ta-lib-docker python /ta/one.py
