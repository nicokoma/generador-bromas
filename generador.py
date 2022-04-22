import random

def main():
	animales = ["el elefante", "la gallina", "la cotorra", "el toro", "la morsa", "el manati", "la vaca", "la iguana", "el conejo", "el lobo", "el perro", "el gato", "la libre", "el raton", "la chinchilla"]
	verbos = ["acariciar", "consultar", "trabajar", "animar", "ensuciar", "sacudir", "lustrar", "pulir", "encerar", "desmembrar", "degollar", "aplaudir", "educar", "ayudar"]
	
	for i in range(20):
		print(random.choice(verbos) + " " + random.choice(animales))
 

if __name__== "__main__":
	main()