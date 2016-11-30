from app import manager
from scripts.load_data import LoadData

manager.add_command('load', LoadData)
manager.run()
