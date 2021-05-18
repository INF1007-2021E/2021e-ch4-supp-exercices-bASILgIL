#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	return len(string) % 2 == 0


def get_num_char(string, char):
	i = 0
	for chr in string:
		if chr == char:
			i += 1

	return i


def get_first_part_of_name(name):
	prenom = name.split("-")[0]
	prenom_cap = prenom[0].capitalize() + prenom[1:]
	return "Bonjour, " + prenom_cap


def get_random_sentence(animals, adjectives, fruits):
	words = []
	for word in (animals, adjectives, fruits):
		words += [word[random.randrange(0, len(word))]]

	return "Aujourd’hui, j’ai vu un %s emparer d’un panier %s plein de %s." % tuple(words)


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
