import json
import os
from datetime import datetime
from enum import Enum


class StudyField(Enum):
    MECHANICAL_ENGINEERING = "MECHANICAL_ENGINEERING"
    SOFTWARE_ENGINEERING = "SOFTWARE_ENGINEERING"
    FOOD_TECHNOLOGY = "FOOD_TECHNOLOGY"
    URBANISM_ARCHITECTURE = "URBANISM_ARCHITECTURE"
    VETERINARY_MEDICINE = "VETERINARY_MEDICINE"


class Student:
    
    
    def __init__(self, email, first_name, last_name, 
                 enrollment_date, birth_date):
        self.__email = email
        self.__first_name = first_name
        self.__last_name = last_name
        self.__enrollment_date = enrollment_date
        self.__birth_date = birth_date
        self.__is_graduated = False
        self.__graduation_date = None
    
    
    @property
    def email(self):
        return self.__email
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"
    
    @property
    def enrollment_date(self):
        return self.__enrollment_date
    
    @property
    def birth_date(self):
        return self.__birth_date
    
    @property
    def is_graduated(self):
        return self.__is_graduated
    
    @property
    def graduation_date(self):
        return self.__graduation_date
    
    
    def graduate(self, graduation_date):
        """Marchează studentul ca absolvent."""
        if self.__is_graduated:
            raise ValueError(
                f"Student {self.__email} is already graduated"
            )
        
        self.__is_graduated = True
        self.__graduation_date = graduation_date
    
    
    def to_dict(self):
        """Convertește la dicționar pentru salvare."""
        return {
            'email': self.__email,
            'first_name': self.__first_name,
            'last_name': self.__last_name,
            'enrollment_date': self.__enrollment_date,
            'birth_date': self.__birth_date,
            'is_graduated': self.__is_graduated,
            'graduation_date': self.__graduation_date
        }
    
    @classmethod
    def from_dict(cls, data):
        """Creează Student din dicționar."""
        student = cls(
            data['email'],
            data['first_name'],
            data['last_name'],
            data['enrollment_date'],
            data['birth_date']
        )
        if data.get('is_graduated'):
            student._Student__is_graduated = True
            student._Student__graduation_date = data.get('graduation_date')
        return student
    
    def __str__(self):
        status = "Graduate" if self.__is_graduated else "Enrolled"
        return (f"{self.full_name} ({self.__email}) - {status}")


class Faculty:
    
    
    def __init__(self, name, abbreviation, field):
        self.__name = name
        self.__abbreviation = abbreviation
        
        # Validare field
        if isinstance(field, str):
            try:
                self.__field = StudyField[field]
            except KeyError:
                raise ValueError(f"Invalid study field: {field}")
        elif isinstance(field, StudyField):
            self.__field = field
        else:
            raise TypeError("Field must be string or StudyField enum")
        
        # Colecții private
        self.__enrolled_students = {}  # {email: Student}
        self.__graduated_students = {}  # {email: Student}
    
    
    @property
    def name(self):
        return self.__name
    
    @property
    def abbreviation(self):
        return self.__abbreviation
    
    @property
    def field(self):
        return self.__field
    
    
    def get_enrolled_students(self):
        """Returnează copie a listei de studenți înrolați."""
        return list(self.__enrolled_students.values())
    
    def get_graduated_students(self):
        """Returnează copie a listei de absolvenți."""
        return list(self.__graduated_students.values())
    
    def get_all_students(self):
        """Returnează toți studenții."""
        return (list(self.__enrolled_students.values()) + 
                list(self.__graduated_students.values()))
    
    def get_student_count(self):
        """Număr studenți activi."""
        return len(self.__enrolled_students)
    
    def get_graduate_count(self):
        """Număr absolvenți."""
        return len(self.__graduated_students)
    
    
    def enroll_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Must be a Student object")
        
        if student.email in self.__enrolled_students:
            raise ValueError(
                f"Student {student.email} is already enrolled in {self.__name}"
            )
        
        if student.email in self.__graduated_students:
            raise ValueError(
                f"Student {student.email} already graduated from {self.__name}"
            )
        
        if student.is_graduated:
            raise ValueError("Cannot enroll a graduated student")
        
        self.__enrolled_students[student.email] = student
    
    def graduate_student(self, email, graduation_date=None):
        if email not in self.__enrolled_students:
            raise ValueError(
                f"Cannot graduate student: {email} (student not enrolled in {self.__name})"
            )
        
        if graduation_date is None:
            graduation_date = datetime.now().strftime("%Y-%m-%d")
        
        student = self.__enrolled_students[email]
        student.graduate(graduation_date)
        
        # Mutare din enrolled în graduated
        self.__graduated_students[email] = student
        del self.__enrolled_students[email]
    
    def has_student(self, email):
        return (email in self.__enrolled_students or 
                email in self.__graduated_students)
    
    def find_student(self, email):
        if email in self.__enrolled_students:
            return self.__enrolled_students[email]
        if email in self.__graduated_students:
            return self.__graduated_students[email]
        return None
    
    
    def to_dict(self):
        return {
            'name': self.__name,
            'abbreviation': self.__abbreviation,
            'field': self.__field.name,
            'enrolled_students': [
                s.to_dict() for s in self.__enrolled_students.values()
            ],
            'graduated_students': [
                s.to_dict() for s in self.__graduated_students.values()
            ]
        }
    
    @classmethod
    def from_dict(cls, data):
        faculty = cls(
            data['name'],
            data['abbreviation'],
            data['field']
        )
        
        # Restaurare studenți înrolați
        for student_data in data.get('enrolled_students', []):
            student = Student.from_dict(student_data)
            faculty._Faculty__enrolled_students[student.email] = student
        
        # Restaurare absolvenți
        for student_data in data.get('graduated_students', []):
            student = Student.from_dict(student_data)
            faculty._Faculty__graduated_students[student.email] = student
        
        return faculty
    
    def __str__(self):
        return (f"{self.__name} ({self.__abbreviation}) - "
                f"{self.__field.name} | "
                f"Students: {self.get_student_count()}, "
                f"Graduates: {self.get_graduate_count()}")


