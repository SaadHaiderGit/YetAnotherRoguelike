from typing import Optional                                 #for vars that can be set to None
import tcod.event
from actions import Action, BumpAction, EscapeAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None             #default return
        key = event.sym

        if key == tcod.event.K_UP:
            action = BumpAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = BumpAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = BumpAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = BumpAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # Key w/ no matching output was pressed (literally all non-input keys); use default return
        return action
