import subprocess

filename = 'script.py'
while True:
    """However, you should be careful with the '.wait()'"""
    p = subprocess.Popen('python '+filename, shell=True).wait()

    """#if your there is an error from running 'my_python_code_A.py', 
    the while loop will be repeated, 
    otherwise the program will break from the loop"""
    if p != 0:
        continue
    else:
        break