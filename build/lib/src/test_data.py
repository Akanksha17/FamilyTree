from .constants import member_gender, relationship_type

members_to_add = [
    {
        'name': 'King Shan',
        'gender': member_gender['MALE']
    },
    {
        'name': 'Queen Anga',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Chit',
        'gender': member_gender['MALE']
    },
    {
        'name': 'Amba',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Ish',
        'gender': member_gender['MALE']
    },
    {
        'name': 'Vich',
        'gender': member_gender['MALE']
    },
    {
        'name': 'Lika',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Satya',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Vyan',
        'gender': member_gender['MALE']
    },
    {
        'name': 'Dritha',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Jaya',
        'gender': member_gender['MALE']
    },
    {
        'name': 'Tritha',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Vritha',
        'gender': member_gender['MALE']
    }, {
        'name': 'Vila',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Chika',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Vritha',
        'gender': member_gender['MALE']
    }, {
        'name': 'Vila',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Chika',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Arit',
        'gender': member_gender['MALE']
    }, {
        'name': 'Jnki',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Ahit',
        'gender': member_gender['MALE']
    },
    {
        'name': 'Satvy',
        'gender': member_gender['FEMALE']
    }, {
        'name': 'Asva',
        'gender': member_gender['MALE']
    },
    {
        'name': 'Krpi',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Vyas',
        'gender': member_gender['MALE']
    },
    {
        'name': 'Atya',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Yodhan',
        'gender': member_gender['MALE']
    }, {
        'name': 'Laki',
        'gender': member_gender['MALE']
    }, {
        'name': 'Lavnya',
        'gender': member_gender['FEMALE']
    },
    {
        'name': 'Vasa',
        'gender': member_gender['MALE']
    },
    {
        'name': 'Kriya',
        'gender': member_gender['MALE']
    },

    {
        'name': 'Krithi',
        'gender': member_gender['FEMALE']
    },
]

relationships_to_add = [
    {
        'from': 'King Shan',
        'to': 'Queen Anga',
        'relationship': relationship_type['SPOUSE']
    },
    {
        'from': 'King Shan',
        'to': 'Chit',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'King Shan',
        'to': 'Ish',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'King Shan',
        'to': 'Vich',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'King Shan',
        'to': 'Aras',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'King Shan',
        'to': 'Satya',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Chit',
        'to': 'Amba',
        'relationship': relationship_type['SPOUSE']
    },
    {
        'from': 'Vich',
        'to': 'Lika',
        'relationship': relationship_type['SPOUSE']
    },
{
        'from': 'Aras',
        'to': 'Chitra',
        'relationship': relationship_type['SPOUSE']
    },
    {
        'from': 'Satya',
        'to': 'Vyan',
        'relationship': relationship_type['SPOUSE']
    },
    {
        'from': 'Chit',
        'to': 'Dritha',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Chit',
        'to': 'Tritha',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Chit',
        'to': 'Vritha',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Vich',
        'to': 'Vila',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Vich',
        'to': 'Chika',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Aras',
        'to': 'Jnki',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Aras',
        'to': 'Ahit',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Satya',
        'to': 'Asva',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Satya',
        'to': 'Vyas',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Satya',
        'to': 'Atya',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Dritha',
        'to': 'Jaya',
        'relationship': relationship_type['SPOUSE']
    },
    {
        'from': 'Jnki',
        'to': 'Arit',
        'relationship': relationship_type['SPOUSE']
    },
    {
        'from': 'Asva',
        'to': 'Satvy',
        'relationship': relationship_type['SPOUSE']
    },
    {
        'from': 'Vyas',
        'to': 'Krpi',
        'relationship': relationship_type['SPOUSE']
    },
    {
        'from': 'Dritha',
        'to': 'Yodhan',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Jnki',
        'to': 'Laki',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Jnki',
        'to': 'Lavnya',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Asva',
        'to': 'Vasa',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Vyas',
        'to': 'Kriya',
        'relationship': relationship_type['CHILD']
    },
    {
        'from': 'Vyas',
        'to': 'Krithi',
        'relationship': relationship_type['CHILD']
    },
]