# Functions
# The following are some of the most commonly used functions in the shutil module:
# shutil.copy(src,dst):this function copys the file location specified by dst.If the destination location already exists,the original file will be overwritten.

# shutil.copy2(src,dst):This function is similar to shutil.copy, but it also preserves more metadata about the original file,such as timestamp.

# shutil.copytree(src,dst):This function recursively copies the directoy located at scr to a new location specified by dst.If the destination location already exist, the original directory will be merged with it.

# shutil.move(src,dst):move file location

# shutil.rmtree(path):This function recursivly deleted the directory located at path,alog with all of its content.



import shutil
