=======================================
scraper_service proof_of_concept

Brandon Bagwell, June 2024
brandon@bagwellonline.com
A small flask application
=======================================

README documentation goes here

# Pre-requisites:
	* make installed
	* docker installed and running
	* bats installed (required for unit tests... run 'apt-get install --yes bats' if necessary)
	* Internet Connectivity

# Build Instructions:

	To build the container, run 'make'

# To start the container (using docker)

	To start a container instance on the local box, run 'make run'

# Anything else?

        'make stop'  stops the container
	'make clean' nukes the image
        'make batstest'  runs the bats tests (bats installed seperately!)

# Is there any saved state?

	Metrics are stored in tblArray.json within the container.  If this were not a POC, the metrics would be stored in a bind mounted file location, docker volume, or for a more advanced deployment, a Kubernetes CSI container.

# Other notes

	Right now the behavior is to return the current set of metrics everytime there is a scrape.  The instructions didn't say the output had to blank, and it was great for debugging.  The behavior is left in for now.	
