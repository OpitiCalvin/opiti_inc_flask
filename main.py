#!/usr/bin/env python3
import os
from opiti_inc import db, create_app
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand
# import uuid

if 'OPITI_INC_ENV' in os.environ:
    config_name = os.environ.get("OPITI_INC_ENV")
else:
    print("Unable to find the 'OPITI_INC_ENV' variable. Starting APP with 'development config settings'")
    config_name = 'development'

app = create_app(config_name)
migrate = Migrate(app,db, compare_type=True)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(host='0.0.0.0', port=3000, threaded=True))

if __name__ == '__main__':
    manager.run()
