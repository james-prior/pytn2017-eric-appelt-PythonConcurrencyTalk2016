"""
This module is a naive threaded version of
animals.py in which the animated printing
is not properly synchronized.
"""
from threading import Thread

import requests

from radprint import radprint


def speak(animal):
    """
    Retrieves the sound for the given animal,
    and prints it with animation.
    """
    session = requests.Session()
    response = session.get(
        'https://ericappelt.com/animals/{0}'.format(animal)
    )
    sound = response.text
    radprint('The {0} says "{1}".'.format(animal, sound))
    session.close()

def main():
    """
    Retrieve and print sounds for all animals.
    """
    animals = ['cow', 'pig', 'chicken']
    threads = []
    for animal in animals:
        worker = Thread(target=speak, args=(animal,))
        threads.append(worker)
        worker.start()

    for worker in threads:
        worker.join()


if __name__ == '__main__':
    main()
