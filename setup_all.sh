# (re-)Install core, plugin and user projects from the ground up

if [[ -d "spiffy-core" ]]; then
  if [ -n "${VIRTUAL_ENV}" ]; then
    echo "deactivating user venv"
    deactivate
  fi

  echo " -------- rebuilding core -------- "
  cd spiffy-core || return
  pwd
  . ./recreate_env.sh
  . ./rebuild.sh

  echo " -------- rebuilding plugin -------- "
  cd ../spiffy-plugin || return
  pwd
  . ./recreate_env.sh
  . ./rebuild.sh

  echo " -------- rebuilding user -------- "
  cd ../spiffy-user || return
  pwd
  . ./setup_env.sh
  . ./install_stuff.sh
  deactivate

  cd .. || return

else
  echo "Must be executed from spiffy-user dir"
fi
