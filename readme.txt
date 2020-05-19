Build docker image so you can use TA-lib using python.

See https://mrjbq7.github.io/ta-lib/

# Note: You may need "sudo" before this command.
docker build -t ta-lib-docker:latest .

# You can run your local scripts like this:
# (which will volume mount the current directory as "/ta" on the docker container)
docker run --rm -it -v $(pwd):/ta mkinney/ta-lib-docker python /ta/one.py

# Or like this:
docker run --rm -it -e "CBPRO_API_KEY=$CBPRO_API_KEY" -e "CBPRO_SECRET=$CBPRO_SECRET" -e "CBPRO_PASSWORD=$CBPRO_PASSWORD" -v $(pwd):/ta mkinney/ta-lib-docker python /ta/cbpro_openorders.py

# to make this easier you can simply do this:
./run cbpro_openorders.py
