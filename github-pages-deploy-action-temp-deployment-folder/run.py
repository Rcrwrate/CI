import argparse
import time
import traceback
import os
from Lib.Network import Network
from Code.Pixiv import Pixiv

parser = argparse.ArgumentParser(
    prog="Pixiv Downloader",
    description='用于下载固定UID的收藏列表',
    epilog='Phantom-sea © limited |∀` )',
)
parser.add_argument('-c', '--cookies', type=str,
                    dest="cookie", help='设置cookie', default=False)
parser.add_argument("-d", "--download", "-i", "--id", type=int,
                    help='下载某个串，中间无视其他优化选项', default=False)
parser.add_argument("-o", "--output", type=str, nargs="?",
                    help='输出选择,可选项:epub,txt,默认全部', default=["epub", "txt"])
parser.add_argument("-uid", "--uid", type=str, help='用户UID', default=False)

args = parser.parse_args()


def main(args):

    print(args)
    if args.uid is False:
        print("UID未配置!")
        return None
    if args.cookie is False:
        print("cookie未配置!")
        return None
    n = Network({"www.pixiv.net": {"ip": "210.140.92.193"}})
    P = Pixiv(PHPSESSID=args.cookie)

    if not os.path.exists("image"):
        os.mkdir("image")

    def save(url):
        url = url.replace("i.pximg.net", P.Mirror)
        with open(os.path.join("image", url.split("/")[-1]), "wb") as f:
            f.write(n.get(url).content)

    def ID(id):
        try:
            T = P.geturls_by_pid(id)
            for i in T["body"]:
                save(i["urls"]["original"])
                print(i["urls"]["original"].split("/")[-1])
        except Exception as e:
            print(traceback.format_exc())
            time.sleep(5)
            ID(id)


main(args)