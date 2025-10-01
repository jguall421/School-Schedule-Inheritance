from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def display_transport_message(self):
        has_transport = "has" if self.gets_transportation else "doesn't have"

        return f"{self.name} {has_transport} transport privileges"

    # overrides the Student class's summary
    def summary(self):
        student_summary = super().summary()
        transport_message = self.display_transport_message()
        return "\n".join((student_summary,transport_message))

