ROLES_WOLF_PACK= [
    {
        'name': 'Alpha Wolf',
        'faction': 'Wolf Pack',
        'emoji': '🐺',
        'corrupted': True,
    },
    {
        'name': 'Pack Wolf',
        'faction': 'Wolf Pack',
        'emoji': '🐺',
        'corrupted': True,
    },

    {
        'name': 'Wolf Pup',
        'faction': 'Wolf Pack',
        'emoji': '🐺🐕',
        'corrupted': True,
    },
    {
        'name': 'Defector',
        'faction': 'Wolf Pack',
        'emoji': '🔄',
    },
]

ROLES_VILLAGE = [
    {
        'name': 'Farmer',
        'secret_role': 'Hero Farmer',
        'faction': 'Village',
        'emoji': '🧑‍🌾',
        'secret_emoji': '💪🧑‍🌾',
    },
    {
        'name': 'Farmer',
        'secret_role': 'Wolf Farmer',
        'faction': 'Village',
        'emoji': '🧑‍🌾',
        'secret_emoji': '🐺🧑‍🌾',
    },
    {
        'name': 'Clairvoyant',
        'faction': 'Village',
        'mystic': True,
        'emoji': '🔮',
    },
    {
        'name': 'Witch',
        'faction': 'Village',
        'mystic': True,
        'emoji': '🧙‍♀️',
    },
    {
        'name': 'Medium',
        'faction': 'Village',
        'mystic': True,
        'emoji': '👻',
    },
    {
        'name': 'Healer',
        'faction': 'Village',
        'mystic': True,
        'emoji': '💖',
    },
    {
        'name': 'Bard',
        'faction': 'Village',
        'emoji': '🎤',
    },
    {
        'name': 'Innkeeper',
        'faction': 'Village',
        'emoji': '🍻',
    },
    {
        'name': 'Hermit',
        'faction': 'Village',
        'emoji': '🏠',
    },
    {
        'name': 'Monk',
        'faction': 'Village',
        'emoji': '🙏',
    },
    {
        'name': 'Priest',
        'faction': 'Village',
        'emoji': '✝️',
    },
    {
        'name': 'Sinner ',
        'faction': 'Village',
        'corrupted': True,
        'emoji': '😈',
    },
    {
        'name': 'Seducer',
        'faction': 'Village',
        'corrupted': True,
        'emoji': '💋',
    },
    {
        'name': 'Madman',
        'faction': 'Third Party',
        'emoji': '🌀',
    },
    {
        'name': 'Jester',
        'faction': 'Third Party',
        'emoji': '🎭',
    },
]

ROLES = ROLES_WOLF_PACK + ROLES_VILLAGE

def roles_to_verbose(roles):
    verbose_lines = ''
    for role in roles:
        verbose_lines.append(
            f'{role["name"]} {role["emoji"]} ({role["faction"]}) {"🖤" if role.get("corrupted") else ""} {"✨" if role.get("mystic") else ""}'
        )
    return '\n'.join(verbose_lines)