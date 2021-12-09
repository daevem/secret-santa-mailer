#Secret Santa Mailer

Simple python program to send Secret Santa participation emails and bring Christmas magic in people's hearts.

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