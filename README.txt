Python 3.9.5

To run forms_search.py:

- cd into the directory of the file and run forms_search.py interactively by entering 

    ''' 

    python -i forms_search.py 
    
    '''
- Use search_irs_forms(), which takes in a list of strings as a parameter 
- Either save the function, with a list of strings as an argument, to a variable and print the variable, for example: 

    ''' 

    results = search_irs_forms(['Form W-2', 'Form 1095-C'])

    print(results)

    '''

or print the function with the argument, such as:

    ''' 
    
    print(search_irs_forms(['Form W-2', 'Form 1095-C']))

    '''
- forms_search.py will output the results in JSON by printing the json.dumps of the function 


To run forms_download.py:

- cd into the directory of the file and run forms_download.py interactively by entering 

    ''' 

    python -i forms_download.py 
    
    '''
- Use download_forms(), which takes in three parameters ('string', number, number)
- The first parameter should be the form name, the second parameter is the initial year of the range, and the third parameter is the last year of the range 
- It should look as follows:

    '''

    download_forms('Form W-2', 2018, 2020)

    '''

- The console will print the file name once it is downloaded, if the year requested was not found it will print 'Not Available'