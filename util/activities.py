import random

from discord import Activity, ActivityType

from util.generic_helpers import cycle_random

SONGS = [
    "Owl City",
    "Enemy (J.I.D. Verse Only)",
    "your thoughts",
    "NPR's Tiny Desk",
]

GAMES = [
    "dead 💀",
    "Chess ♟",
    "Wild Rift",
    "Toontown",
    f"you{random.choice([' 😏', ''])}",
    "Adventure Quest",
    "Tribal Wars",
    "Spore",
    "Endless Online",
    "Mech Warriors",
    "RuneLite",
    "Dolphin Emulator",
    "Club Penguin",
    "TFT",
    "ARAM",
]

CLIPS = [
    "Arcane: Season 2",
    "Spy Kids 3-D: Game Over",
    "Camp Rock!",
    "Twilight: Charlie's Revenge",
    f"Harry Potter Book 7 Part {random.randint(3, 20)}",
]

playing_activities = [Activity(type=ActivityType.playing, name=game) for game in GAMES]
listening_activities = [Activity(type=ActivityType.listening, name=sound) for sound in SONGS]
watching_activities = [Activity(type=ActivityType.watching, name=clip) for clip in CLIPS]

goonbot_activities = cycle_random([*playing_activities, *listening_activities, *watching_activities])
