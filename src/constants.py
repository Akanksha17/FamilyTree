relationship_type = {
    'CHILD': 'CHILD',
    'SPOUSE': 'SPOUSE'
}

member_gender = {
    'MALE': 'MALE',
    'FEMALE': 'FEMALE',
    'N/A': 'N/A'
}

relationship_unit = {
    'MALE_PARENT': {
        'gender': member_gender['MALE'],
        'type': relationship_type['PARENT']
    },
    'ANY_PARENT': {
            'gender': member_gender['N/A'],
            'type': relationship_type['PARENT']
        },
    'FEMALE_CHILD': {
            'gender': member_gender['FEMALE'],
            'type': relationship_type['CHILD']
        },
    'MALE_CHILD': {
            'gender': member_gender['MALE'],
            'type': relationship_type['CHILD']
        },
    'FEMALE_SPOUSE': {
        'gender': member_gender['FEMALE'],
        'type': relationship_type['SPOUSE']
    }
}

relationship_def_backtrace = {
    'PATERNAL-AUNT': [
        [
            relationship_unit['MALE_PARENT'],
            relationship_unit['ANY_PARENT'],
            relationship_unit['FEMALE_CHILD']
        ],
        [
            relationship_unit['MALE_PARENT'],
            relationship_unit['ANY_PARENT'],
            relationship_unit['MALE_CHILD'],
            relationship_unit['FEMALE_SPOUSE']
        ]
    ]
}