class University:
    
    def __init__(self, name="Technical University of Moldova"):
        self.__name = name
        self.__faculties = {}  # {abbreviation: Faculty}
    
    @property
    def name(self):
        return self.__name
    
    def get_faculties(self):
        return list(self.__faculties.values())
    
    def get_faculty_count(self):
        return len(self.__faculties)
    
    def add_faculty(self, faculty):
        if not isinstance(faculty, Faculty):
            raise TypeError("Must be a Faculty object")
        
        if faculty.abbreviation in self.__faculties:
            raise ValueError(
                f"Faculty {faculty.abbreviation} already exists"
            )
        
        self.__faculties[faculty.abbreviation] = faculty
    
    def find_faculty(self, abbreviation):
        return self.__faculties.get(abbreviation)
    
    def find_faculties_by_field(self, field):
        if isinstance(field, str):
            try:
                field = StudyField[field]
            except KeyError:
                return []
        
        return [
            f for f in self.__faculties.values() 
            if f.field == field
        ]
    
    def find_student_faculty(self, email):
        for faculty in self.__faculties.values():
            if faculty.has_student(email):
                return faculty
        return None
    
    def to_dict(self):
        return {
            'name': self.__name,
            'faculties': [
                f.to_dict() for f in self.__faculties.values()
            ]
        }
    
    @classmethod
    def from_dict(cls, data):
#Creează University din dicționar.
        university = cls(data.get('name', 'Technical University of Moldova'))
        
        for faculty_data in data.get('faculties', []):
            faculty = Faculty.from_dict(faculty_data)
            university._University__faculties[faculty.abbreviation] = faculty
        
        return university



