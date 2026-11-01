"""
Runs during docker build in order to pre-download additional
data files to ensure they are available at runtime.
"""
from ram_api.load_models import load_ram_plus

load_ram_plus(384)

print("initialization complete")
