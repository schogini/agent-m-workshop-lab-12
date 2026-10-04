import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from agno.agent import Agent
from common import make_model


def get_canteen_menu(day: str) -> str:
    """Return the campus canteen menu for a day of the week."""
    menus = {
        "monday": "Breakfast: Dosa. Lunch: Rice, sambar and vegetables.",
        "tuesday": "Breakfast: Puttu and kadala. Lunch: Veg biryani.",
        "wednesday": "Breakfast: Idli and sambar. Lunch: Rice and avial.",
        "thursday": "Breakfast: Appam and veg stew. Lunch: Meals.",
        "friday": "Breakfast: Upma. Lunch: Fried rice and gobi.",
    }
    return menus.get(day.lower(), "Menu unavailable for that day.")


agent = Agent(
    model=make_model(),
    tools=[get_canteen_menu],
    instructions=[
        "Use the canteen tool when the user asks about the menu.",
        "Do not invent menu items.",
    ],
    markdown=True,
)

if __name__ == "__main__":
    agent.print_response(
        "I prefer vegetarian food. What can I eat in the canteen on Tuesday?",
        stream=True,
    )
