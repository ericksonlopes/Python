import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

print("Saída:")
print(result.stdout)
print("Código de retorno:", result.returncode)