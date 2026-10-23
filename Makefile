.PHONY: test figs clean

test:
	pytest tests/ -q

figs:
	mkdir -p figures
	for f in scripts/fig*.py; do python $$f; done

clean:
	rm -rf figures build *.egg-info
