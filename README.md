# dummy-signposting
Dummy Signposting Generator

poetry build;poetry install; docker rm -f dummy-signposting-service; docker rmi ekoindarto/dummy-signposting-service:0.1.0; docker build --no-cache -t ekoindarto/dummy-signposting-service:0.1.0 -f Dockerfile . ;docker run -d -p 2907:2907 --name dummy-signposting-service ekoindarto/dummy-signposting-service:0.1.0; docker exec -it dummy-signposting-service /bin/bash 

