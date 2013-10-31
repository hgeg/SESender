SESender
========

An Amazon SES bulk mail sender

Usage
---------

You can send emails on terminal by typing:

    python sesender.py <list_file> <mail_file>

**list_file:** A text file containing list of emails seperated by new line.

**mail_file:** This is also a text file containing subject and mail body with such form:


    important!!!
     
    this is an important message!


Resulting email will have `important!!!` as subject field and `this is an important message!` as the mail body.

