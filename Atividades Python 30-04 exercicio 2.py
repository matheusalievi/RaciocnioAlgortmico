import importlib.util

spec = importlib.util.spec_from_file_location("modulo_temp", "Atividades Python 30-04.py")
modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulo)

print(modulo.a)