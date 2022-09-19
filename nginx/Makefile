all: apply

k3s:
	sudo curl -sfL https://get.k3s.io | sh -

k3s_upgrade:
	sudo curl -sfL https://get.k3s.io | INSTALL_K3S_CHANNEL=latest sh -

build:
	cd hostis
	docker-compose build
	docker tag hostis docker-registry:5000/hostis
	docker push docker-registry:5000/hostis
	cd - 

apply:
	sudo kubectl apply -f nginx01.yaml

delete:
	sudo kubectl delete -f nginx01.yaml

test:
	curl localhost
