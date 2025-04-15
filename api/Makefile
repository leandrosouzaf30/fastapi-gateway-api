APP = fastapi-gateway-api

setup-dev:
	@kind create cluster --config k8s/config/config.yaml
	@kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml
	@kubectl wait --namespace ingress-nginx \
		--for=condition=ready pod \
		--selector=app.kubernetes.io/component=controller \
		--timeout=270s

teardown_dev:
	@kind delete clusters kind

deploy-dev:
	# @docker build -t $(APP):latest .
	# @kind load docker-image $(APP):latest
	@kubectl apply -f k8s/manifests
	@kubectl rollout restart deploy fastapi-gateway-api

dev: setup-dev deploy-dev

