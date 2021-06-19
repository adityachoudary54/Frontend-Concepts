import subprocess
a = subprocess.run(["git", 'tree'], capture_output=True)
a = a.stdout.decode('utf-8')

with open("README.md", "w+") as file:
    file.write("Will revise frontend concepts in this repo\n")
    file.write("```")
    file.write(a)
    file.write("```")
