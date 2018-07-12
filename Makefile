HOST=127.0.0.1
TEST_PATH=./

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	-exec sudo python cleanup.py

main:
	-exec sudo python main.py

path:
	-exec sudo python pathfinder.py
