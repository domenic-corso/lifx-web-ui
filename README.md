# lifx-web-ui
A web UI used to interact with LAN LIFX bulbs. This makes use of the awesome [lifxlan](https://github.com/mclarkk/lifxlan) library.

## Build
Install Python dependencies
```shell
pip install -r requirements.txt
```
Install Node.js dependencies
```shell
npm install
```
Build front-end
```shell
npm run build
```

## Deploy
For Windows (cmd):
```shell
set FLASK_APP=main
flask run
```
For Linux and Mac:
```shell
export FLASK_APP=main
flask run
```
