# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file's creation and modification times)

import shutil
shutil.copyfile('text.txt', 'copy.txt') #source, destination


#shutil.copy('text.txt', 'copy2.txt')
#shutil.copy2('text.txt', 'copy2method.txt')


