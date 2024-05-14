all:
	mkdir target
	gcc ./src/func.c -o ./target/libfunc.so -shared -fPIC
	gcc ./src/main.c -o ./target/main.out -L./target -lfunc

install:
	sudo cp ./target/libfunc.so /usr/lib/libfunc.so
	cp ./target/main.out ./main.out

run: main.out
	./main.out

clean:
	rm -rf ./target/
	rm -rf main.out

uninstall:
	sudo rm -rf /usr/lib/libfunc.so