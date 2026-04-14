class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = 0
        
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                c = 0
            else:
                students.append(students[0])
                students.pop(0)
                c +=1
            if c > len(students):
                return len(students)
        return 0