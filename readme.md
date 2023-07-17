# Welcome To SendIpToEmail

a python script to regularly send the ip of your current machine to an email address.

## Installation:-
1- Clone/Download the repository
```rb
git clone https://github.com/MaxBadarne/sendIpToEmail.git
```
2- Navigate to the sendIpToEmail directory
```rb
cd sendIpToEmail
```
3- Install all the requirements with pip
```rb
pip install git+https://github.com/elasticemail/elasticemail-python.git
pip install -r requirements.txt
```
4- Create an ElasticMain account and Generate an API key | Follow [/Instructions/ElasticEmail_Instructions.md](Instructions/ElasticEmail_Instructions.md)

Run "setup.py" and input all the needed information
 
<sub> if no "time to wait" specified, the script will set itself to send an email every 24 hours </sub>


```rb
python3 setup.py
```

When finished, run "run.py"
```rb
python3 run.py
```

The script will send your ip regularly as long as its running.

### MISC

* Known Bugs : 
    - Sometimes an empty email will be sent, it seems to be a problem only when running the script for the first time after setting it up
* Logs will be saved locally in data/logs .
* A special Thank you to Elasticemail for their beautiful API documentation and for their amazing services.
* Feedback is always appreciated, I welcome any suggestion and or bug, if you find any problem or have a better way of writing certain parts, please feel free to make a pull request.
