import csv
import subprocess

def createCatastropheCard(name, biome, population, traits, text, image, disaster, virus):
    code = "\\begin{tikzpicture} \n"
    code += "\cardborder{} \n"
    code += "\cardcata{" + disaster + "}{" + virus + "} \n"
    code += "\cardextra{" + population + "}{" + traits + "} \n"
    code += "\cardinfo{" + name + "}{" + image + "} \n"
    code += "\cardbiome{" + biome + "} \n"
    if text != "":
        code += "\cardcontent{" + text + "} \n"
    code += "\end{tikzpicture}\n\\newpage\n"
    #code += "\end{tikzpicture}\n\hspace{-4mm}\n"
    return code

def processCards(fileName = "cdList2.csv"):
    f = open("cards.txt", "w")
    baseFile = "ZXcList2"
    texFile = baseFile + ".tex"
    pdfFile = baseFile + ".pdf"
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
    f.close()
    compileFile(texFile)
    subprocess.Popen([pdfFile],shell=True)
    return

def compileFile(fileName):
    proc=subprocess.Popen(['pdflatex',fileName])
    proc.communicate()

processCards()
