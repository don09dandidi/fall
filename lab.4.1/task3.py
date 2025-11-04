from oop_test import Display

class Assistant:
    def __init__(self, assistant_name):
        self.assistant_name = assistant_name
        self.assigned_displays = []

    def assign_display(self, display):
        self.assigned_displays.append(display)

    def assist(self):
        for i in range(len(self.assigned_displays) - 1):
            d1 = self.assigned_displays[i]
            d2 = self.assigned_displays[i+1]
            print(d1.compare_with_monitor(d2))

    def buy_display(self, display):
        if display in self.assigned_displays:
            self.assigned_displays.remove(display)
            return display
        else:
            return None


if __name__ == "__main__":
    d1 = Display(1920, 1080, 100, "Dell")
    d2 = Display(2560, 1440, 120, "LG")
    d3 = Display(1920, 1080, 150, "Samsung")

    assistant = Assistant("techGuru")
    assistant.assign_display(d1)
    assistant.assign_display(d2)
    assistant.assign_display(d3)
    assistant.assist()
