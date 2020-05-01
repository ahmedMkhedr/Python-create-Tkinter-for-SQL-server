
#Mohamed Khedr, Ahmed

#MySQL client program
#v1.0.3 -2018-11-11
#compatible with Python versions 3.4 -3.7
#source file: a3-ahmed-and-enning.py
#

from tkinter import *

      
def Tkinter():
    '''
        None -> None
        This fuction is to create a TK window with adjusted label, text entry box
        and click_ok button. When end-user type SQL comments in the entry-box and
        click ok button. the entry is saved in textentry variable,which is a global
        variable will can be used cross-function.It enables us to write the title of the
        screen and control the size of the tkinter box. 
        >>> Tkinter()
        Display a TK window 
        '''
    global textentry
    global window
    window=Tk()
    window.title("Gorrilla Database")
    window.configure(background="black")
    
    Label(window, text="Please enter the database section you would like:",\
    bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)
    entry_text= StringVar()
    textentry= Entry(window, width=60, bg="white", textvariable=entry_text)
    textentry.grid(row=2, column=0, sticky=W)
    Button(window, text="OK", width=6, command=ok_click).grid(row=3, column=0, sticky=W)

    window.mainloop()


def ok_click():
    '''
    None -> None 
    This fuction is used to create a gloabl varaible query_store to store the sql comment from global vaiable textentry.
    the get function enables us to get write the query we need to retreive in the box. the destroy function helps
    is ending the tkinter box once we click ok so that the table and rows of the quory requested is show in the python shell.
    >>>ok_click
    SQl comment is stored in global variable query_store'''
    global query_store
    query_store = textentry.get()
    print(query_store)
    window.destroy()


import mysql.connector

def connect_to_db():
    '''
        (None) -> list
        This fuction enable python to connect with mysql database, and then retrive
        data. it also creates two lists including results_list which put all the data
        in the query in a new list. the database contains multiple tables the user can choose from
        for example a gene is a table in the database.
        and rows_list to organize data.
        >>>connect_to_db()
        Return:
            List: rows_list from mysql database. 
        
        '''
    results_list= []
    rows_list= []
    cnx  =  mysql.connector.connect( host='ensembldb.ensembl.org',
                                 user='anonymous', password='',
                                 database='gorilla_gorilla_core_52_1')
    cursor = cnx.cursor()
    query = query_store
    cursor.execute( query )

    for row in cursor:
        results_list.append(row)
        
    for i in results_list:
        rows_list.append(list(i))  

    cursor.close()
    cnx.close()
    return rows_list

def data_from_database(data):
    '''
    list -> None
    This function is used to print the results of data to tell the end-user about the total rows and columns in query
    and the type of each data.
    
    >>>data_from_database(rows_list)
    the total rows in the query is: 21182
    the total number of column is: 14
    the type of data are:
    <class 'int'>
    <class 'str'>
    <class 'NoneType'>
    <class 'int'>
    ...
    ...
    '''
    print(" the total rows in the query is: " ,len(data))
    for o in range(len(data)):
        number_of_column= len(data[o])
        
    print( " the total number of column is: ",number_of_column)
    print("the type of data are: ")
    for s in data[0]:
        print(type(s))
        
def get_10_rows(rows_string):
    '''
        list -> string
        This function is used to print the top 10 rows in selected table from database and if the table contains less than 10 rows
        it prints all the rows presneted 
        >>>get_10_rows(row_list)
        [1, 'protein_coding', 34, 1977660, 249, 3625, 1, None, 'ensemb1', 'NOVEL', None, 1, 1, None]

        [2, 'protein_coding', 34, 1983781, 25318, 299379, 1, 209026. 'ensembl', 'KNOWN_BY_PROJECTION', 'RUN and FYVE domain-conraining protein 4 [Source:UniprotKB/Swiss-Prot;Acct:Q6ZNE9]', 1, 1, None]

        ...
        ...
        '''
    counter = 0
    if len(rows_string) > 10:
        while counter < 10:
            print(rows_string[counter])
            print('\n')

            counter+= 1
    elif len(rows_string) < 10:
        for i in range(len(rows_string)):
            print(rows_string[i])
            print('\n')

if __name__ == "__main__":
    while True:
        Tkinter()
        try:
            rows_list= connect_to_db()
            data_from_database(rows_list)
            get_10_rows(rows_list)
        except:
            print("Sorry we can't find it try something else")
     


