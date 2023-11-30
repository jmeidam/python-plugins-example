# Tester for package-plugin integration: User

This folder is meant for testing the package-plugin suite as a user of the plugin (and core indirectly)

## Setup/Usage

You can use the bash scripts to setup the environment and run tests:

 - `setup_user_env.sh`: Sets up the user environment from scratch (rebuilds everything).
 - `install_plugin.sh`: Installs spiffy-plugin from its dist folder
 - `recreate_env.sh`: (re-)create the virtual environment
 - `show_spiffy_installed_content.sh`: Lists the contents of the installed spiffy package.

When the environment is set up, you can run `python test.py` (after having activated the virtual env of course) to verify that everything works as expected.
