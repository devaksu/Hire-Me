class People:
    
    def contacting(contact):
        print(f'Phone ringing')
        return True

class Aleksi(People):
    name = 'Aleksi'
    happy = None
    open_for_work = True
    hired = False
    ideas = None

    def working(for_who=None):
        if for_who is None:
            print('Studying')
        else:
            print(f'Me working for {for_who.name}' )


class Employer(People):
    name = 'Your company'
    has_open_position = True
    happy = None
    ideas = None

    def hiring(worker):
        worker.hired = True
        worker.open_for_work = False
        Employer.happy = True
        print('🤝')

        return worker.hired, worker.open_for_work, Employer.happy

    def interested(worker):
        return True


def discuss(worker, employee):
    print('Discussing...')
    worker.ideas = True
    employee.ideas = True

    return worker.ideas, employee.ideas



