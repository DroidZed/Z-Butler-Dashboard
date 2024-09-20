include .env

deps:
	poetry install --no-root

install-front:
	litestar assets install

dev:
	litestar run

build-front:
	litestar assets build

module:
	mkdir ./src/modules/${MODULE_NAME}

	touch ./src/modules/${MODULE_NAME}/service.py
	touch ./src/modules/${MODULE_NAME}/routes.py
	touch ./src/modules/${MODULE_NAME}/controller.py
	touch ./src/modules/${MODULE_NAME}/test_${MODULE_NAME}.py
	echo "from .${MODULE_NAME} import *" >> ./src/modules/__init__.py

test:
	py -m pytest -vs .

build:
	docker build -t droidzed/z-butler-dashboard:$(IMAGE_TAG) .
