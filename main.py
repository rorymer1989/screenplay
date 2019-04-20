from screenplay.actor import Actor
import screenplay.interactions as interactions

if __name__ == '__main__':
  actor = Actor()
  actor.can(webdriver='chrome')

  # from interactions import click
  # actor.attempts_to(click, locator='button')
  
  actor.knows(interactions)
  actor.click(locator='button')

  # actor.bark()
