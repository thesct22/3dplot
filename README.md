# 3dplot
The project runs on a virtual machine on any cloud platform.
Run this on terminal of your VM: bokeh serve --num-procs=0 --port=5006 --address=0.0.0.0 --allow-websocket-origin=*  --use-xheaders --show sample.py

Go to <externl-ip-of-vm>:5006 on browser to view after running the code successfully.

To run this on a local machine, download the code and with the necerssary requirements (see below) fulfilled, and run: bokeh serve --show sample.py

Bokeh is a data visualizing library on Python which utilizes Vis.Js for data visualization on browsers.
The bokeh server is configured to receive coordinates (x,y) and temperature (t) from a Firebase Real-time Database and plot a 3D surface plot on a webpage from the interpolated data. We make use of cubic interpolation for the same.

Requires Python 3.5 or 3.6 along with the libraries in the requirements.txt
Requires Node.Js alongwith graph3d from vis.js ($ npm install vis-graph3d)

runthis.py is a simple python code to write your VM's external IP to a Firebase Real-time Database for the use in a mobile app. (https://github.com/thesct22/Air-Condition-App)
