#wrapper.py

from contrast.wsgi import ContrastMiddleware

main_module_name = 'vulpy.app'
main_function_name = 'main'

main_module = importlib.import_module(main_module_name)
main_func = getattr(main_module, main_function_name)

app = ContrastMiddleware(main_func())