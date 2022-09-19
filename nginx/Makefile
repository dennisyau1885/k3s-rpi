all: install

k3s:
	sudo curl -sfL https://get.k3s.io | sh -

k3s_upgrade:
	sudo curl -sfL https://get.k3s.io | INSTALL_K3S_CHANNEL=latest sh -

install:
	kubectl apply -f nginx01.yaml

remove:
	kubectl delete -f nginx01.yaml

test:
	curl localhost

upgrade:
	
