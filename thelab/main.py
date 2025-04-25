from modules.iopy import readlib, wrtsum, gensum

library=readlib(r"C:\dev\LearningPython\thelab\data\library.json")
wrtsum(library)
gensum(library)

