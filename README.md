# Welcome to futurenet calculator!

This calculator is a python script that allows you to make calculations in the **AdPro** world.
This calculator doesn't include the matrix or futurocoin.
Note that this only works in a terminal bashed environment.


# Usage
Calculate the amount of profit in one day
```
python3 futurenet.py -m [amount]
```
Calculate the amount of profit in one day when the holiday mode is active
```
python3 futurenet.py -m [amount] -hd
```

Calculate the amount of profit in x day
```
python3 futurenet.py -m [amount] -d [days]
```

Calculate the amount of money x adpacks generate  in one day
```
python3 futurenet.py -a [adpacks] -ap
```

Calculate the amount of days it takes to generate one adpack
```
python3 futurenet.py -a [adpacks] -e
```

Calculate the amount of adpacks needed to achieve x amount of profit
```
python3 futurenet.py -tp [profit]
```

Calculate total revenue from x days
```
python3 futurenet.py -c [revenue 1] [revenue 2] [revenue 3] ... [revenue n] -cp
```

Calculate amount of adpack in x days (reinvesting)
```
python3 futurenet.py -D [YYYY-MM-DD] -a [adpacks] -b [balance] -r -pb -pa
```

Calculate amount of balance in x days
```
python3 futurenet.py -D [YYYY-MM-DD] -a [adpacks] -b [balance] -pb -pa
```

Calculate profit your friends have given you listed in a file
```
python3 futurenet.py -f [file]
```
Calculate profit your friends have given you listed in a file and append new information:
```
python3 futurenet.py -f [file] -fe [Winst1] [Winst2] [Winst3] ... [WinstN]
```
Calculate profit your earned daily in a file while holiday mode is active and append new information :
```
python3 futurenet.py -f [file] -de [Winst1] [Winst2] [Winst3] ... [WinstN] -hd
```

# How to install
1 - First you will have to install python (either 2.7 or 3.x will work)
follow the instructions for your OS

2 - clone this repo and execute fn.py with python like this if you are using python3
```
python3 fn.py -h
```
or if you are using python 2.7
```
python fn.py -h
```

