import os;

print(os.getcwd());
print(os.listdir(os.getcwd()));

str = os.getcwd().split("\\")
str.pop();
# print('\\'.join(str));

newDir = '\\'.join(str);
# os.chdir(newDir);
newFolder = input("Enter the new Directory name:\n");
os.mkdir(newDir+"\\" + newFolder);