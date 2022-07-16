# Display QR Codes
A simple tool to create any QR code offline on your node own node.

## Installation
First, clone repository to your node. Run this in your terminal:

```sh
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
