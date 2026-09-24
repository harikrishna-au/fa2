"""Offline setup check. Does not import student answers or invoke AWS."""
from importlib import import_module
from pathlib import Path
import ast
import sys

ROOT = Path(__file__).resolve().parent
failures = []
for module, names in [
    ("langchain_aws", ["ChatBedrockConverse"]),
    ("langchain_core.tools", ["tool"]),
    ("langgraph.graph", ["StateGraph", "START", "END"]),
    ("langgraph.checkpoint.memory", ["InMemorySaver"]),
    ("langgraph.types", ["interrupt", "Command"]),
    ("dotenv", ["load_dotenv"]),
    ("grandalf", []),
]:
    try:
        obj = import_module(module)
        for name in names:
            getattr(obj, name)
        print("OK import:", module)
    except (ImportError, AttributeError) as exc:
        failures.append(module)
        print("FAIL import:", module, "-", exc)
for filename in ["FA2_Mock_P1.py", "FA2_Mock_P2.py"]:
    path = ROOT / filename
    if not path.exists():
        print("SKIP original filename (perhaps renamed):", filename)
        continue
    try:
        ast.parse(path.read_text(encoding="utf-8"))
        print("OK syntax:", filename)
    except SyntaxError as exc:
        failures.append(filename)
        print("FAIL syntax:", filename, exc)
print("Python:", sys.version.split()[0])
print(".env present:", (ROOT / ".env").exists(), "(contents never printed)")
print("This check does not validate credentials, model access, TODOs or correctness.")
sys.exit(1 if failures else 0)
