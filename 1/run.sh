./compiler.py ${1-inp.HNI} inp.BIN &&
./compiler.py ${2-prg.HNI} prg.BIN &&
./interpreter inp.BIN prg.BIN
