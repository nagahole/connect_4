import pygame

from src import game


def run() -> None:

    pygame.init()
    running = True

    game.init(None)

    while running:
        events = pygame.event.get()

        for event in events:  # X on window
            if event.type == pygame.QUIT:
                running = False

        game.tick(events)
        game.render()

        pygame.display.flip()  # renders drawn figures to screen

    pygame.quit()


if __name__ == "__main__":
    run()
