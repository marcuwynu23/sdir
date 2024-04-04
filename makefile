FILE=sdir.py
COMMAND=pyinstaller
PROD_LOCATION=C:\tool\bin

all:
	$(COMMAND) $(FILE) --onefile
prod:
	$(COMMAND) $(FILE) --onefile --distpath $(PROD_LOCATION)
clean:
	rm -rf build dist sdir.spec