direct_relationship = {
    'FATHER': 'FATHER',
    'MOTHER': 'MOTHER',
    'SON': 'SON',
    'DAUGHTER': 'DAUGHTER',
    'PARENT': 'PARENT',
    'CHILD': 'CHILD',
    'SISTER': 'SISTER',
    'BROTHER': 'BROTHER',
    'SIBLING': 'SIBLING',
    'SPOUSE': 'SPOUSE'
}

indirect_relationship = {
    'PATERNAL-AUNT': [
        [
            direct_relationship['FATHER'],
            direct_relationship['SISTER'],
        ],
    ],
    'PATERNAL-UNCLE': [
        [
            direct_relationship['FATHER'],
            direct_relationship['BROTHER']
        ]
    ],
    'MATERNAL-UNCLE': [
        [
            direct_relationship['MOTHER'],
            direct_relationship['BROTHER']
        ]
    ],
    'MATERNAL-AUNT': [
        [
            direct_relationship['MOTHER'],
            direct_relationship['SISTER']
        ]
    ],
    'SISTER-IN-LAW': [
        [
            direct_relationship['SPOUSE'],
            direct_relationship['SISTER']
        ],
        [
            direct_relationship['SIBLING'],
            direct_relationship['SPOUSE'],
        ]
    ],
    'BROTHER-IN-LAW': [
        [
            direct_relationship['SPOUSE'],
            direct_relationship['BROTHER']
        ],
        [
            direct_relationship['SIBLING'],
            direct_relationship['SPOUSE'],
        ]
    ],
}