class SaveManager:
    
    
    def __init__(self, filename="university_data.json"):
        self.__filename = filename
    
    def save(self, university):
        """Salvează starea universității în fișier JSON."""
        try:
            data = university.to_dict()
            with open(self.__filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load(self):
        """Încarcă starea universității din fișier JSON."""
        if not os.path.exists(self.__filename):
            return None
        
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return University.from_dict(data)
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def file_exists(self):
        return os.path.exists(self.__filename)



class UniversityManager:
    
    
    def __init__(self, save_manager=None, eager_save=False):
        self.__university = University()
        self.__save_manager = save_manager
        
        if self.__save_manager:
            loaded = self.__save_manager.load()
            if loaded:
                self.__university = loaded
            elif eager_save:
                self._persist()
    
    @property
    def university(self):
        return self.__university
    
    
    def create_faculty(self, name, abbreviation, field):
        faculty = Faculty(name, abbreviation, field)
        self.__university.add_faculty(faculty)
        self._persist()
        return faculty
    
    def get_faculties(self):
        return self.__university.get_faculties()
    
    def get_faculties_by_field(self, field):
        return self.__university.find_faculties_by_field(field)
    
    def find_faculty(self, abbreviation):
        return self.__university.find_faculty(abbreviation)
    
    
    def enroll_student(self, faculty_abbr, email, first_name, 
                       last_name, birth_date):
        faculty = self.__university.find_faculty(faculty_abbr)
        if not faculty:
            raise ValueError(f"Faculty {faculty_abbr} not found")
        
        enrollment_date = datetime.now().strftime("%Y-%m-%d")
        student = Student(email, first_name, last_name, 
                         enrollment_date, birth_date)
        
        faculty.enroll_student(student)
        self._persist()
        return student
    
    def graduate_student(self, faculty_abbr, email):
        faculty = self.__university.find_faculty(faculty_abbr)
        if not faculty:
            raise ValueError(f"Faculty {faculty_abbr} not found")
        
        graduation_date = datetime.now().strftime("%Y-%m-%d")
        faculty.graduate_student(email, graduation_date)
        self._persist()
    
    def check_student_belongs_to_faculty(self, faculty_abbr, email):
        faculty = self.__university.find_faculty(faculty_abbr)
        if not faculty:
            return False
        return faculty.has_student(email)
    
    def find_student_faculty(self, email):
        return self.__university.find_student_faculty(email)


    def _persist(self):
#Salveaza starea daca SaveManager este disponibil.
        if self.__save_manager:
            self.__save_manager.save(self.__university)


class CLI:
    
    def __init__(self, manager):
        self.__manager = manager
    
    def run(self):
        """Pornește loop-ul principal."""
        print("=" * 60)
        print("Student Management System - Technical University of Moldova")
        print("=" * 60)
        print()
        
        while True:
            self._display_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if choice == 'q':
                print("\nGoodbye!")
                break
            
            self._handle_choice(choice)
    
    def _display_menu(self):
        print("\n" + "=" * 60)
        print("MAIN MENU")
        print("=" * 60)
        print("\nGENERAL OPERATIONS:")
        print("  g - General operations")
        print("\nFACULTY OPERATIONS:")
        print("  f - Faculty operations")
        print("\nOTHER:")
        print("  q - Quit")
    
    def _display_general_menu(self):
        print("\n" + "-" * 60)
        print("GENERAL OPERATIONS")
        print("-" * 60)
        print("1. Create a new faculty")
        print("2. Search what faculty a student belongs to")
        print("3. Display all university faculties")
        print("4. Display faculties by field")
        print("b. Back to main menu")
    
    def _display_faculty_menu(self):
        print("\n" + "-" * 60)
        print("FACULTY OPERATIONS")
        print("-" * 60)
        print("1. Enroll student to faculty")
        print("2. Graduate student from faculty")
        print("3. Display enrolled students")
        print("4. Display graduates")
        print("5. Check if student belongs to faculty")
        print("b. Back to main menu")
    
    def _handle_choice(self, choice):
        try:
            if choice == 'g':
                self._handle_general_operations()
            elif choice == 'f':
                self._handle_faculty_operations()
            else:
                print(f"\nInvalid choice: {choice}")
        except Exception as e:
            print(f"\nError: {e}")
    
    def _handle_general_operations(self):
        while True:
            self._display_general_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if choice == 'b':
                break
            
            try:
                if choice == '1':
                    self._create_faculty()
                elif choice == '2':
                    self._search_student_faculty()
                elif choice == '3':
                    self._display_all_faculties()
                elif choice == '4':
                    self._display_faculties_by_field()
                else:
                    print(f"\nInvalid choice: {choice}")
            except Exception as e:
                print(f"\nError: {e}")
    
    def _handle_faculty_operations(self):
        # Selectare facultate
        abbr = input("\nEnter faculty abbreviation: ").strip().upper()
        faculty = self.__manager.find_faculty(abbr)
        
        if not faculty:
            print(f"\nFaculty {abbr} not found!")
            return
        
        print(f"\nWorking with: {faculty}")
        
        while True:
            self._display_faculty_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if choice == 'b':
                break
            
            try:
                if choice == '1':
                    self._enroll_student(abbr)
                elif choice == '2':
                    self._graduate_student(abbr)
                elif choice == '3':
                    self._display_enrolled_students(faculty)
                elif choice == '4':
                    self._display_graduates(faculty)
                elif choice == '5':
                    self._check_student_belongs(abbr)
                else:
                    print(f"\nInvalid choice: {choice}")
            except Exception as e:
                print(f"\nError: {e}")
    
    
    def _create_faculty(self):
        print("\n--- Create New Faculty ---")
        name = input("Faculty name: ").strip()
        abbr = input("Abbreviation: ").strip().upper()
        
        print("\nAvailable fields:")
        for i, field in enumerate(StudyField, 1):
            print(f"  {i}. {field.name}")
        
        field_choice = input("Choose field (number): ").strip()
        try:
            field_idx = int(field_choice) - 1
            field = list(StudyField)[field_idx]
        except (ValueError, IndexError):
            print("Invalid field choice!")
            return
        
        faculty = self.__manager.create_faculty(name, abbr, field)
        print(f"\n✓ Faculty created: {faculty}")
    
    def _search_student_faculty(self):
        print("\n--- Search Student Faculty ---")
        email = input("Student email: ").strip()
        
        faculty = self.__manager.find_student_faculty(email)
        if faculty:
            print(f"\n✓ Student {email} belongs to: {faculty.name}")
        else:
            print(f"\n✗ Student {email} not found in any faculty")
    
    def _display_all_faculties(self):
        print("\n--- All Faculties ---")
        faculties = self.__manager.get_faculties()
        
        if not faculties:
            print("No faculties found.")
            return
        
        for faculty in faculties:
            print(f"  • {faculty}")
    
    def _display_faculties_by_field(self):
        print("\n--- Faculties by Field ---")
        print("\nAvailable fields:")
        for i, field in enumerate(StudyField, 1):
            print(f"  {i}. {field.name}")
        
        field_choice = input("Choose field (number): ").strip()
        try:
            field_idx = int(field_choice) - 1
            field = list(StudyField)[field_idx]
        except (ValueError, IndexError):
            print("Invalid field choice!")
            return
        
        faculties = self.__manager.get_faculties_by_field(field)
        
        if not faculties:
            print(f"\nNo faculties found for {field.name}")
            return
        
        print(f"\nFaculties in {field.name}:")
        for faculty in faculties:
            print(f"  • {faculty}")
    
    
    def _enroll_student(self, faculty_abbr):
        """Înrolează un student."""
        print("\n--- Enroll Student ---")
        email = input("Email: ").strip()
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        birth_date = input("Birth date (YYYY-MM-DD): ").strip()
        
        student = self.__manager.enroll_student(
            faculty_abbr, email, first_name, last_name, birth_date
        )
        print(f"\n✓ Student enrolled: {student}")
    
    def _graduate_student(self, faculty_abbr):
        """Absolve un student."""
        print("\n--- Graduate Student ---")
        email = input("Student email: ").strip()
        
        self.__manager.graduate_student(faculty_abbr, email)
        print(f"\n✓ Student {email} graduated successfully")
    
    def _display_enrolled_students(self, faculty):
        print("\n--- Enrolled Students ---")
        students = faculty.get_enrolled_students()
        
        if not students:
            print("No enrolled students.")
            return
        
        for student in students:
            print(f"  • {student}")
    
    def _display_graduates(self, faculty):
        """Afișează absolvenți."""
        print("\n--- Graduates ---")
        students = faculty.get_graduated_students()
        
        if not students:
            print("No graduates.")
            return
        
        for student in students:
            grad_date = student.graduation_date or "N/A"
            print(f"  • {student.full_name} ({student.email}) - "
                  f"Graduated: {grad_date}")
    
    def _check_student_belongs(self, faculty_abbr):
        print("\n--- Check Student Membership ---")
        email = input("Student email: ").strip()
        
        belongs = self.__manager.check_student_belongs_to_faculty(
            faculty_abbr, email
        )
        
        if belongs:
            print(f"\n✓ Student {email} belongs to this faculty")
        else:
            print(f"\n✗ Student {email} does NOT belong to this faculty")



def main():
    save_manager = SaveManager("university_data.json")
    
    
    manager = UniversityManager(save_manager, eager_save=False)
    
    if save_manager.file_exists():
        print("✓ Previous session data loaded successfully!")
    else:
        print("⚠ No previous data found. Starting fresh.")
    
    cli = CLI(manager)
    cli.run()


if __name__ == "__main__":
    main()