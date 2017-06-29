test:: test_unit style_test report

modules = chibi_command

style_test: flakes pep8

test_unit:
	@echo "Running tests"
	@pytest --cov-config .coveragerc --cov .

report:
	@coverage report
	@coverage html

open_report_firefox:
	@nohup firefox .coverage_html_report/index.html > /dev/null &

clean:
	@echo "Running clean..."
	@find . -name ".*.sw*" -exec rm {} +
	@rm -rf .coverage .coverage_html_report

style:
	@echo "Running flake8 test...."
	@flake8 ${modules}

pep8:
	@echo "Running pep8 tests..."
	@pep8 --statistics ${modules}

flakes:
	@echo "Running flakes tests..."
	@pyflakes ${modules}
