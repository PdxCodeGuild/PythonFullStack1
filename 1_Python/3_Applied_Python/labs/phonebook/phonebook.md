# Lab: Phonebook

##### Delivery Method: Prompt and Demo

------------------------------


#### Goal

Write a python command line interfaced phonebook to store contact data.

-------------------------------

#### Instructions


Make a command line interface phonebook that supports the following options:

__C.R.U.D.__

1. Create New Contact
2. Retrieve Contact
3. Update Existing Contact
4. Delete Contact



Here is an example of contact data being stored with a nickname key as a __dictionary of dictionaries__:

```python
phonebook = {'Kieran': {'name': 'Kieran',
                        'number': 8456331959,
                        'phrase': 'Good code is not written, it\'s re-written.'},
            'Lambda': {'name': 'Lambda',
                         'number': 8454185633,
                         'phrase': 'I am a robot.'}}
```
Here is another implementation; A __list of dictionaries__:

```python
phonebook = [{'name': 'Kieran',
            'number':8456331959,
            'phrase': 'Good code is not written, it\'s re-written.'},
            {'name': 'Lambda',
             'number':8454185633,
             'phrase': 'I am a robot.'}]
```

Or perhaps a __List of lists__:

```python
phonebook = [['Kieran',
              8456331959,
              'Good code is not written, it\'s re-written.'],
              ['Lambda',
               8454185633,
               'I am a robot.']]
```


#### Advanced

Support searching by:

 - Partial Name
 - Phone Number
 - Partial Phrase

 If there are multiple results, display each of them.


#### Super Advanced

- Add Save and Load features for your contact data by saving a csv file.

- Using the python CSV Module's CSVDictReader, download your google contacts and add them to your phonebook on startup


#### Future...?

Use the Twilio API to send a text message from your program.



-------------------------------

#### Documentation


1. [Python Official Docs: Operators](https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions)

------------------

#### Key Concepts

- Dictionaries
- CRUD
- Common Dictionary Operations


