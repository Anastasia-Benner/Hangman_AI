import game

def main():
    g = game.Game('test')

    print(g)

    while (g.alive and not g.win):
        g.process_guess(input('Enter a letter: '))
        print(g)

    if (g.win):
        print('\vYOU WIN!')
    else:
        print('\vYOU LOSE!')


if __name__ == '__main__':
    main()
