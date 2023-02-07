import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

print("Output:")
print(result.stdout)
print("Return Code:", result.returncode)