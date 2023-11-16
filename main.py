import group
import people


def main():
    andrew = people.Client('Andrew')
    alice = people.Student('Alice', andrew)
    eve = people.Client('Eve')
    jane = people.Student('Jane', eve)
    wn_20 = group.Group(20, 'Maths')
    wn_20.add_student(alice)
    wn_20.add_student(jane)
    print(wn_20.get_group_attendees())
    
    
if __name__ == "__main__":
    main()
