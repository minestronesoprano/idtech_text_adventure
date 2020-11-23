alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# message = "wpau iwt ephhldgs udg iwt uxghi rajt xh tctgvxots"
# message = "ifz!cptt!j!xbt!bcmf!up!hfu!bddftt!up!tpnf!qfstpobm!jogpsnbujpo!gps!uif!ubshfut!zpv!tqfdjgjfe/!up!hfu!ju!zpv!kvtu!ibwf!up!tfoe!bo!fnbjm!up!dszqujdsftqpotftAhnbjm/dpn!nblf!tvsf!uif!tvckfdu!jt!fofshjafe/"
# message = "Rah_cXRaTb_^]bTb@V\\PX[.R^\\"
message = "hi baby chuddles"


def decode(new_message):
    # Try every key value
    for key in range(len(alphabet)):
        new_alphabet = alphabet[key:] + alphabet[:key]
        attempt = ""

        for i in range(len(new_message)):
            index = alphabet.find(new_message[i])

            if index < 0:
                attempt += new_message[i]
            else:
                attempt += new_alphabet[index]

        print("Key: " + str(key) + " - " + attempt)


decode(message)