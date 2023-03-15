from CRY.CRY_RSA import Cry
import argparse

parser = argparse.ArgumentParser(
    prog="Pixiv Downloader",
    description='用于下载固定UID的收藏列表',
    epilog='Phantom-sea © limited |∀` )',
)
parser.add_argument('--private', type=str,
                    dest="private", help='设置private key', default=False)
parser.add_argument('--public', type=str,
                    dest="public", help='public key', default=False)


def main(args):
    c = Cry(args.private, args.public)
    # c.create_rsa_key()
    r = c.encrypt_more("dawDAW")
    print(r)
    r = c.decrypt_more(r)
    print(r)


args = parser.parse_args()
main(args)