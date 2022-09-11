import random

from discord import Activity, ActivityType

from util.generic_helpers import cycle_random

SONGS = [
    "Owl City",
    "Enemy (J.I.D. Verse Only)",
    "your thoughts",
    "Dunkin Darius (10H Loop)",
]

GAMES = [
    "dead",
    "chess",
    "wild rift",
    "toontown",
    "you",
    "adventure quest",
    "tribal wars",
    "Spore",
    "Endless Online",
]

CLIPS = [
    "Arcane: Season 2",
    "Camp Rock!",
    f"Harry Potter Book 7 Part {random.randint(1, 100)}",
]

playing_activities = [Activity(type=ActivityType.playing, name=game) for game in GAMES]
listening_activities = [Activity(type=ActivityType.listening, name=sound) for sound in SONGS]
watching_activities = [Activity(type=ActivityType.watching, name=clip) for clip in CLIPS]

goonbot_activities = cycle_random([*playing_activities, *listening_activities, *watching_activities])
