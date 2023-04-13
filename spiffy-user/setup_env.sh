if [ -d ".venv" ]; then

  if [ -n "${VIRTUAL_ENV}" ]; then
    deactivate
  fi

  echo "removing user venv"
  rm -r .venv

fi

python3.9 -m venv .venv
. .venv/bin/activate
