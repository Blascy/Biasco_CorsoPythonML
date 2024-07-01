#prima parte:
#Create un file.txt con uno script python scaricando manualmente testo preso da https://it.lipsum.com/
#Seconda parte:
#create un programma che legge il documento e ci restituisce il numero di parole, righe e caratteri.

#Definisco il testo copiato da Lipsum.com
testo = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris at libero diam. 
Etiam non elementum ante. Phasellus lobortis erat id ornare auctor. 
Vestibulum porta libero malesuada, ultrices nisl ac, mattis elit. 
Nunc vel ante quis dolor faucibus congue. Sed commodo lorem sed consequat consequat. 
Donec suscipit ullamcorper tristique. Cras auctor rhoncus magna quis hendrerit. 
Nullam vulputate et eros a ultricies. 
Sed et ullamcorper arcu. Morbi commodo libero id justo blandit, id malesuada arcu rutrum. 
In vehicula ex in mattis feugiat. Nulla facilisi."""

#Apri un file in modalità scrittura
nome_file = "file.txt"
file = open(nome_file, 'w')

#Scrivo il testo nel file
file.write(testo)

#Chiudo il file
file.close()

print(f"Il testo è stato scritto nel file {nome_file}.")

#Apri il file in modalità lettura ('r').
#Leggi tutto il contenuto del file.
#Conta le righe utilizzando splitlines().
#Conta le parole utilizzando split().
#Conta i caratteri utilizzando len().

#apro file in modalita lettura
file = open(nome_file, 'r')

contenuto = file.read()

numero_righe = len(contenuto.splitlines()) #
numero_parole = len(contenuto.split())
numero_caratteri = len(contenuto)

file.close()

print(f"Numero di righe: {numero_righe}")
print(f"Numero di parole: {numero_parole}")
print(f"Numero di caratteri: {numero_caratteri}")

