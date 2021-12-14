import parsing
from email_sender import SecretSantaSender
import argparse

if __name__ == '__main__':

    argparser = argparse.ArgumentParser(description="Send randomized Secret Santa emails.")
    argparser.add_argument("email", type=str, help="Mail to use for Santa Claus.")
    argparser.add_argument("pwd", type=str, help="Password to use for Santa Claus' email.")
    argparser.add_argument("--stmp-server", type=str,
                           default="stmp.gmail.com",
                           help="Stmp server to connect to for Santa's email. Use gmail by default.")
    argparser.add_argument("--max-expense", type=int, default=10,
                           help="Specifies the maximum expendable money for each present.")
    argparser.add_argument("--email-object", type=str, default="Secret Santa",
                           help="Defines the object to use for the emails.")
    argparser.add_argument("--participants-file", type=str, default="santas_secret_list.csv",
                           help="Specifies the path to the .csv file that contains the list of who participates.")
    argparser.add_argument("--csv-sep", type=str, default=",", help="Set the .csv file separator.")
    argparser.add_argument("--likes-sep", type=str, default=";", help="Set the 'likes' list separator in the .csv file.")
    argparser.add_argument("--no-card", action="store_true",
                           help="Tells the script to avoid sending xmas cards attachments.")

    args = argparser.parse_args()

    parser = parsing.CSVParser(args.participants_file, sep=args.csv_sep)
    couplings = parser.get_random_couplings()
    sender = SecretSantaSender(args.email, args.pwd)
    for coupling in couplings:
        attachments = []
        if not args.no_card:
            xmas_card = "./media/xmas_card_" + coupling[1].name.lower() + ".pdf"
            attachments.append(xmas_card)
        sender.send_to(coupling[0], coupling[1], likes_sep=args.likes_sep,
                       attachments_paths=attachments, email_object=args.email_object)
        # print(coupling[0].name, "=>", coupling[1].name)
    print("Done! This Christmas will once again be Merry!")

