 * Installation of geth by building from source code
 ```sh
 go get -d github.com/ethereum/go-ethereum
 go install github.com/ethereum/go-ethereum/cmd/geth
 ```
 
 * Install pip if it is not available:
 ```sh
$ which pip || curl https://bootstrap.pypa.io/get-pip.py | python
```
 * Install virtualenv if it is not available:
 ```sh
 which virtualenv || pip install --upgrade virtualenv
```
* If the above command displays an error, you can try installing as root:
```sh
$ sudo pip install virtualenv
```

* Create a virtual environment:
```sh
$ virtualenv -p python3 ~/.venv-py3
```

* Activate your new virtual environment:
```sh
$ source ~/.venv-py3/bin/activate
```

* With virtualenv active, make sure you have the latest packaging tools
```sh
$ pip install --upgrade pip setuptools
```

* Now we can install web3.py...
```sh
$ pip install --upgrade web3
```

* Enable the geth launchpad repository
```sh
$ sudo add-apt-repository -y ppa:ethereum/ethereum
```

* Install go-ethereum
```sh
$ sudo apt-get update
$ sudo apt-get install ethereum
```

* Run the client in fast-sync mode
```sh
$geth --syncmode "fast"
```

* As you run the client there will be an opening of IPC endpoint, note that and use it to connect to a terminal using Javascript API as:
```sh
$geth attach /home/<username>/.ethereum/geth.ipc
$txpool.content
```
