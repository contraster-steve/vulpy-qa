#wrapper.py

#from contrast.wsgi import ContrastMiddleware
from contrast.flask import ContrastMiddleware # Vulpy uses Flask instead of pure wsgi

main_module_name = 'vulpy.app'
main_function_name = 'main'

main_module = importlib.import_module(main_module_name)
main_func = getattr(main_module, main_function_name)

app.wsgi_app = ContrastMiddleware(main_func())
