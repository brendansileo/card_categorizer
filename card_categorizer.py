import mtg_thesaurus

def get_card_category(card_name):
    similars = mtg_thesaurus.findSimilar(card_name)
    if similars == -1:
    	return -1
    with open('categories.txt', 'r') as f:
        lines = f.readlines()

        categories = {}
        for line in lines:
            l = line.split(';')
            categories[l[0]] = l[1]

        for card in similars:
            if card in categories:
                return categories[card]
	

if __name__ == '__main__':
    import sys
    card_name = sys.argv[1]
    print(get_card_category(card_name))
