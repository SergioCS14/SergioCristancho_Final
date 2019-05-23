CristanchoSergio_final_15.pdf : CristanchoSergio_final_15.py Datos15.dat
	python CristanchoSergio_final_15.py
Datos15.dat : a.out
	./a.out
a.out : CristanchoSergio_Final_15.cpp
	g++ CristanchoSergio_Final_15.cpp