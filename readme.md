### welcome to "SendIpToEmail"

a python script to regularly send the ip of your current machine to an email address.

To use you will first need to do 
```rb
git clone https://github.com/MaxBadarne/sendIpToEmail.git
```
and then navigate to the sendIpToEmail folder:
```rb
cd sendIpToEmail
```
and run those commands to install all the requirements:
```rb
pip install git+https://github.com/elasticemail/elasticemail-python.git
pip install requirements.txt -r
```
Then create an ElasticMain account and Generate an API key | Follow [/Instructions/ElasticEmail_Instructions.md](Instructions/ElasticEmail_Instructions.md)

run "setup.py" and input all the needed information.
<!-- if no "time to wait" specified, the script will set itself to send an email every 24 hours -->

```rb
python3 setup.py
```

when finished, run "run.py".
```rb
python3 run.py
```

The script will send your ip regularly as long as its running.

* Known Bugs:-
    - Sometimes an empty email will be sent, it seems to be a problem only when running the script for the first time after setting it up
* Logs will be saved locally
* I would like to thank Elasticemail for their beautiful API documentation and for their amazing services
* I would really love any sort of feedback. I welcome any suggestion and or bug, if you find any problem or have a better way of writing certain parts, please feel free to make a pull request.
