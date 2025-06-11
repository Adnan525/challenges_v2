# Given the Solar System in the form of a list, you have to return the Solar System (as a list) 
# after the "Meteoroid"s have stopped smashing into the planets.
# The Solar System can have 2 types of celestial bodies.
# "Meteoroids"s
# Small solid planets, which are: ["Mercury", "Venus", "Earth", "Mars"]
# The direction of the "Meteoroid" will depend on the arrow, for example, "Meteoroid>" is moving to the right, 
# but "<Meteoroid" is moving to the left. All "Meteoroid"s will have an arrow, either pointing to the left or 
# the right.
# The small solid planets' sizes are denoted with brackets, for example, "(((Mars)))" is bigger than "(Venus)". 
# The planets can also have no brackets, like just "Earth".
# A "Meteoroid" crosses another "Meteoroid" without changing anything, and continues to go onward.
# If a moving "Meteoroid" goes out of the list, it has to be simply removed from the Solar System.
# Now, each time a moving "Meteoroid" hits a planet, it breaks, but the planet it hit loses one pair of brackets.
# If a "Meteoroid" hits a planet without any brackets (or with all its brackets removed by other "Meteoroid"s), 
# then both the planet and the "Meteoroid" break.
# EXAMPLE
# Given the Solar System: ["<Meteoroid", "Meteoroid>", "Meteoroid>", "((Mercury))", "Meteoroid>", "Mars", 
# "<Meteoroid", "Meteoroid>", "((Earth))"]
# You start with the first "<Meteoroid".
# "<Meteoroid" moves to the left, and straight away goes out of orbit.
# Solar System: ["Meteoroid>", "Meteoroid>", "((Mercury))", "Meteoroid>", "Mars", "<Meteoroid", "Meteoroid>", 
# "((Earth))"]
# "Meteoroid>" starts to move, crosses another "Meteoroid>", smashes into "((Mercury))", gets destroyed 
# but reduces "(Mercury)" to just one pair of brackets.
# Solar System: ["Meteoroid>", "(Mercury)", "Meteoroid>", "Mars", "<Meteoroid", "Meteoroid>", "((Earth))"]
# Next, the second "Meteoroid>" moves. It smashes into "(Mercury)" and breaks. Now Mercury is just "Mercury".
# Solar System: ["Mercury", "Meteoroid>", "Mars", "<Meteoroid", "Meteoroid>", "((Earth))"]
# Mercury can't move and change things, so we move onto the next Meteoroid, which is "Meteoroid>". 
# It moves and smashes into a bracket-less and unprotected "Mars". Both the "Meteoroid" and "Mars" are be destroyed.
# Solar System: ["Mercury", "<Meteoroid", "Meteoroid>", "((Earth))"]
# Now it's the next Meteoroid, who is moving towards the left. Directly towards poor, battle-worn Mercury! 
# Mercury has no brackets, so both get destroyed!
# Solar System: ["Meteoroid>", "((Earth))"]
# "Meteoroid>" moves towards "((Earth))" and smashes into it. The "Meteoroid" breaks, but "(Earth)" only 
# loses a pair of brackets.
# Solar System: ["(Earth)"]
# Now that the "(Earth)" is not going anywhere and everything's done. You have to return the new Solar System, 
# ["(Earth)"].
# =================================================================================================================

def meteor_shower(solar_system: list[str]) -> list[str]:
    is_meteor = lambda x: "Meteoroid" in x
    delta_index = lambda x: -1 if x.startswith("<") else 1

    while any("Meteoroid" in obj for obj in solar_system):
        for i, item in enumerate(solar_system):
            print(solar_system)
            # print(f"Processing item: {item} at index {i}")
            if is_meteor(item):
                # print(f"Is a Meteoroid: {is_meteor(item)}")
                old_i = i
                while i >= 0 and i < len(solar_system):
                    hit_index = i + delta_index(item)

                    if hit_index < 0 or hit_index >= len(solar_system):
                        solar_system[old_i] = "removed"
                        i = old_i  # reset to original index
                        break # out of bounds
                    hit_item = solar_system[hit_index]
                    if is_meteor(hit_item):
                        i = hit_index  # continue moving in the same direction
                        continue # skip and continue moving left
                    else:
                        if "removed" in hit_item:
                            i = hit_index
                            continue
                        if hit_item.startswith("("):
                            # hit a planet with brackets
                            solar_system[hit_index] = hit_item[1:-1]
                        else:
                            # hit a planet without brackets
                            solar_system[hit_index] = "removed"
                        solar_system[old_i] = "removed"
                        i = old_i  # reset to original index
                        break
                break
    
    return [planet for planet in solar_system if planet != "removed"]

test = ['<Meteoroid', 'Meteoroid>', 'Meteoroid>', '((Mercury))', 'Meteoroid>', 
        'Mars', '<Meteoroid', 'Meteoroid>', '((Earth))']
result = meteor_shower(test)
print(result)