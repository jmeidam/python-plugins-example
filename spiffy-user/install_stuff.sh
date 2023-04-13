if [ -z "${VIRTUAL_ENV}" ]; then
  . .venv/bin/activate
fi
pip install spiffy-plugin  --no-index --find-links ../spiffy-plugin/dist --force-reinstall
