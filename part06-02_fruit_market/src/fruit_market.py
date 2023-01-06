# write your solution here

def read_fruits():

    with open("fruits.csv") as new_file:

        fruits_dict = {}

        for line in new_file:
            line = line.replace("\n", "")
            part = line.split(";")
            fruit_name = part[0]
            fruid_price = part[1]
            fruits_dict[fruit_name] = float(fruid_price)

        return fruits_dict


if __name__ == "__main__":
     print(read_fruits())

