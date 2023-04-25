# Display QR Codes
Sometimes you need to generate a QR code on your node, for whatever reason. This simple tool create any QR code you want on your node and displays it on your local network. It can be exposed via tor too if need be for remote access.

## Installation 
Installation instructions for Ubuntu based nodes. Clone repository to your node. Run this in your terminal:

```sh
cd
git clone https://github.com/proofofjogi/anyqr.git
```

And then move into the repository directory
```sh
cd anyqr
```

Make a virtual environment and activate it. This requires python3-venv to be installed. Run
```sh
sudo apt install python3-venv
```

to install python3-venv. Next we make a virtual environment named env and activate it:

```sh
python3 -m venv env
source env/bin/activate
```

Now we can install all python dependencies:
```sh
pip install -r requirements.txt
```

## Run

To run anyqr, make sure the environment is activated. Activate if it is not and then run:
```sh
cd anyqr
source env/bin/activate
python run.py 
```
That serves up anyqr on your local node IP address.

Access it through http://127.0.0.1:4203/ on localhost or through your nodes IP address, like so:

http://192.168.0.111:4203/

You can now paste strings into the text box and generate all sorts of QR codes on our node.
