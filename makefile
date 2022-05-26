NAME=sdir
TEMP=build dist
all:
	pyinstaller $(NAME).py

run-exe:
	dist/$(NAME)/$(NAME).exe
run:
	python $(NAME).py


clean:
	del $(NAME).spec
	rd /Q /S $(TEMP)
