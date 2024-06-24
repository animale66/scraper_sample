# Sample Makefile here

default:  
	docker build -t bagwell .

clean:
	docker rmi bagwell
run:      
	docker run --name bagwell_container -d --rm -ti -p 8080:8080 -p 9095:8080 bagwell

stop: 
	docker stop bagwell_container
batstest:	 
	bats tests/*.bats
