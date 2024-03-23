# models.py
from printing_functions import print_models, show_completed_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)  # Передача копії списку, щоб уникнути зміни оригінального списку.
show_completed_models(completed_models)
