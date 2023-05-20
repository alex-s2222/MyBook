docker rm -f `docker ps -aq`

docker run --name main --network pr5 -v $(pwd):/pocod -w /pocod -dit pr5
docker run --name c1 --network pr5 -v $(pwd):/pocod -dit pr5
docker run --name c2 --network pr5 -v $(pwd):/pocod -dit pr5

docker exec c1 service ssh start
docker exec c2 service ssh start

docker exec -it main bash
