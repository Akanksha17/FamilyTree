relationship_type = {
    'CHILD': 'CHILD',
    'SPOUSE': 'SPOUSE',
    'PARENT': 'PARENT'
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
    'FEMALE_PARENT': {
        'gender': member_gender['FEMALE'],
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
    'ANY_CHILD': {
        'gender': member_gender['N/A'],
        'type': relationship_type['CHILD']
    },
    'FEMALE_SPOUSE': {
        'gender': member_gender['FEMALE'],
        'type': relationship_type['SPOUSE']
    },
    'MALE_SPOUSE': {
        'gender': member_gender['MALE'],
        'type': relationship_type['SPOUSE']
    }
}

valid_actions = {
    'ADD_CHILD': 'ADD_CHILD',
    'GET_RELATIONSHIP': 'GET_RELATIONSHIP',
    'ADD_SPOUSE': 'ADD_SPOUSE',
}

output_messages = {
    'INVALID_ACTION': 'INVALID_ACTION',
    'INVALID_INPUT': 'INVALID_INPUT',
    'CHILD_ADDITION_SUCCEEDED': 'CHILD_ADDITION_SUCCEEDED',
    'PERSON_NOT_FOUND': 'PERSON_NOT_FOUND',
    'INVALID_NUMBER_OF_ARGS': 'INVALID_NUMBER_OF_ARGS',
    'INVALID_GENDER': 'INVALID_GENDER',
    'INVALID_RELATIONSHIP_TYPE': 'INVALID_RELATIONSHIP_TYPE',
    'CHILD_ADDITION_FAILED': 'CHILD_ADDITION_FAILED',
    'RELATIONSHIP_UNSUPPORTED': 'RELATIONSHIP_UNSUPPORTED',
    'SUCCESS': 'SUCCESS',
    'SPOUSE_ADDITION_SUCCEEDED': 'SPOUSE_ADDITION_SUCCEEDED'
}
