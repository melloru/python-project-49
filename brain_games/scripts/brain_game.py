#!/user/bin/env python3
# import sys
# sys.path.insert(0,'/home/eugene/project/python-project-49')
from brain_games import cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    return name


if __name__ == '__main__':
    main()
# print(sys.path[:])
