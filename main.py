import pygame
import sys
sys.dont_write_bytecode = True

from src.engine import Engine

def main():
    engine = Engine()
    engine.run()

if __name__ == "__main__":
    main()
