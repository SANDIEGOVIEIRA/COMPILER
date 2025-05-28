# run_all_tests.py
import os
import subprocess

TEST_DIR = "testes"
SRC_FILES = [
    "teste_bool.src",
    "teste_func.src",
    "teste_not.src",
    "teste_ast.src",
    "teste_for.src",
    "teste_semantica.src",
    "teste_erro_semantica.src",
    "teste_full.src"
]

print("=== Execução automática dos testes ===\n")

# Teste especial de fluxo de tokens com lexer.py
print("🧪 Testando: fluxo de tokens com lexer.py")
try:
    subprocess.run("python lexer.py", shell=True, check=True)
except subprocess.CalledProcessError:
    print("❌ Erro ao executar lexer.py")
print("-" * 50)

# Teste especial de tokens inválidos (com src)
print("🧪 Testando: tokens inválidos com teste_lex.src")
try:
    cmd = (
        "python -c \"import lexer; "
        "data=open('testes/teste_lex.src').read(); "
        "lexer.lexer.input(data); "
        "[tok for tok in lexer.lexer]; "
        "print(lexer.lexer.invalid_tokens)\""
    )
    subprocess.run(cmd, shell=True, check=True)
except subprocess.CalledProcessError:
    print("❌ Erro ao executar teste_lex.src")
print("-" * 50)

# Demais testes com main.py
for file in SRC_FILES:
    print(f"🧪 Testando: {file}")
    path = os.path.join(TEST_DIR, file)
    try:
        subprocess.run(f"python main.py {path}", shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"❌ Erro ao executar o teste: {file}")
    print("-" * 50)

print("\n✅ Todos os testes foram executados.")
