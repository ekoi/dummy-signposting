# dummy-signposting
Dummy Signposting Generator

http://localhost:2907/links/linkset-01.json

poetry build;poetry install; docker rm -f dummy-signposting-service; docker rmi ekoindarto/dummy-signposting-service:0.1.2; docker build --no-cache -t ekoindarto/dummy-signposting-service:0.1.2 -f Dockerfile . ;docker run -d -p 2907:2907 --name dummy-signposting-service ekoindarto/dummy-signposting-service:0.1.2; docker exec -it dummy-signposting-service /bin/bash 

