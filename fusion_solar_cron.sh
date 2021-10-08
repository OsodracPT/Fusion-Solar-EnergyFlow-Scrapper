#! /bin/bash    

#Setup Crontab to execute script every 5 minutes and Output logs to a file
# (/bin/date && /bin/bash -c /home/pi/Fusion-Solar-EnergyFlow-Scrapper/fusion_solar_cron.sh) >> /home/pi/logs/fusionsolar.log 2>&1

cd /home/pi/Fusion-Solar-EnergyFlow-Scrapper
source ./env/bin/activate

# virtualenv is now active, which means your PATH has been modified.
# Don't try to run python from /usr/bin/python, just run "python" and
# let the PATH figure out which version to run (based on what your
# virtualenv has configured).

python screenshot.py && cp painel.png /home/pi/homeassistant/config/www