from src.constants import relationship_unit

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
    ],
    'SON': [
        [
            relationship_unit['MALE_CHILD'],
        ]
    ],
    'DAUGHTER': [
            [
                relationship_unit['FEMALE_CHILD'],
            ]
        ]
}