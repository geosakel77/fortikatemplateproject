# Project : hellofortika

from hellofortika.classes.hellofortika import HelloFortika
from hellofortika.lib.libhellofortika import print_hello_world


def run():
    hf = HelloFortika()
    hf.print_fortika()
    print_hello_world()


if __name__ == "__main__":
    run()
