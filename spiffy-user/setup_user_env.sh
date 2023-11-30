curdir="$(pwd)"
if [[ "$(basename $curdir)" == "spiffy-user" ]]; then
  if [ -n "${VIRTUAL_ENV}" ]; then
    echo "deactivating user venv"
    deactivate
  fi

  echo " -------- rebuilding core -------- "
  cd ../spiffy-core || return
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
  . ./recreate_env.sh
  . ./install_plugin.sh

else
  echo "Must be executed from spiffy-user dir"
fi
