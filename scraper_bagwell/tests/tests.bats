@test "docker is running" {
	# Is this docker-ce, containerd, Ubuntu's flavor, etc etc
	ps aux | grep docker
}

@test "bagwell_container is running" {
	docker ps -a | grep bagwell_container | grep Up
}

@test "version endpoint works" {
	wget -q http://localhost:8080/version > /dev/null
}

@test "metrics endpoint works, and returns at least one entry" {
        entries=`wget -q -O - http://localhost:9095/metrics | wc -l`
	[[ $entries -gt 0 ]]
}
