relationship_type = {
    'CHILD': 'CHILD',
    'SPOUSE': 'SPOUSE',
    'PARENT': 'PARENT'
}

member_gender = {
    'Male': 'MALE',
    'Female': 'FEMALE',
    'N/A': 'N/A'
}

relationship_unit = {
    'MALE_PARENT': {
        'gender': member_gender['Male'],
        'type': relationship_type['PARENT']
    },
    'FEMALE_PARENT': {
        'gender': member_gender['Female'],
        'type': relationship_type['PARENT']
    },
    'ANY_PARENT': {
        'gender': member_gender['N/A'],
        'type': relationship_type['PARENT']
    },
    'FEMALE_CHILD': {
        'gender': member_gender['Female'],
        'type': relationship_type['CHILD']
    },
    'MALE_CHILD': {
        'gender': member_gender['Male'],
        'type': relationship_type['CHILD']
    },
    'ANY_CHILD': {
        'gender': member_gender['N/A'],
        'type': relationship_type['CHILD']
    },
    'FEMALE_SPOUSE': {
        'gender': member_gender['Female'],
        'type': relationship_type['SPOUSE']
    },
    'MALE_SPOUSE': {
        'gender': member_gender['Male'],
        'type': relationship_type['SPOUSE']
    }
}

relationship_def = {
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
    ],
    'FATHER': [
        [
            relationship_unit['MALE_PARENT']
        ]
    ]
}

valid_actions = {
    'ADD_CHILD': 'ADD_CHILD',
    'GET_RELATIONSHIP': 'GET_RELATIONSHIP'
}

output_messages = {
    'INVALID_ACTION': 'INVALID_ACTION',
    'INVALID_INPUT': 'INVALID_INPUT',
    'CHILD_ADDITION_SUCCEEDED': 'CHILD_ADDITION_SUCCEEDED',
    'PERSON_NOT_FOUND': 'PERSON_NOT_FOUND'
}
