"""People Popper."""
import sys


def main():
    """People Popper."""
    # All people.
    people = list(range(1, int(sys.argv[1]) + 1))

    # Start from person 1.
    person = 1

    # Until there is 1 person standing.
    while len(people) > 1:
        # If the highest numbered person has the knife.
        if person == people[-1]:
            # They kill the lowest numbered person.
            print(f"{person} kills {people.pop(0)}", end="")

            # Then give the knife to the new lowest numbered person
            person = people[0]

        # If the second highest numbered person has the knife.
        elif person == people[-2]:
            # They kill the highest numbered person.
            print(f"{person} kills {people.pop(-1)}", end="")

            # Then give the knife to the lowest numbered person.
            person = people[0]

        # Otherwise.
        else:
            # Kill the next person
            print(f"{person} kills {people.pop(people.index(person)+1)}", end="")

            # Then give the knife to the new next person.
            person = people[people.index(person) + 1]

        print(f" ({len(people)} people still alive)")

    print(f"\nPerson {person} is the last one standing!")


if __name__ == "__main__":
    main()
