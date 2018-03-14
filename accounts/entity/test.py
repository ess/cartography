from unittest import TestCase

import maury.accounts as accounts

class TestAccounts(TestCase):
    def test_entity_fetch(self):
        data = {
                'id' : 'someaccount'
                }

        e = accounts.Entity(data = data)

        # When the property is known, we return the associated value
        self.assertEqual(e.fetch('id'), data['id'])

        # When the property is unknown, we return None
        self.assertEqual(e.fetch('unknown_key'), None)

    def test_entity_id(self):
        data = {
                'id' : 'someaccount'
                }

        good = accounts.Entity(data = data)
        bad = accounts.Entity(data = {})

        # An entity with an id returns that id
        self.assertEqual(good.id, data['id'])

        # An entity without an id returns None
        self.assertEqual(bad.id, None)

    def test_entity_name(self):
        data = {
                'name' : 'someaccount'
                }

        good = accounts.Entity(data = data)
        bad = accounts.Entity(data = {})

        # An entity with a name returns that name
        self.assertEqual(good.name, data['name'])

        # An entity without a name returns None
        self.assertEqual(bad.name, None)

    def test_entity_emergency_contact(self):
        data = {
                'emergency_contact' : '911'
                }

        good = accounts.Entity(data = data)
        bad = accounts.Entity(data = {})

        # An entity with an emergency contact returns that contact
        self.assertEqual(good.emergency_contact, data['emergency_contact'])

        # An entity without an emergency contact returns None
        self.assertEqual(bad.emergency_contact, None)
