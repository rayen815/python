try:
    import os
except:
    print("os library missing")
    quit()

os.chdir("C:/Users")
cwd=os.getcwd()
print(cwd)

for dic in os.listdir(cwd):
    if not(dic in ["All Users","Default","Default User","Public"]) and os.path.isdir(dic):
        user=dic
        break
user="C:/Users/"+user
os.chdir(user)

path=user+"/"+input(f"complete this path {user}/")

an=input("are you sure to start ? y/n: ")
if an=="n":
    print("ok bye")
    quit()
elif an=="y":
    os.chdir(path)
    files={"docx":[],"py":[],"html":[],"css":[],"js":[],"sql":[],"pdf":[],"img":[],"other":[],"app":[]}
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file):
            if file[file.find("."):].lower() == ".docx":
                files["docx"].append(file)
            elif file[file.find("."):].lower() == ".py":
                files["py"].append(file)
            elif file[file.find("."):].lower() == ".html":
                files["html"].append(file)
            elif file[file.find("."):].lower() == ".css":
                files["css"].append(file)
            elif file[file.find("."):].lower() == ".js":
                files["js"].append(file)
            elif file[file.find("."):].lower() == ".sql":
                files["sql"].append(file)
            elif file[file.find("."):].lower() == ".pdf":
                files["pdf"].append(file)
            elif file[file.find("."):].lower() in [".png",".jpg",".gif"]:
                files["img"].append(file)
            elif file[file.find("."):].lower() in [".exe",".lnk"]:
                files["app"].append(file)
            else:
                files["other"].append(file)

        for key in files.keys():
            os.makedirs(path+"/"+key)
            if key !="":
                for f in files[key]:
                    if f!="osclean.py":
                        os.replace(path+"/"+f,path+"/"+key+"/"+f)
                        
else:
    print("make sure to write a clear answer")
    quit()

