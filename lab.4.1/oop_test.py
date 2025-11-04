class Display:
    def __init__(self, width, height, ppi, model):
        self.__width = width
        self.__height = height
        self.__ppi = ppi
        self.__model = model

    def compare_size(self, other):
        area_self = self.__width * self.__height
        area_other = other.__width * other.__height

        if area_self > area_other:
            print(f"{self.__model} is larger than {other.__model}")
        elif area_self < area_other:
            print(f"{other.__model} is larger than {self.__model}")
        else:
            print(f"{self.__model} and {other.__model} are the same size")

    def compare_sharpness(self, other):
        if self.__ppi > other.__ppi:
            print(f"{self.__model} is sharper than {other.__model}")
        elif self.__ppi < other.__ppi:
            print(f"{other.__model} is sharper than {self.__model}")
        else:
            print(f"{self.__model} and {other.__model} have equal sharpness")

    def compare_with_monitor(self, other):
        self.compare_size(other)
        self.compare_sharpness(other)


if __name__ == "__main__":
    d1 = Display(1920, 1080, 100, "Dell ")
    d2 = Display(2560, 1440, 120, "Samsung ")
    d3 = Display(1920, 1080, 100, "LG ")

    d1.compare_with_monitor(d2)
    d2.compare_with_monitor(d3)
