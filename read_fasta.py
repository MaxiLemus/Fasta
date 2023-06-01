#!/usr/bin/python3
from Bio import SeqIO

codigos_tres_letras = {
    'A': 'Ala',
    'R': 'Arg',
    'N': 'Asn',
    'D': 'Asp',
    'C': 'Cys',
    'E': 'Glu',
    'Q': 'Gln',
    'G': 'Gly',
    'H': 'His',
    'I': 'Ile',
    'L': 'Leu',
    'K': 'Lys',
    'M': 'Met',
    'F': 'Phe',
    'P': 'Pro',
    'S': 'Ser',
    'T': 'Thr',
    'W': 'Trp',
    'Y': 'Tyr',
    'V': 'Val'
}

archivo = "/root/Fasta/datos.fasta"

for registro in SeqIO.parse(archivo, "fasta"):
    secuencia_aminoacidos = str(registro.seq)

    codigos_tres_letras_secuencia = [codigos_tres_letras[aminoacido] for aminoacido in secuencia_aminoacidos]

    print("Secuencia de aminoácidos:", secuencia_aminoacidos)
    print("Códigos de tres letras:", " ".join(codigos_tres_letras_secuencia))
