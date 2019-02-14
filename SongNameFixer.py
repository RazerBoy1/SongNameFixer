import os, re, string
from os import listdir
from os.path import isfile, join

class NameFixer:
    def __init__(self):
        self.targetFolder = "C:\\Users\\RazerBoy\\Desktop\\music"
        self.fileNames = []

    def getFileNames(self):
        return self.fileNames

    def findFileNames(self):
        self.fileNames = [f for f in listdir(self.targetFolder) if isfile(join(self.targetFolder, f))]

    def rename_youre(self, name):
        return name.replace("youre", "You're").replace("Youre", "You're")

    def remove_lines(self, name):
        return name.replace(" - ", " ").replace("- ", " ").replace(" -", " ").replace("-", " ")

    def remove_space(self, name):
        return name.replace("  ", " ").replace("   ", " ")

    def remove_lyrics(self, name):
        return name.replace("lyrics", "").replace("Lyrics", "").replace("with lyrics", "").replace("with Lyrics", "")

    def remove_exclamation_marks(self, name):
        return name.replace("!", "")

    def remove_whitespace_at_end(self, name):
        return name.rstrip()

    def remove_years(self, name):
        newName = ""
        for word in name.split():
            if not word.isdigit():
                newName += word + " "
            else:
                if int(word) < 1900:
                    newName += word + " "

        return newName

    def remove_brackets_with_everything_inside(self, name):
        return re.sub(r'\(.*\)', '', name)

    def remove_square_brackets_with_everything_inside(self, name):
        return re.sub(r'\[.*\]', '', name)

nf = NameFixer()
nf.findFileNames()

for name in nf.fileNames:
    newName = nf.rename_youre(name)
    newName = nf.remove_lines(newName)
    newName = nf.remove_space(newName)
    newName = nf.remove_years(newName)
    newName = nf.remove_lyrics(newName)
    newName = nf.remove_whitespace_at_end(newName)
    newName = nf.remove_exclamation_marks(newName)
    newName = nf.remove_brackets_with_everything_inside(newName)
    newName = nf.remove_square_brackets_with_everything_inside(newName)

    orgName = nf.targetFolder + "\\" + name
    targetName = nf.targetFolder + "\\" + string.capwords(newName.encode("ascii", errors = "ignore").decode().lstrip())

    os.rename(orgName, targetName)

    orgName = targetName
    targetName = targetName.replace("Xxxtentacion", "XXXTENTACION")

    os.rename(orgName, targetName)