class AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address('121 Admin Rd.', 'Concord', 'NH', '03301'),
            # 2: Address('121 Admin Rd.', 'Concord', 'NH', '03301'),
            # 3: Address('121 Admin Rd.', 'Concord', 'NH', '03301'),
            # 4: Address('121 Admin Rd.', 'Concord', 'NH', '03301'),
            # 5: Address('121 Admin Rd.', 'Concord', 'NH', '03301')
        }

    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address

class Address:
    def __init__(self, street, city, state, zipcode, street2 = ''):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.street2 = street2

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state}, {self.zipcode}')
        return '\n'.join(lines)