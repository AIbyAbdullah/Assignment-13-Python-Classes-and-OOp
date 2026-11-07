'''
Pillar 1: Encapsulation
Q1. Student Result Manager | Beginner
Create a Student class with a public name, protected _marks, and private __grade attributes. Initialize the
student through a constructor. Implement set_marks(marks), which accepts only values from 0 to 100, along with
get_marks() and get_grade(). Assign grade A for 80 to 100, B for 60 to 79, C for 40 to 59, and F below 40.
Demonstrate both a valid and an invalid marks update. Extension: Attempt direct access to __grade and explain
the result.
'''

class Student:
    def __init__(self, name, marks):
        self.name = name          # public
        self._marks = None       # protected
        self.__grade = ""         # private
        self.set_marks(marks)

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
            if marks >= 80:
                self.__grade = "A"
            elif marks >= 60:
                self.__grade = "B"
            elif marks >= 40:
                self.__grade = "C"
            else:
                self.__grade = "F"
        else:
            print(f"Invalid marks ({marks})! 0-100 hi do")

    def get_marks(self):
        return self._marks

    def get_grade(self):
        return self.__grade

# --- 2 Objects Demo ---
print("--- Valid Demo ---")
s1 = Student("Ali", 85)
print(f"{s1.name} -> Marks: {s1.get_marks()}, Grade: {s1.get_grade()}")

s2 = Student("Sara", 30)
print(f"{s2.name} -> Marks: {s2.get_marks()}, Grade: {s2.get_grade()}")

# Valid update
print("\n--- Valid Update ---")
s1.set_marks(65)
print(f"After update: {s1.name} -> Marks: {s1.get_marks()}, Grade: {s1.get_grade()}")

# Invalid update
print("\n--- Invalid Update ---")
s1.set_marks(200)
print(f"After invalid try, marks still: {s1.get_marks()}")

# --- Extension: Direct Access Attempt ---
print("\n--- Direct access to __grade (Extension) ---")
try:
    print(s1.__grade) # Yahan error ayega
except AttributeError as e:
    print(f"Error Aya: {e}")
    print("Wajah: __grade private hai. Python isko _Student__grade bana deta hai (Name Mangling), is liye direct access nahi hota.")

print("\nSahi tarika hamesha get se hai:", s1.get_grade())