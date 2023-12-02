This is the completed version of ChocAn project for CS 314, team 1.
The team includes:
    Amrit Thapa 
    Anthony Casper 
    Gabriel Soto 
    Karla Martinez
    Kevin Tran
    Simon Parker 


The "requirements.txt" file is a list of the imported python modules used. The intention for this file is to simplify installing the modules by using the following command:
    $ pip install -r requirements.txt

The test_* files are the unit tests for our program. Notice that the controller programs include little to no input checking. Instead, data.py does most of the error checking for us, so it has its own unit tests.

The intended way to use our completed program is to run provider_terminal.py and manager_terminal.py.
    $ python provider_terminal.py
    and
    $ python manager_terminal.py

The structure of the database is shown below:
database
    reports
        week_1
            members
                -member1_week_1.json
            providers
                -provider1_week_1.json
            -etf.json
        week_2
    service_records
        -week_1.json
    -member_registry.json
    -provider_directory.json
    -provider_registry.json

As you use the software, you may notice changes occuring in the database folder. 
When using the provider terminal, adding visit records in the program will create a 'week_#.json' file and append service records to the appropriate week JSON file in the 'service_records' folder. 
While using the manager terminal, adding/updating/removing providers or members will change 'provider_registry.json' or 'member_registry.json', respectively. Choosing the 'End of Week' option in the manager terminal will create new files and folders in the 'reports' folder using entered data from the providers. 