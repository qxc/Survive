import csv

def createCatastropheCard(name, biome, population, traits, text, image, disaster, virus):
    code = "\\begin{tikzpicture} \n"
    code += "\cardborder{} \n"
    code += "\cardcata{" + disaster + "}{" + virus + "} \n"
    code += "\cardextra{" + population + "}{" + traits + "} \n"
    code += "\cardinfo{" + name + "}{" + image + "} \n"
    code += "\cardbiome{" + biome + "} \n"
    if text != "":
        code += "\cardcontent{" + text + "} \n"
    code += "\end{tikzpicture}\n\hspace{-4mm}\n"
    return code

def processCards(fileName = "cList.csv"):
    f = open("cards.txt", "w")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            biome = row['Biome']
            population = row['Population']
            traits = row['Traits']
            text = row['Description']
            image = row['Image'].lower()
            disaster = row['Cost Disaster']
            virus = row['Cost Virus']
            if row['Card Status'] == "":
                continue
            card = createCatastropheCard(name, biome, population, traits, text, image, disaster, virus)
            number = row['Supply']
            f.write(card*int(number))
    return

processCards()
