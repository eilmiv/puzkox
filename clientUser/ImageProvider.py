import os
from bisect import bisect_left

class ImageProvider:
    def __init__(self, pygame, path):
        self.pygame = pygame
        self.car_images = dict()
        self.grass_images = dict()
        self.house_images = dict()
        self.street_images = dict()
        self.original_images = []
        self.scaled_images = []
        self.original_car_images = []
        self.scaled_car_images = []
        self.load_images(path)

    def load_images(self, path):
        pygame = self.pygame

        # read and categorize images
        for name in os.listdir(path):
            image_path = os.path.join(path, name)
            properties = name[:-4].split('_')

            if properties[0] == 'car':
                if len(properties) == 3:
                    try:
                        version = int(properties[1])
                        damage = float(properties[2])
                        image = pygame.image.load(image_path).convert_alpha()
                        index = len(self.original_car_images)
                        self.original_car_images.append(image)
                        if version in self.car_images:
                            self.car_images[version].append((damage, index))
                        else:
                            self.car_images[version] = [(damage, index)]
                    except ValueError:
                        print("invalid image, expected car_int version_float damage: " + str(image_path))
                else:
                    print("invalid image option count, expected car_version_damage: " + str(image_path))

            elif properties[0] == 'grass':
                if len(properties) == 3:
                    try:
                        biome = int(properties[1])
                        version = int(properties[2])
                        image = pygame.image.load(image_path).convert()
                        index = len(self.original_images)
                        self.original_images.append(image)
                        self.grass_images[(biome, version)] = index
                    except ValueError:
                        print("invalid image, expected grass_int biome_int version: " + str(image_path))
                else:
                    print("invalid image option count, expected grass_biome_version: " + str(image_path))

            elif properties[0] == 'house':
                if len(properties) == 4:
                    try:
                        biome = int(properties[1])
                        version = int(properties[2])
                        damage = float(properties[3])
                        image = pygame.image.load(image_path).convert()
                        index = len(self.original_images)
                        self.original_images.append(image)
                        if (biome, version) in self.house_images:
                            self.house_images[(biome, version)].append((damage, index))
                        else:
                            self.house_images[(biome, version)] = [(damage, index)]
                    except ValueError:
                        print("invalid image, expected house_int biome_int version_float damage: " + str(image_path))
                else:
                    print("invalid image option count, expected house_biome_version_damage: " + str(image_path))

            elif properties[0] == 'street':
                if len(properties) == 4:
                    try:
                        biome = int(properties[1])
                        version = int(properties[2])
                        directions = int(properties[3], base=2)
                        image = pygame.image.load(image_path).convert()
                        index = len(self.original_images)
                        self.original_images.append(image)
                        if (biome, version) in self.street_images:
                            self.street_images[(biome, version)][directions] = index
                        else:
                            self.street_images[(biome, version)] = {directions: index}
                    except ValueError:
                        print("invalid image, expected street_int biome_int version_nosw directions: " + str(image_path))
                else:
                    print("invalid image option count, expected street_biome_version_directions: " + str(image_path))

            else:
                print("invalid image: " + str(image_path))

        # configure image data structures
        for damages in self.car_images.values():
            damages.sort(key=lambda x: x[0])

        for damages in self.house_images.values():
            damages.sort(key=lambda x: x[0])

    @staticmethod
    def find_closest(l, value):
        """
        Assumes myList is sorted. Returns closest value to myNumber.

        If two numbers are equally close, return the smallest number.
        """
        pos = bisect_left(l, value)
        if pos == 0:
            return l[0]
        if pos == len(l):
            return l[-1]
        before = l[pos - 1]
        after = l[pos]
        if after[0] - value[0] < value[0] - before[0]:
            return after
        else:
            return before

    def get_car(self, ang, version=0, damage=0):
        d, index = self.find_closest(self.car_images[version], (damage,))
        return self.pygame.transform.rotate(self.scaled_car_images[index], ang)

    def get_grass(self, biome=0, version=0):
        return self.scaled_images[self.grass_images[(biome, version)]]

    def get_house(self, biome=0, version=0, damage=0):
        d, index = self.find_closest(self.house_images[(biome, version)], (damage,))
        return self.scaled_images[index]

    def get_street(self, biome=0, version=0, north=False, east=False, south=False, west=False):
        directions = 0
        if north:
            directions += 8
        if east:
            directions += 4
        if south:
            directions += 2
        if west:
            directions += 1
        street_type = self.street_images[(biome, version)]
        if directions in street_type:
            return self.scaled_images[street_type[directions]]
        else:
            return self.scaled_images[street_type[0]]

    def biome_report(self):
        biome = 0
        biomes = []
        while True:
            grasses = 0
            while (biome, grasses) in self.grass_images:
                grasses += 1

            houses = 0
            while (biome, houses) in self.house_images:
                houses += 1

            streets = 0
            while (biome, streets) in self.street_images:
                streets += 1

            if grasses == 0 and houses == 0 and streets == 0:
                break

            biomes.append({"nr": biome, "grasses": grasses, "houses": houses, "streets": streets})
            biome += 1

        return biomes

    def car_report(self):
        cars = 0
        while cars in self.car_images:
            cars += 1
        return cars

    def scale(self, block_size, car_width, car_height):
        self.scaled_images = []
        for image in self.original_images:
            self.scaled_images.append(self.pygame.transform.scale(image, (block_size, block_size)))
        self.scaled_car_images = []
        for image in self.original_car_images:
            self.scaled_car_images.append(self.pygame.transform.scale(image, (car_width, car_height)))
