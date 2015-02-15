all: debug

debug:
	dev_appserver.py --host 0.0.0.0 .

deploy:
	appcfg.py update --oauth2 .
