# (PRODUCT, AMOUNT, ID)

inventory = [
    # SODA
    ('Pepsi', 0),
    ('DietPepsi', 0),
    ('Starry', 0),
    ('MtDew', 0),
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
    ('SugarPacket', 0),
    ('SaltPacket', 0),
    ('PepperPacket', 0),
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

    ('RedDoritoBox', 0),
    ('BlueDoritoBox', 0),
    ('CheetoBox', 0),
    ('GardenSalsaBox', 0),
    ('ClassicLayBox', 0),
    ('BakedLayBox', 0),
    ('BBQBox', 0),
    ('JalapenoBox', 0),
    ('SeaSaltBox', 0),
    ('VinegarBox', 0),
    ('DillPickleBox', 0),

    # VEGETABLES
    ('Onions', 0),
    ('Lettuce', 0),
    ('Tomato', 0),
    ('BananaPepper', 0),
    ('Jalapeno', 0),
    ('CPR', 0),
    ('Pickles', 0),
    ('Mayo', 0),
    ('Mushroom', 0),
    ('SweetPepper', 0),
    ('Avocado', 0),
    ('BellPeppers', 0),
    
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
    ('AmericanCheesePrep', 0),
    ('SweetPepperPrep', 0),
    ('JalapenoPrep', 0),
    ('MushroomPrep', 0),
    ('PortabellaMushroomPrep', 0), #2.25oz
    ('TurkeyPrep', 0),
    ('HamPrep', 0), # == Ham * 2
    ('ProscuittiniPrep', 0), # == Proscuittini * 2
    ('CapocolloPrep', 0), # == Capocollo * 2
    ('SalamiPrep', 0), # == Salami * 2
    ('PepperoniPrep', 0), # == Pepperoni * 2
    ('RoastBeefPrep', 0), # == RoastBeef * 2
    ('TunaPrep', 0),# == (BlueTuna - 1) + (YellowTuna - 1)
    ('ProvoloneCheesePrep', 0), # == ProvoloneCheese * 2
    ('SwissCheesePrep', 0), # == SwissCheese * 2
    ('LettucePrep', 0), 
    ('OnionPrep', 0),

    # SPRINKLE
    ('SauceCup', 0),
    ('SauceCupLid', 0),

    # GRILL
    ('PhillySteak', 0),
    ('PhillySteakBox', 0), # == PhillySteak * 2
    ('PhillyChicken', 0),
    ('PhillyChickenBox', 0), # == PhillyChicken * 2
    
    # SUPPLIES
    ('SubBag', 0),
    ('SubBagBox', 0),
    ('WrapPaper', 0),
    ('Knife', 0),
    ('KnifeSharpener', 0),
    ('Marker', 0),
    ('Pen', 0),
    ('ToiletPaper', 0),
    ('Soap', 0),
    ('PaperTowel', 0),
    
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

    # TRAYS
    ('WhiteBreadTray', 0), # == WhiteBread - 18
    ('WheatBreadTray', 0), # == WheatBread - 18
    ('RPBreadTray', 0), # == RPBread - 18
    ('MiniWhiteBreadTray', 0), # == RPBread - 6
    ('MiniWheatBreadTray', 0), # == RPBread - 6
    ('MiniRPBreadTray', 0), # == RPBread - 6

    # Kitchen Tools
    ('BreadKnife', 0),
    ('SmallKnife', 0),
    ('LargeKnife', 0),

    # Packaging Containers
    ('LargeCup', 0),
    ('SmallCup', 0),


    # DESSERTS
    ('ChocolateChipCookie', 0),
    ('SugarCookie', 0),
    ('OatmealRaisinCookie', 0),
    ('DTChocolateChipCookie', 0),
    ('Brownie', 0),
    ('Snickerdoodle', 0),

    # BOTTLES AND SHAKERS
    ('VinegarBottle', 0),
    ('OliveOilBottle', 0),
    ('OreganoShaker', 0),
    ('SaltShaker', 0),
    ('PepperShaker', 0),

    # Packaging Boxes
    ('SubBagBox', (0, 0)),
    ('SmallBagBox', (0, 0)),
    ('LargeBagBox', (0, 0)),
    ('SmallCarryBagBox', (0, 0)),
    ('LargeCarryBagBox', (0, 0)),
    ('SauceCupBox', (0, 0)),
    ('SauceCupLidBox', (0, 0)),
    ('BlueCheesePacketBox', (0, 0)),
    ('MayoPacketBox', (0, 0)),
    ('MustardPacketBox', (0, 0)),
    ('FlourWrapBox', (0, 0)),
    ('WheatWrapBox', (0, 0)),
    
    # Storage Containers
    ('OilContainer', 0),
    ('VinegarContainer', 0),
    ('OreganoContainer', 0),
    ('PepperContainer', 0),
    ('RosemaryContainer', 0),

    # Cleaning Supplies
    ('SanitizeTablets', 0),
    ('GreenScrub', 0),
    ('MetalScrub', 0),
    ('DishSoap', 0),
    ('DrainSieve', 0),

    # Metal Kitchen Equipment
    ('MetalPanDeepWide', 0),
    ('MetalPanDeepThin', 0),
    ('MetalPanWide', 0),
    ('MetalPanThin', 0),
    ('MetalPanShallowWide', 0),
    ('MetalPanShallowThin', 0),
    ('MetalCube', 0),
    ('MetalCubeHalf', 0),
    ('MetalColdUnit', 0),

    # Plastic Kitchen Equipment
    ('PlasticPanDeepThin', 0),
    ('PlasticPanCube', 0),

    # Jars
    ('JalapenoJar', 0),
    ('MushroomPrep', 0),
    ('SweetPepperJar', 0),
    ('BananaPepperJar', 0),

    # CHEESE
    ('AmericanCheese', 0),
    ('ProvoloneCheese', 0),
    ('SwissCheese', 0),

    # Vegetables and Prepped Vegetables
    ('OnionSack', 0),
    ('OnionPrep', 0),
    ('LettuceContainer', 0),
    ('LettuceBopped', 0),
    ('TomatoContainer', 0),
    ('PickleContainer', 0),
    ('PortabellaMushroomContainer', 0),
    ('PortabellaMushroomPrep', 0),

    # Deli Meats and Prepped Meats
    ('Ham', 0),
    ('Proscuittini', 0),
    ('Capocollo', 0),
    ('Salami', 0),
    ('Pepperoni', 0),
    ('TurkeyBox', (0, 0)),
    ('RoastBeefPack', 0),
    ('RoastBeefPrep', 0),
    ('TunaPacketsBlue', 0),
    ('TunaPacketsYellow', 0),

    # Condiment Containers
    ('MayoContainer', 0),
    ('YellowMustardContainer', 0),
    ('SpicyMustardContainer', 0),
    ('HoneyMustardContainer', 0),
    ('CPRContainer', 0),
    ('JalapenosContainer', 0),
    ('BananaPeppersContainer', 0),

    # Prepped Condiment Boxes
    ('CPRJarBox', (0, 0)),
    ('BlueCheesePacketBox', (0, 0)),
    ('MayoPacketBox', (0, 0)),
    ('MustardPacketBox', (0, 0)),
    ('FlourWrapBox', (0, 0)),
    ('WheatWrapBox', (0, 0)),

    # Meat and Bread Packaging Boxes
    ('PhillySteakBox', (0, 0)),
    ('PhillyChickenBox', (0, 0)),
    ('BaconBox', (0, 0)),
    ('WhiteBreadBox', (0, 0)),
    ('MiniWhiteBreadBox', (0, 0)),
    ('WheatBreadBox', (0, 0)),
    ('MiniWheatBreadBox', (0, 0)),
    ('GlutenFreeBreadBox', (0, 0)),

    # Cookie and Dessert Boxes
    ('ChocolateChipCookieBox', (0, 0)),
    ('SugarCookieBox', (0, 0)),
    ('OatmealRaisinCookieBox', (0, 0)),
    ('DecadentTripleChocolateChipCookieBox', (0, 0)),

    # Brownie and Snickerdoodle Boxes
    ('BrownieBox', (0, 0)),
    ('SnickerdoodleBox', (0, 0)),
    ('TrashbagLarge', 0),
    ('TrashbagSmall', 0),

    ('FlourWrap', 0),
    ('WheatWrap', 0),

]