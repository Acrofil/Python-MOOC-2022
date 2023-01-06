# Write your solution here
def search_by_name(filename: str, word: str):

    recipes_list = []
    with open(filename) as file:
        

        for line in file:
            if line == line.lower():
                continue
            if line not in recipes_list:
                recipes_list.append(line.strip())
    

    searched_recipes = []
    for recipe in recipes_list:
        if word in recipe.lower():
            searched_recipes.append(recipe)
    
    return searched_recipes


def search_by_time(filename: str, prep_time: int):

    new_file = []
    shortest_time_recipe = []
    with open(filename) as file:
        for line in file:
            line = line.strip().replace("\n", "")
            new_file.append(line)
        
    
    for x in range(len(new_file)):

        if new_file[x].isdigit() == False:
            continue
        elif int(new_file[x]) <= prep_time:
            shortest_time_recipe.append(f"{new_file[x - 1]}, preparation time {new_file[x]} min")
            
    return shortest_time_recipe
        

def search_by_ingredient(filename: str, ingredient: str):
    recipe_list = []
    string = ""
    space = " "
    recipes = []
    all_recipes = []
    redepc_dict = {}
    with open(filename) as file:
        for line2 in file:
            line2 = line2.strip().replace("\n", "")
            recipes.append(line2)

    for x in range(len(recipes)):
        
        if recipes[x].isdigit() == False:
            continue
        elif ingredient in recipes[x]:
            all_recipes = recipes[:x]

        for c in all_recipes[::-1]:
            if space in c:
                if c.split()[0].istitle():
                    string = c
                    d = recipe_list.index(c)
                    if c in recipe_list:
                        break
                    else:
                        redepc_dict[c] = recipe_list[d + 1]
                        continue
                elif c.istitle():
                    string = c
                    d = redepc_dict.index(c)
                    if c in redepc_dict:
                        break
                    else:
                        redepc_dict[c] = recipe_list[d + 1]
                        continue
        recipe_list.clear()
        for name in redepc_dict:
            string = f"{name}, preparation times {redepc_dict[name]} min"
            recipe_list.append(string)
        return recipe_list


            

    




if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)
  


