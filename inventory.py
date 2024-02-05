# (PRODUCT, AMOUNT, ID)

inventory = [
    # SODA
    ('Pepsi', 0),
    ('DietPepsi', 0),
    ('MUG', 0),
    ('Starry', 0),
    ('MtnDew', 0),
    ('GreenBubbly', 0),
    ('PurpleBubbly', 0),
    ('RedGatorade', 0),
    ('BlueGatorade', 0),
    ('LemonTea', 0),
    ('RaspberryTea', 0),
    ('SweetTea', 0),
    ('UnsweetTea', 0),
    ('LifeWater', 0),
    ('CherryStubborn', 0),
    ('VanillaStubborn', 0),
    ('RootBeerStubborn', 0),

    # UTENSILS
    ('Fork', 0),
    ('Knife', 0),
    ('Straw', 0),
    ('Sugar', 0),
    ('Salt', 0),
    ('Pepper', 0),
    ('SmallLid', 0),
    ('LargeLid', 0),
    ('CupHolder', 0),
    ('SmallBag', 0),
    ('LargeBag', 0),
    ('SmallCarryBag', 0),
    ('LargeCarryBag', 0),
    ('Napkin', 0),
    ('Sticker', 0),
    ('SubTub', 0),
    ('SubTubLid', 0),
    ('TicketPaper', 0),
    
    # CHIPS
    ('RedDoritoChip', 0),
    ('BlueDoritoChip', 0),
    ('CheetoChip', 0),
    ('GardenSalsaChip', 0),
    ('ClassicLayChip', 0),
    ('BakedLayChip', 0),
    ('BBQChip', 0),
    ('JalapenoChip', 0),
    ('SeaSaltChip', 0),
    ('VinegarChip', 0),
    ('DillPickleChip', 0),

    ('RedDorito', 0),
    ('BlueDorito', 0),
    ('Cheeto', 0),
    ('GardenSalsa', 0),
    ('ClassicLay', 0),
    ('BakedLay', 0),
    ('BBQ', 0),
    ('Jalapeno', 0),
    ('SeaSalt', 0),
    ('Vinegar', 0),
    ('DillPickle', 0),

    # VEGETABLES
    ('Onion', 0),
    ('Lettuce', 0),
    ('Tomato', 0),
    ('BananaPepper', 0),
    ('Jalapeno', 0),
    ('CPR', 0),
    ('Pickle', 0),
    ('Mayo', 0),
    ('Mushroom', 0),
    ('SweetPepper', 0),
    ('Avocado', 0),
    ('BellPepper', 0),
    
    # CONDIMENTS
    ('ChipotleMayo', 0),
    ('Ranch', 0),
    ('Mayo', 0),
    ('Buffalo', 0),
    ('BlueCheese', 0),
    ('Vinegar', 0),
    ('OliveOil', 0),
    ('Oregano', 0),
    ('Salt', 0),

    # SLICER
    ('Scale', 0),
    ('DeliPaper', 0),
    
    # PREPPED
    ('AmericanCheese', 0),
    ('SweetPepper', 0),
    ('Jalapeno', 0),
    ('Mushroom', 0),
    ('PortabellaMushroom', 0), #2.25oz
    ('Turkey', 0),
    ('Ham', 0), # == Ham * 2
    ('Proscuittini', 0), # == Proscuittini * 2
    ('Capocollo', 0), # == Capocollo * 2
    ('Salami', 0), # == Salami * 2
    ('Pepperoni', 0), # == Pepperoni * 2
    ('RoastBeef', 0), # == RoastBeef * 2
    ('Tuna', 0),# == (BlueTuna - 1) + (YellowTuna - 1)
    ('ProvoloneCheese', 0), # == ProvoloneCheese * 2
    ('SwissCheese', 0), # == SwissCheese * 2
    ('Lettuce', 0), 
    ('Onion', 0),

    # SPRINKLE
    ('SauceCup', 0),
    ('SauceCupLid', 0),

    # GRILL
    ('PhillySteak', 0),
    ('PhillySteak', 0), # == PhillySteak * 2
    ('PhillyChicken', 0),
    ('PhillyChicken', 0), # == PhillyChicken * 2
    
    # SUPPLIES
    ('SubBag', 0),
    ('SubBag', 0),
    ('WrapPaper', 0),
    ('Knife', 0),
    ('KnifeSharpener', 0),
    ('Marker', 0),
    ('Pen', 0),
    ('ToiletPaper', 0),
    ('Soap', 0),
    ('PaperTowel', 0),
    ('TrashbagLarge', 0),
    ('TrashbagSmall', 0),
    
    # BREAD
    ('WhiteBread', 0),
    ('MiniWhiteBread', 0),
    ('WheatBread', 0),
    ('MiniWheatBread', 0),
    ('RPBread', 0),
    ('MiniRPBread', 0),

    ('WhiteBreadLog', 0),
    ('WheatBreadLog', 0),

    # MEAT
    ('Turkey', 0),
    ('Ham', 0),
    ('Proscuittini', 0),
    ('Capocollo', 0),
    ('Salami', 0),
    ('Pepperoni', 0),
    ('Tuna', 0),
    ('TunasBlue', 0),
    ('TunasYellow', 0),

    # Kitchen Tools
    ('BreadKnife', 0),
    ('SmallKnife', 0),
    ('LargeKnife', 0),

    # CUPS
    ('LargeCup', 0),
    ('SmallCup', 0),

    # DESSERTS
    ('ChocolateChipCookie', 0),
    ('SugarCookie', 0),
    ('OatmealRaisinCookie', 0),
    ('DTChocolateChipCookie', 0),
    ('Brownie', 0),
    ('Snickerdoodle', 0),

    # COOKIE BOX
    ('ChocolateChipCookie', (0, 0)),
    ('SugarCookie', (0, 0)),
    ('OatmealRaisinCookie', (0, 0)),
    ('DTChocolateChipCookie', (0, 0)),
    ('Brownie', (0, 0)),
    ('Snickerdoodle', (0, 0)),

    # BOTTLES AND SHAKERS
    ('VinegarBottle', 0),
    ('OliveOilBottle', 0),
    ('OreganoShaker', 0),
    ('SaltShaker', 0),
    ('PepperShaker', 0),

    # Packaging
    ('SubBag', (0, 0)),
    ('SmallBag', (0, 0)),
    ('LargeBag', (0, 0)),
    ('SmallCarryBag', (0, 0)),
    ('LargeCarryBag', (0, 0)),
    ('SauceCup', (0, 0)),
    ('SauceCupLid', (0, 0)),
    ('BlueCheese', (0, 0)),
    ('Mayo', (0, 0)),
    ('Mustard', (0, 0)),
    ('FlourWrap', (0, 0)),
    ('WheatWrap', (0, 0)),
    
    # CONTAINERS
    ('Oil', 0),
    ('Vinegar', 0),
    ('Oregano', 0),
    ('Pepper', 0),
    ('Rosemary', 0),
    ('Jalapeno', 0),
    ('Mushroom', 0),
    ('SweetPepper', 0),
    ('BananaPepper', 0),
    ('Turkey', (0, 0)),
    ('RoastBeefPack', 0),
    ('RoastBeef', 0),


    # Cleaning Supplies
    ('SanitizeTablets', 0),
    ('GreenScrub', 0),
    ('MetalScrub', 0),
    ('DishSoap', 0),
    ('DrainSieve', 0),

    # METAL PANS
    ('MetalPanDeepWide', 0),
    ('MetalPanDeepThin', 0),
    ('MetalPanWide', 0),
    ('MetalPanThin', 0),
    ('MetalPanShallowWide', 0),
    ('MetalPanShallowThin', 0),
    ('MetalCube', 0),
    ('MetalCubeHalf', 0),
    ('MetalColdUnit', 0),

    # PLASTIC PANS
    ('PlasticPanDeepThin', 0),
    ('PlasticPanCube', 0),

    # CHEESE
    ('AmericanCheese', 0),
    ('ProvoloneCheese', 0),
    ('SwissCheese', 0),

    # 
    ('OnionSack', 0),
    ('LettuceBopped', 0),
    ('Tomato', 0),
    ('Pickle', 0),
    ('PortabellaMushroom', 0),

    # CONDIMENT CONTAINERS
    ('Mayo', 0),
    ('YellowMustard', 0),
    ('SpicyMustard', 0),
    ('HoneyMustard', 0),
    ('CPR', 0),
    ('Jalapenos', 0),
    ('BananaPeppers', 0),

    # TORTILLA
    ('FlourWrap', 0),
    ('WheatWrap', 0),

    # BOX
    ('CPR', (0, 0)),
    ('BlueCheese', (0, 0)),
    ('Mayo', (0, 0)),
    ('Mustard', (0, 0)),
    ('FlourWrap', (0, 0)),
    ('WheatWrap', (0, 0)),
    ('PhillySteak', (0, 0)),
    ('PhillyChicken', (0, 0)),
    ('Bacon', (0, 0)),
    ('WhiteBread', (0, 0)),
    ('MiniWhiteBread', (0, 0)),
    ('WheatBread', (0, 0)),
    ('MiniWheatBread', (0, 0)),
    ('GlutenFreeBread', (0, 0)),
]