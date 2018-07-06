import csv
import subprocess

def createTraitCard(name, costR, costB, costY, cataColor, text, image, cataColor2):
    code = "\\begin{tikzpicture} \n"
    code += "\cardborder{} \n"
    code += "\cardcost{" + costR + "}{" + costB + "}{" + costY + "} \n"
    if cataColor != "" or cataColor2 != "":
        code += "\cardcatacolor{" + cataColor + "}{" + cataColor2 + "} \n"
    code += "\cardinfo{" + name + "}{" + image + "} \n"
    if text != "":
        code += "\cardcontent{" + text + "} \n"
    code += "\end{tikzpicture}\n\\newpage\n"
    #code += "\end{tikzpicture}\n\hspace{-4mm}\n"
    return code

def processCards(fileName = "cdList.csv"):
    baseFile = "ZXcList"
    texFile = baseFile + ".tex"
    pdfFile = baseFile + ".pdf"
    f = open("cards.txt", "w")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            costR = row['Cost Red']
            costB = row['Cost Blue']
            costY = row['Cost Yellow']
            cataColor = row['Catastrophe Color']
            cataColor2 = row['Catastrophe Color2']
            text = row['Description']
            image = row['Image'].lower()
            if row['Card Status'] == "":
                continue
            card = createTraitCard(name, costR, costB, costY, cataColor, text, image, cataColor2)
            number = row['Supply']
            f.write(card*int(number))
    #f.write("\end{center}\n\end{document}")
    f.close()
    compileFile(texFile)
    subprocess.Popen([pdfFile],shell=True)
    return

def makeHeader():
    header = "\\documentclass{article}\n\\nonstopmode\n\input{libs.tex}"
    header += "\n\\usepackage{ifthen}"
    header += "\n\input{colors.tex}\n\input{Commands.tex}"
    header += "\n\\begin{document}\n\\begin{center}"
    return header

def compileFile(fileName):
    proc=subprocess.Popen(['pdflatex',fileName])
    proc.communicate()

processCards()
