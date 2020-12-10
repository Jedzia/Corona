#  Corona  #
Some calculations and considerations how fast you will **DIE**!

* Setup

    Assuming you're not dead you can run this contraption with a standard Python 3.8 installation and ignore the
    following virtual environment setup. This is purely for development and the further spread of this disease. 
    No medical extensions are required (yet).

    With a virtual environment you can
    add the source folder to the python search path: 

        (venv) Corona> add2virtualenv src

* Running the module

        (venv) Corona> python -m Corona.main
        
    with 
    
        usage: main.py [-h] [-s SPREADRATE] N
        
    where -h or --help show this help and
    
    -s denotes the spread rate and 
    
    and an provided integer as the main argument will possibly show you the amount of your beloved, 
    turning into dead zombies...         

## Example of devastation ##

    (venv) ➜ Corona git:(master) python -m Corona.main 5
    Your personal devastation calculator is starting up. Please wait...
    
    Range of days to calculate:  5
    data file is '/home/jedzia/Projects/Python/Corona/src/Corona/data/COVID-19.cfg'.
    section[COVID-19]:  {'name': 'Coronavirus SARS-CoV-2', 'spreadrate': '0.2'}
    Calculating Statistics for the COVID-19 Virus
    day 1:  Cole: "I can see 1,20  dead people."
    day 2:  Cole: "I can see 1,44  dead people."
    day 3:  Cole: "I can see 1,73  dead people."
    day 4:  Cole: "I can see 2,07  dead people."
    day 5:  Cole: "I can see 2,49  dead people."

## Coming soon™ ##

Pretty tables, never seen before! 