"""Cat Parade"""
def process_cats(input_lines):
    """process cat"""
    cats = {}
    all_cats = []
    for line in input_lines:
        if line == "IT'S A DOG":
            if all_cats:
                last_cat = all_cats.pop()
                if cats[last_cat][1] == 1:
                    del cats[last_cat]
                else:
                    cats[last_cat][1] -= 1
        else:
            breeds = line.split(", ")
            for breed in breeds:
                all_cats.append(breed)
                if breed not in cats:
                    cats[breed] = [len(all_cats), 1]
                else:
                    cats[breed][1] += 1
    return cats

def print_results(cats):
    """print result"""
    for breed in sorted(cats.keys()):
        print(f"{breed} {cats[breed][0]} {cats[breed][1]}")

def main():
    """main"""
    input_lines = []
    while True:
        line = input().strip()
        if line == "END":
            break
        input_lines.append(line)
    cats = process_cats(input_lines)
    print_results(cats)
main()
