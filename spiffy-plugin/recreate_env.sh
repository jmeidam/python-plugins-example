if [ -d ".venv" ]; then
  echo "removing plugin venv"
  rm -r .venv
fi

if [ -f poetry.lock ]; then rm poetry.lock; fi

poetry env use 3.9
poetry install
