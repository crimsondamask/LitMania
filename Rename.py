import os

dirname = '/media/crimsondamask/Lonelyblackhole/Crimsondamask/Books/workbee/Alexievich, Svetlana'

for (thisDir, subsHere, filesHere) in os.walk(dirname):
        for filename in filesHere:
            if filename.endswith('.jpg'):
                fullname = filename.replace(' ', '_')
                os.rename(filename, fullname)