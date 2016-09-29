class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.people_greeted = []
        self.unique_people_greeted = 0

    def greet(self, other_person):
        self.greeting_count += 1
        if other_person not in self.people_greeted:
            self.people_greeted.append(other_person)
            self.unique_people_greeted += 1
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

    def print_contact_info(self):
        print "{0}'s email: {1}, {0}'s phone number: {2}".format(sonny.name.capitalize(),sonny.email,sonny.phone)

    def add_friend(self,other):
        return self.friends.append(other)

    def num_friends(self):
        return len(self.friends)

    def __repr__(self):
        return "{0}'s email: {1}, {0}'s phone number: {2}".format(sonny.name.capitalize(),sonny.email,sonny.phone)

    def num_unique_people_greeted(self):
        return self.unique_people_greeted


sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
jordan = Person('Jordan','jordan@aol.com','495-586-3456')
dee_ann = Person('Dee Ann','deeann@hotmail.com','704-779-8391')

# sonny.greet(jordan)
# jordan.greet(sonny)
#
# print "Sonny's Email: {0}\nSonny's Phone: {1}".format(sonny.email,sonny.phone)
# print "Jordan's Email: {0}\nJordan's Phone: {1}".format(jordan.email,jordan.phone)
# print
# sonny.print_contact_info()
# print
# print jordan.friends.append(sonny)
# sonny.friends.append(sonny)
# print len(jordan.friends)
# print
# print jordan.add_friend(sonny)
# print jordan.num_friends()
# print sonny.greeting_count
# sonny.greet(jordan)
# print sonny.greeting_count
# sonny.greet(jordan)
# print sonny.greeting_count
#
# sonny.people_greated = 0
# sonny.greet(jordan)
# print sonny.num_unique_people_greeted()
# sonny.greet(jordan)
# print sonny.num_unique_people_greeted()
# sonny.greet(dee_ann)
# print sonny.num_unique_people_greeted()
