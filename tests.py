from classes import Course, copy_course, Change, AddressBuilder

if __name__ == '__main__':
    _course = Course(language='english', level='A1', price='200',
                     teachers=['Anna'], students=['Ivan', 'Pety', 'Maria'],
                     address='Munich', books='LLoL')
    copy_cour = copy_course(_course)
    print(copy_cour)
    change_cour = Change(copy_cour, level='A2', price='400')
    cour = change_cour.change_data()
    print(cour)

    addr = AddressBuilder().set_city('Paris').\
        set_street('Tred').set_country('Germany').build()
    print(addr)
