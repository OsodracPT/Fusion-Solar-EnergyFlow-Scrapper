#! /bin/bash    
cd /home/pi/Fusion-Solar-EnergyFlow-Scrapper
source ./env/bin/activate

# virtualenv is now active, which means your PATH has been modified.
# Don't try to run python from /usr/bin/python, just run "python" and
# let the PATH figure out which version to run (based on what your
# virtualenv has configured).

python screenshot.py && cp painel.png /srv/dev-disk-by-uuid-2ad6968b-221f-40b7-920f-7cf58a149d6f/Config/homeassistant