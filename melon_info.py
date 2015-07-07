"""
Prints out all the melons in our inventory
"""

from melons import melon_data


# def print_melon(melon_data):
#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print "%ss %s seeds and are $%0.2f" % (name, have_or_have_not, price)


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])


def print_melon_data(melon_data):
	for melon, attributes in melon_data.items():
		print melon
		for attribute, value in attributes.items():
			print "%s : %s " % (attribute, value)
		print '\n'


print print_melon_data(melon_data)

