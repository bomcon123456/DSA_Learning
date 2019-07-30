"""
    Class:
        - Book:
            Fields:
                Author <---- Person
                Date
                Descriptions
                Pages
                Rating
                Type
                IsBought
                Related Books: [Book]
                Source: (Can be file or links)
            Methods:
                Accessors
                Mutators
                get_previewContent()
        - Book List:
            Fields:
                [Book]
            Methods:
                Accessors
                Mutators
                some convinient methods like: sort(), filter(), suggest(),...
        - Configurator:
            Fields:
                Name
                Purpose
            Method:
                start()
        - BookConfigurator <--- Configurators
        - UserConfigurator <--- Configurators
        - Book Manager:
            Fields:
                BookList
                ConfigSettings = [BookConfigurator]
                Type: enum("ONLINE", "LOCAL")
            Methods:
                init()
                scheduleWork()
        - Person:
            Fields:
                Name
                DoB
                Descriptions
                some more personal stuff
        - Author <--- Person
            Fields:
                Books: BookList
        - User <--- Person
            Fields:
                Email
                Password
                ....
                UserConfigs: [UserConfigurator]
                BookPurchased: BookList
                FavBooks: BookList
                Wishlist: BookList
                Payment: Payment
        - ....
"""
