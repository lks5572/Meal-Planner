import random, numpy as np

recipes = {'Vegan': [
                    [
                        ['tofu', 'udon noodles', 'mushrooms', 'onion', 'soy sauce', 'gochujang'],

                        ['rice', 'chickpeas', 'tomato'],

                        ['dry split lentils', 'pasta sauce', 'spaghetti'],

                        ['soba noodles', 'cucumber', 'hummus'],

                        ['veggie grounds', 'pasta sauce', 'baby spinach', 'lasagna noodles', 'extra firm tofu',
                         'lemon juice', 'garlic powder', 'nutritional yeast'],

                        ['sushi rice', 'rice vinegar', 'smoked tofu', 'nori sheet', 'lettuce', 'carrots', 'cucumber',
                          'avocado'],

                        ['bread', 'hummus', 'favorite vegetables'],

                        ['tofu', 'broccoli', 'carrot', 'sweet chili sauce'],

                        ['macaroni', 'chickpeas', 'avocado', 'onion', 'garlic powder', 'bell pepper'],

                        ['rotini pasta', 'peanut butter', 'red curry paste']
                    ],

                    [
                        ['Udon', '1/4 block tofu, cut into bite-sized cubes', '1 serving of udon noodles',
                         '1/2 cup chopped mushrooms', '1/4 of a small onion, thinly sliced',
                         '1 tbsp gochujang (sauce)', '1 tbsp soy sauce (sauce)', '',

                         '1. Heat a non-stick pan on high heat.',
                         '2. Cook udon noodles according to instructions.',
                         '3. In the pan, add a small amount of oil and add the tofu pieces. Allow the tofu to'
                         ' cook on one side while you chop the vegetables or mix together the sauce.',
                         '4. Mix together the sauce ingredients in a small bowl.',
                         '5. Flip over the tofu and allow to cook on the other side.',
                         '6. Once tofu is done cooking, remove from pan and add in the mushrooms and onions. Saute'
                         ' until mushrooms begin to brown and onions soften.',
                         '7. When noodles are cooked, drain and add into the pan. Add the tofu back in along with '
                         'the sauce and mix well.', ''],

                        ['Chickpea Tomato Rice', '2 cups rice', '2 cups water', '1 can chickpeas', '1 large tomato, cut'
                         ' into chunks', 'seasoning/sauces', '',

                         '1. Add all the ingredients into a rice cooker and mix well',
                         '2. Cook using the rice setting',
                         '3. Add seasoning and sauces as desired',''],

                        ['Lentil Spaghetti', '3/4 cup dry red split lentils', '1 cup pasta sauce', '1 serving '
                         'spaghetti', '',

                         '1. Soak lentils in water for 10-15 minutes.',
                         '2.Add the lentils to a pan with a little bit of water and bring to a boil, boil spaghetti in '
                         'the meantime.',
                         '3. After about 10-15 minutes, add the pasta sauce to lentils.',
                         '4. Cover and simmer in low heat for about 5-10 minutes, then mix in spaghetti.',''],

                        ['Hummus Soba', '1 serving soba noodles', '1/3 cucumber', '2-3 tbsp hummus','',

                         '1. Cook soba noodles according to instructions.',
                         '2. Chop cucumber into long, thin pieces.',
                         '3. Mix hummus with a splash of water to thin it out until it is more of a sauce consistency.',
                         '4. Drain and rinse soba noodles with cold water.',
                         '5. Add in hummus and cucumber to the noodles and mix well, add toppings if desired.',''],

                        ['Lasagna', '1/2 package veggie grounds', '1 jar of pasta sauce', '2 handfuls of baby spinach',
                         '1 package of lasagna noodles', '1 block extra firm tofu', 'lemon juice', 'garlic powder',
                         'salt', 'nutritional yeast', '',

                         '1. Preheat oven to 400 degrees Fahrenheit.',
                         '2. Add tofu, lemon juice, garlic powder, and yeast into a food processor and blend it until '
                         'the consistency is very smooth, similar to cream cheese.',
                         '3. In a baking dish, spread a layer of pasta sauce on the bottom and place lasagna noodles '
                         'side by side. Depending on the type of noodles you have, you might have to cook them first.',
                         '4. Spread a layer of tofu cheese on top of the noodles then place some spinach over that.',
                         '5. Continue with another layer of noodles then add some veggie crumble and spread it on top.',
                         '6. Add another layer of sauce then place more more noodles on top.',
                         '7. Finish it off with a layer of pasta sauce and make sure all of the noodles are covered.',
                         '8. Cover the baking dish with aluminum foil and place it in the oven for 30 minutes.',
                         '9. Remove the aluminum foil and bake for an additional 10-15 minutes.', ''],

                        ['Sushi Rolls', '1 cup cooked sushi rice', '1 tbsp rice vinegar', 'few pieces of smoked tofu',
                         'nori sheet', 'lettuce', 'carrots', 'cucumber', 'avocado','',

                         '1. Heat up a pan with some oil and fry the tofu for a few minutes on each side, until '
                         'browned. Cut length wise into thin strips.',
                         '2. Prepare all your veggies into long, thin strips.',
                         '3. In a bowl, mix the rice with the rice vinegar.',
                         '4. On a flat surface, place a nori sheet and spread the rice evenly and flatten it out. '
                         'Leave a little bit of space on one side of the nori to bind the roll later.',
                         '5. Add your veggies and tofu in a line along the middle then roll it up. Use some water to wet '
                         'the space on the nori you left so that it will stick to the other side.',
                         '6. Use a sharp knife to carefully cut the roll into bite sized pieces.', ''],

                        ['Veggie Sandwich', '2 pieces of bread', '2 tbsp hummus', 'Whatever veggies you want','',
                         
                         '1. Toast some sandwich bread in a toaster.',
                         '2. Spread a layer of hummus on both pieces of bread.',
                         '3. Chop all your veggies into thin slices and place them on the bread to construct your '
                         'sandwich.',''],

                        ['Sweet Chili Mix', '1/2 block tofu', '1 cup chopped broccoli', '1/2 carrot, chopped', '2-3 '
                         'tbsp sweet chili sauce','',

                         '1. Use a paper towel to wipe off the excess water on the tofu and cut it into cubes.',
                         '2. Heat a non-stick pan and add some oil. Add the tofu and try to make sure none of the '
                         'pieces are touching as the starch likes to stick them together.',
                         '3. Cook them on medium-high for about 2-3 minutes on each side until they are golden and '
                         'crispy then remove them from the pan and set aside.',
                         '4. Place the veggies in the pan and cook them for a few minutes. Add a bit of water to cook '
                         'them thoroughly.',
                         '5. Place the tofu back into the pan and add some sweet chili sauce and mix together.',
                         '6. Add toppings as desired.',''],

                        ['Chickpea Guacaroni', '1 serving macaroni', '3/4 cup chickpeas, cooked', '1/2 avocado',
                         '1 tbsp diced onion', '1/2 tsp garlic powder', '1/2 bell pepper', 'salt & pepper', '',

                         '1. Cook macaroni according to instructions.',
                         '2. Meanwhile, mash your chickpeas with a fork.',
                         '3. Mix in and mash the ripe avocado.',
                         '4. Add in onion, garlic powder, bell pepper, and mix well.',
                         '5. Once macaroni is cooked, drain and rinse thoroughly under cold water.',
                         '6. Add macaroni into the avocado and chickpea mixture and mix, then add salt and pepper.', ''],

                        ['Red Curry Pasta', '3oz rotini pasta', '2 tbsp peanut butter', '1 tbsp red curry paste',
                         '1-2 tbsp water', 'salt & pepper','',

                        '1. Cook pasta according to instructions. Save a small amount of pasta water (about 1/2 cup) '
                        'before draining the pasta.',
                        '2. While pasta is cooking, add peanut butter and red curry paste into a small bowl and mix '
                        'well.',
                        '3. Add 1-2 tbsp of water to thin out the sauce mixture and mix well.',
                        '4. Take out the cooked pasta and using the same pot, add the sauce mixture along with the '
                        'saved pasta water. Then add the pasta back in and mix well.', '']
                    ]
                    ],

            'Vegetarian':[
                        [
                            ['eggs', 'olive oil', 'cherry tomatoes', 'basil', 'shredded cheddar'],

                            ['tortillas', 'tomato sauce', 'ball of mozzarella cheese', 'olives', 'onion', 'tomato',
                             'bell pepper'],

                            ['eggs', 'cheddar cheese', 'sourdough bread', 'tomato', 'olive oil'],

                            ['olive oil', 'potato', 'onion', 'tofu', 'cherry tomatoes'],

                            ['avocado', 'onion', 'tomato', 'lemon', 'chili pepper', 'tortillas', 'olive oil'],

                            ['white beans', 'onion', 'bell pepper', 'olive oil', 'cilantro and parsley',
                             'sun-dried tomatoes in oil'],

                            ['banana', 'eggs', 'maple syrup', 'berries of choice'],

                            ['flour', 'eggs', 'onion', 'corn', 'olive oil'],

                            ['whole wheat bread', 'ball of mozzarella cheese', 'sun-dried tomatoes in oil', 'olives',
                             'basil'],

                            ['rotini pasta', 'olive oil', 'onion', 'garlic cloves', 'tomato sauce', 'basil',
                             'spinach', 'butter', 'mascarpone']
                        ],

                        [
                            ['Omelette', '2 eggs', '2 tbsp olive oil', '1/2 cup cherry tomatoes', '1/2 cup basil',
                             '1/4 cup cheese', '',

                             '1. Wash the tomatoes and chop into small pieces.',
                             '2. Heat oil in a pan and fry the tomatoes for about 2 minutes. Set aside. Clean the pan '
                             'with a tissue.',
                             '3. Crack the eggs into a bowl and beat well with a fork, adding the salt and pepper.',
                             '4. Heat the rest of the oil in a pan (non-stick if possible) on low to medium heat.',
                             '5. Pour the egg mix into the pan.',
                             "6. Using a spatula, ruffle the omelette so it doesn't stick.",
                             "7. Let it cook for about 2 minutes and when the egg mixture looks nearly cooked, drop on "
                             "the tomatoes and basil.", ''],

                           ['Tortilla Pizza', '2 tortillas', '1/2 cup tomato sauce', '1/2 ball mozzarella cheese',
                            '1/2 handful olives', '1/2 onion', '2 tomatoes', '1/4 bell pepper', 'basil', '',

                            '1. Spread the tomato sauce and basil over each tortilla.',
                            '2. Slice the cheese into thin layers and add to tortillas.',
                            '3. Chop the veggies into small pieces then place evenly on tortillas.',
                            '4. Cook in the oven for 10-15 mins at 360°F, then let cool', ''],

                            ['Welsh Rarebit', '1 egg yolk', 'salt and pepper', '4 ounces shredded cheddar cheese',
                             '2 slices sourdough loaf', '4 slices tomato', '2 tsp olive oil', '',

                             '1. Preheat broiler.',
                             '2. In a medium bowl, whisk together salt, pepper, and egg yolk. Stir in shredded cheddar '
                             'until well blended.',
                             '3. Arrange bread slices and tomato slices on a baking sheet. Drizzle tomato slices with '
                             'olive oil and season with salt and pepper. Broil 3 minutes.',
                             '4. Remove from broiler and spread cheese mixture evenly over each bread slice. Broil '
                             'until melted and bubbly, 3 to 4 minutes more.',
                             '5. Top of each bread slice with two broiled tomato slices on and serve immediately.', ''],

                            ['Potato Mix', '1.5 tbsp olive oil', '2 potatoes', '1 onion', '3.5 oz tofu',
                             'salt and pepper', 'seasoning as desired', '1/2 cup cherry tomatoes','',
                             
                             '1. Clean and cut the potatoes in cubes. Peel and cut the onions into “half rings”.',
                             '2. In a pan, put a bit of olive oil and set to low-medium heat. Add the potatoes and cook'
                             'for 5 mins, stirring gently. Then add the onions.',
                             '3. Now crumble in the tofu. Stir and add the spices, salt and pepper. If you have, put a '
                             'lid onto the pan and cook for 15 min.',
                             '4. In a second pan add olive oil and set to medium heat. Cut the tomatoes in half and fry'
                             'for roughly 5 minutes until some dark spots appear. Season with salt and pepper.',
                             '5. Assemble the potato mix and tomatoes on a plate.', ''],

                            ['Nachos and Guacamole', '1 avocado', '1/2 onion', '2 tomatoes', '1/2 lemon, juiced',
                             '1 chopped chili pepper', 'salt and pepper', '3 tortillas', '3 tbsp olive oil', '',

                             '1. Cut the avocado and remove stone. Take out the flesh and mash it in a bowl.',
                             '2. Peel and finely dice the onion. Throw into the bowl as well.',
                             '3. Chop the tomatoes and chuck in too.',
                             '4. Add the salt, pepper, and chopped chili, and squeeze in the lemon, then mix well.',
                             '5. Using scissors, layer the tortillas on top of each other and cut into triangles.',
                             '6. Spread olive oil andsSprinkle the salt over the tortillas.',
                             '7. Place on a tray and bake for 5 minutes in the oven at 390°F.'
                             '8. Eat with guacamole and enjoy.', ''],

                            ['White Bean Salad', '1 can white beans', '1 onion', '4 sun-dried tomatoes',
                             '1 bell pepper', '3 tbsp olive oil', '1 small handful parsley',
                             '1 small handful cilantro', 'salt and pepper', '',

                             '1. Wash the beans and let water drain.',
                             '2. Dice onion into small pieces.',
                             '3. Wash bell pepper, cut into small pieces as well.',
                             '4. Add parsley and cilantro.',
                             '5. Cut the dried tomatoes in small strips.',
                             '6. Throw everything into a big bowl, add the olive oil, and finish it off with some salt'
                             'and pepper.', ''],

                            ['Banana Pancakes', '1 banana', '2 eggs', 'handful of assorted berries', 'butter',
                             'maple syrup', '',

                             '1. Mash up bananas in a large bowl.',
                             '2. Whisk eggs and add to banana paste.',
                             '3. Fry gently in a pan on low-medium heat with a little heated oil or butter.',
                             '4. Top with berries and maple syrup.', ''],

                            ['Corn Fritters', '1/3 cup flour', 'salt', 'pepper', '1 egg', '6 tbsp water', '1/2 onion',
                             '1 cup corn','2 tbsp olive oil', '',

                             '1. In a bowl add flour, salt, pepper, egg and water. Mix to a batter.',
                             '2. Finely dice the red onion and rinse and drain the corn. Mix in both to the batter.',
                             '3. Add the olive oil to a pan and set to medium heat.',
                             '4. Take a burger-sized amount of the batter and place it into the pan.',
                             '5. Fry flat in the pan 5 minutes each side or until golden brown.', ''],

                            ["Runner's Sandwich", '4 slices bread', '1/2 ball mozzarella,', '1/4 cup dried tomatoes',
                             '2 tbsp olives', '1/4 cup basil', 'salt and pepper', '',
                             
                             '1. Roughly chop the cheese, tomatoes, and olives and throw into a mixing bowl.',
                             '2. Add the herbs, salt and pepper.',
                             '3. Use a fork to mix up and mash the ingredients a little.',
                             '4. If you’re using soft bread, pop it in the toaster/pan without oil for a minute or so.',
                             '5. Spread the mix on the bottom slices, add the other slices on top. Squish down.',
                             '6. Heat the pan (with or without the oil) and put the sandwich in. Put a lid on the pan. '
                             'Cook for 3 or 4 min, squishing down with a spatula occasionally, then flip and cook the '
                             'other side the same way.', ''],

                            ['One Pot Pasta', '2 cups rotini pasta', '1 tbsp olive oil', '1/2 chopped onion',
                             '3 crushed garlic cloves', 'salt', 'desired herbs', '3/4 cup tomato sauce', '4 cups water',
                             'handful of basil', '1 cup spinach', '3 tbsp butter', '3 spoonfuls mascarpone', '',

                             '1. In a large pot, heat some olive oil and gently saute your onions until soft.',
                             '2. Add the garlic and herbs, and saute on a very low heat for a further 1-2 minutes.',
                             '3. Add tomato sauce and salt. Cook for 5 minutes, until bubbling.',
                             '4. Add the pasta, bring to the boil, and then simmer for 10 to 12 minutes, stirring often,'
                             ' until the pasta has cooked and the sauce has thickened back up.',
                             '5. Now add the spinach, basil and butter, and stir over a low heat until cooked down.',
                             '6. Finally, stir in the mascarpone until melted.', '']
                        ]
            ],

            'All':[
                [
                    ['chili garlic sauce', 'soy sauce', 'brown sugar', 'ground pork','ramen noodles', 'chopped peanuts'],

                    ['rice', 'ground beef', 'corn', 'black beans', 'shredded cheddar', 'salsa'],

                    ['English muffins', 'tomato sauce', 'shredded mozzarella', 'spinach'],

                    ['soy sauce', 'sriracha', 'cabbage', 'carrot', 'ground beef', 'ginger'],

                    ['bowtie pasta', 'broccoli', 'butter', 'parmesan cheese'],

                    ['olive oil', 'onion', 'garlic cloves', 'ground turkey', 'black beans', 'diced tomatoes',
                     'tomato sauce'],

                    ['lo mein noodles', 'butter', 'eggs', 'soy sauce', 'sriracha', 'sugar'],

                    ['olive oil', 'garlic cloves', 'spinach', 'ciabatta rolls', 'shredded mozzarella', 'feta cheese'],

                    ['tortillas', 'pepperoni', 'mozzarella cheese sticks', 'pizza sauce'],

                    ['chopped chicken', 'black beans', 'onion', 'shredded cheddar', 'sweet BBQ sauce', 'tortillas']
                ],

                [
                    ['Pork & Peanut Noodles', '1/4 cup chili garlic sauce', '1/4 cup soy sauce', '1/4 cup brown sugar',
                     '1/2 lb. ground pork', '6 oz. ramen noodles', '1/4 cup chopped peanuts', '',

                     '1. Combine the chili garlic sauce, soy sauce, and brown sugar in a bowl.',
                     '2. Add the ground pork to a skillet and cook over medium heat until it is fully browned. Once '
                     'browned, add the prepared sauce and chopped peanuts. Allow the pork and peanuts to simmer in the '
                     'sauce for another 5 minutes',
                     '3. While the pork is browning, begin boiling water for your noodles. Once boiling, add your noodles'
                     ' and cook according to the package directions. Drain the noodles in a colander.',
                     '4. Once the sauce has reduced and the noodles have drained, add the noodles to the skillet and toss'
                     ' until everything is combined and coated in sauce.', '' ],

                    ['Burrito Bowl', '1 cup rice', '1/4 lb ground beef', '1/4 cup corn', '1/4 can black beans',
                     '1 cup shredded cheese', '1/3 cup salsa', '',

                     '1. Cook the rice according to the package directions.',
                     '2. While the rice is cooking, add the ground turkey or beef to a skillet and cook over medium '
                     'heat until it is cooked through.',
                     '3. Once the meat is fully cooked, add the taco seasoning and 1/2 cup water. Stir and simmer the '
                     'meat and spices for 5 min. Turn the heat off and set the meat aside.',
                     '4. Rinse and drain the black beans and shred the cheese.',
                     '5. Once the rice is finished, fluff it with a fork and add all other ingredients.', ''],

                    ['Freezer Mini Pizza - overnight', '2 English Muffins', '1/4 cup tomato sauce', '1/2 cup '
                     'shredded mozzarella', 'handful of spinach', '',
                     
                     '1. Line two small baking sheets with foil or parchment paper. Open the English muffins and line '
                     'them up on the baking sheets with cut sides facing up.',
                     '2. Spread about 1 Tbsp pizza sauce over the surface of each muffin, then top with about 2 Tbsp '
                     'shredded mozzarella.',
                     '3. Chop the spinach into very small pieces, then divide them evenly among the pizzas. Cover the '
                     'baking sheets with plastic wrap and freeze for about 8 hours.',
                     '4. To bake the pizzas, place them on a baking sheet, and let them partially thaw as you preheat '
                     'the oven to 400ºF. Once the oven is fully preheated, bake the pizzas for about 15 minutes.', ''],

                    ['Beef and Cabbage Stir Fry', '0.5 Tbsp soy sauce', '0.5 Tbsp sriracha', '1/4 head cabbage',
                     '1/2 carrot, shredded', '1/4 lb ground beef', '1/2 tbsp grated ginger', 'salt and pepper', '',

                     '1. In a small bowl stir together the soy sauce and sriracha. Set the sauce aside.',
                     '2. Cut one small cabbage in half, remove the core, and then finely shred the leaves of one fourth'
                     'of the cabbage.'
                     '3. Heat a large skillet over medium heat. Once hot add cooking oil, ground beef, ginger, and '
                     'pinch of salt and pepper. Cook the beef for about five minutes.',
                     '4. Add the cabbage and carrots to the skillet and continue to stir and cook until the cabbage is '
                     'slightly wilted. Stir in the prepared sauce and top with sriracha.', ''],

                    ['Bowties and Broccoli', '1/2 cup bowtie pasta', '1/3 lb broccoli', '1 tbsp butter',
                     '1 tbsp grated parmesan', 'salt and pepper', '',

                    '1. Bring a pot of water to a boil, then add the pasta. Boil for 7-10 minutes.',
                    '2. Add the broccoli florets to the boiling pasta water, turn off the heat, and let sit for 1-2 '
                    'minutes. Drain the pasta and broccoli in a colander.',
                    '3. Transfer the pasta and broccoli back to the pot (with the heat off) or to a bowl and add the '
                    'butter. Toss until the butter has melted and coated everything. Add the Parmesan, salt, and '
                    'pepper, then toss to coat again. Serve immediately.', ''],

                    ['Black Bean Chili', '1/3 tbsp olive oil', '1/3 onion', '1.5 cloves garlic', '1/4 lb ground turkey',
                     '1 can black beans', '1/3 can diced tomatoes', '1/4 cup tomato sauce', 'salt', 'spices as desired',
                     '',

                     '1. Dice the onion and mince the garlic. Add the onion and garlic to a large pot with 1 Tbsp olive'
                     ' oil and cook over medium-low heat for 2-3 minutes.',
                     '2. Add the ground turkey to the pot and continue to sauté for 5-7 minutes. Break the turkey up '
                     'into small crumbles with your spoon as it cooks.',
                     '3. Add the beans (undrained), the diced tomatoes (undrained), tomato sauce, and spices. Stir '
                     'everything to combine.',
                     '4. Let the chili simmer for about 10 minutes. Taste the chili and add salt as needed.', ''],

                    ['Spicy Noodles', '2 oz. lo mein noodles', '1 Tbsp butter', '1 egg', '0.5 Tbsp sugar',
                     '0.5 Tbsp soy sauce', '0.5 Tbsp sriracha', '',

                     '1. Begin to boil water for the noodles. Once the water reaches a full boil, add the noodles and '
                     'cook according to the package directions.',
                     '2. In a small bowl stir together the sugar, soy sauce, and sriracha.',
                     '3. In a large skillet melt 2 tablespoons of butter over medium-low heat. Whisk an egg in a bowl '
                     'and then add to the melted butter. Once the egg is done cooking, turn off the heat.',
                     '4. When the noodles are tender, drain the water and then add them to the skillet with the cooked '
                     'egg. Also add the prepared sauce. Turn the heat on to low and stir until everything is coated '
                     'well with the sauce.', ''],

                    ['Spinach Feta Grilled Cheese', '1/2 Tbsp olive oil', '1 clove garlic', '1/4 lb cut spinach',
                     'salt and pepper', '2 ciabatta rolls', '2 ciabatta rolls', '1 cup shredded mozzarella', '1 oz feta'
                     ' cheese', '',

                     '1. Mince the garlic and add it to a skillet with the olive oil. Cook over medium-low heat for '
                     '1-2 minutes. Add the spinach, turn the heat up to medium, and cook for about 5 minutes. Add '
                     'salt and pepper.',
                     '2. Cut the rolls in half. Add about 1/4 cup of shredded mozzarella and 1/2 oz. of feta to the '
                     'bottom half of each roll. Divide the cooked spinach between the two sandwiches and 1/4 cup '
                     'shredded mozzarella on each.',
                     '3. Place the top half of the ciabatta roll on the sandwiches and transfer them to a large '
                     'non-stick skillet. Fill a large pot with a few inches of water to create weight, then place the '
                     'pot on top of the sandwiches to press them down. Turn the heat on to medium-low and cook until '
                     'the sandwiches are crispy on the bottom. Carefully flip the sandwiches, place the weighted pot '
                     'back on top, and cook until crispy on the other side and the cheese is melted.', ''],

                    ['Pizza Rolls', '4 torillas', '20 slices pepperoni', '2 mozzarella cheese sticks',
                     '0.25 cup pizza sauce', '',

                     '1. Preheat the oven to 400ºF. Lightly spritz a baking sheet with spray oil.',
                     '2. Stack about 4 tortillas at a time on a plate and cover with a damp paper towel. Microwave for '
                     '20-30 seconds.',
                     '3. Slice each of the mozzarella sticks in half, lengthwise. Place about 5 pepperoni on each '
                     'tortilla in the bottom 1/3 of the circle, then place the halved mozzarella stick on top. Fold '
                     'the sides of the tortilla in to cover the ends, then roll them up tight like a burrito.',
                     '4. Place the tightly rolled Pizza Roll Ups on the baking sheet, seam side down. Leave them '
                     'slightly apart from one another.Spritz the top with spray oil.',
                     '5. Bake for 12-15 minutes, and serve with pizza sauce.', ''],

                    ['Chicken Tortillas', '0.5 cups chopped cooked chicken', '0.5 can black beans, drained',
                     '1/4 onion', '3/4 cups shredded cheddar', '1/4 cup sweet BBQ sauce', 'salt' '4 tortillas', '',
                     
                     '1. Add the chopped chicken and black beans to a large bowl. Finely dice the red onion. Add the '
                     'onion, shredded cheddar, salt, and BBQ sauce to the bowl with the chicken and beans. Stir until '
                     'everything is evenly combined.',
                     '2. Place the BBQ chicken mixture on each tortilla and spread it evenly over one half of the '
                     'surface. Fold closed.'
                     '3. Cook the tortillas in a dry skillet over medium-low heat, until the outside is brown and '
                     'crispy, the filling has heated through, and the cheese has melted. Cut each quesadilla in half '
                     'and serve.', '']
                ]

                ]

           }


