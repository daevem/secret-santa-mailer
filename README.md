# Secret Santa Mailer

Simple python 3 program to send Secret Santa participation emails and bring Christmas magic in people's hearts.

The program uses a `.csv` file to read participant's data and create random couplings. The file is organized in 5 
columns (name, surname, email, gender, likes). The last column can be used to give some suggestions about what the
person likes with each suggestion being separated with a `;` (This can be changed but it's important that it does not 
match the separator used to separate entries in the `.csv` file).

The emails are sent with an xmas card pdf attachment. This is done in order to have everyone use the same type of card
to maintain anonymity. Each xmas card needs to be named 
`xmas_card_{participant's name here}.pdf`. A template is provided in the `media` folder, but the creation of the actual
cards is left to the user.
This feature can be disabled by passing the `--no-card` argument to the script.

As a final note: the email text provided is written in Italian. Changing the text to another language takes little-to-no 
HTML knowledge, however, changes might have to be reflected in the `send_to` method of the `SecretSantaSender` class.


## Running It
Before running the script, make sure you have filled in the csv file as required. If you keep all the default settings, you can run the script with the following command line instruction (after navigating into the folder of the script):

```bash
python main.py <santa_email> <password-to-use>
```

This will expect to find all the relevant information about the participants in a file named `santas_secret_list.csv` and for each participant a corresponding XMas card in the `media` folder. A known bug (too-lazy-to-solve) will show up when multiple participants have the same name, because the name only is used for referencing the xmas cards. A workaround is to tweak the `.csv` file so that, e.g. Joe Doe, will have "Joe Doe" in the `name` field and "" (the empty string) in the `surname` field and name the XMas card accordingly. Gmail is the default smtp server for Santa's login credentials.

Other options include:

```bash
  --stmp-server STMP_SERVER
                        Stmp server to connect to for Santa's email. Use gmail by default.
  --max-expense MAX_EXPENSE
                        Specifies the maximum expendable money for each present.
  --email-object EMAIL_OBJECT
                        Defines the object to use for the emails.
  --participants-file PARTICIPANTS_FILE
                        Specifies the path to the .csv file that contains the list of who participates.
  --csv-sep CSV_SEP     Set the .csv file separator.
  --likes-sep LIKES_SEP
                        Set the 'likes' list separator in the .csv file.
  --no-card             Tells the script to avoid sending xmas cards attachments.
```
