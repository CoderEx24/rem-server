# ReemServer

This repo contians the server of the virtual nurse
the server is reponsible for registering users and keeping a record of the symptoms they report
and the diagnosis given to them

The Server has 4 jobs
- Record the symptoms submitted by users
- Give a diagnosis to the submitted symptoms
- Store the submitted symptoms
- Use the submitted symptoms to try and predict pandemics

### Setup
1. Clone this repo
```
$ git clone https://github.com/CoderEx24/reem-server
```
2. Setup a virtual environment
```
$ python3 -m virtualenv .venv
$ . venv/bin/activate
(.venv) $ python3 -m pip install -r requirements
```