def PlanMeal():
    print("Hello! Welcome to Lauren's Meal Planner.\n"
          "The goal of this project is to create a weekly shopping list that includes ingredients for healthy meals.\n"
          "This project was made by a college student who will be living on her own next year and wanted\n"
          "to stay in shape and learn how to cook.\n")

def start():
    ans = input("Please type Vegan or Vegetarian below.\n"
                "Otherwise, please type 'Next.'\n")
    if ans == 'Vegan' or ans == 'vegan':
        del recipes['Vegetarian']
        del recipes['All']
    elif ans == 'Vegetarian' or ans == 'vegetarian':
        del recipes['All']
    elif ans == 'Next' or ans == 'next':
        pass
    else:
        start()

def shoppinglist():
    print("Here is your weekly shopping list for 3 recipes. To generate 3 new recipes, please type 'N.'")
    n = np.random.choice(9, 3, replace=False)
    x = 0
    L1 = []
    L = []
    L3 = []
    for i in range (1,4):
        a = random.choice(list(recipes))
        b = '\n'.join(recipes[str(a)][0][n[x]])
        c = '\n'.join(recipes[str(a)][1][n[x]])
        L.append(b)
        L1.append(c)
        x += 1
    s = set(L)
    for each in s:
        L3.append(each)
    L3.append('')
    L2 = (L3 + L1)
    print('\n'.join(L2))

def new():
    x = input()
    if x == 'n' or x == 'N':
        shoppinglist()
    else:
        new()

def run():
    PlanMeal()
    start()
    shoppinglist()
    new()

run()

# references:
# https://www.thecheaplazyvegan.com/category/college-student-recipes/
# https://www.budgetbytes.com/top-10-recipes-for-college-students/
# https://hurrythefoodup.com/vegetarian-recipes-for-students/

# yeet