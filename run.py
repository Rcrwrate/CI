import sys
import argparse

parser = argparse.ArgumentParser(
    prog="Xdnmb Downloader",
    description='用于下载Xdnmb的串内容',
    epilog='Phantom-sea © limited |∀` )',
)
parser.add_argument('-c', '--cookies', type=str,
                    dest="cookie", help='设置cookie,请用冒号包裹', default=False)
parser.add_argument('-t', '--title', type=str,
                    help='此参数将在标题为无标题的时候覆盖串标题', default=False)
parser.add_argument("-ft", "--forcetitle", type=str,
                    help='用此参数强制覆盖串标题', default=False)
parser.add_argument("-d", "--download", "-i", "--id", type=int,
                    help='下载某个串，中间无视其他优化选项', default=False)
parser.add_argument("-o", "--output", type=str, nargs="?",
                    help='输出选择,可选项:epub,txt,默认全部', default=["epub", "txt"])
parser.add_argument("-uid", "--uid", type=str, help='UID', default=False)

args = parser.parse_args()


def main(args):
    print(args)


main(args)
