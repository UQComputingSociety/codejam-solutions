
def yelling(s):
    lowercase = 0
    for char in s:
        if char.islower():
            lowercase += 1

    percent = lowercase / len(s) if len(s) > 0 else 0

    if percent == 0:
        return "Acceptable."
    if 0 < percent < 0.15:
        return "WHAT WAS THAT?!"
    elif 0.15 <= percent < 0.25:
        return "SAY THAT AGAIN?!"
    elif 0.25 <= percent < 0.5:
        return "YELL IT LOUDER!"
    elif 0.5 <= percent < 0.65:
        return "I CAN'T HEAR YOU!!"
    elif 0.65 <= percent < 0.75:
        return "I THOUGHT I HEARD SOMETHING?!"
    else:
        return "WHY ARE YOU SO QUIET?"
