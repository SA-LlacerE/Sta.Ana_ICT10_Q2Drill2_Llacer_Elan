from pyscript import document

# Club members
grade7 = {'Amor Rita', 'Cap Jornales', 'Jobe Bellingham'}
grade8 = {'Colleen Hoover', 'Nella Rose', 'Sean Lee', 'Epiphany Stone'}
grade9 = {'Stephanie Garber', 'Brian Nayve', 'Conrad Fisher'}
grade10 = {'Kiehla Abuiza', 'Jan Lee', 'Hariette Mae'}

# Union of all grade sets
members = grade7 | grade8 | grade9 | grade10


def result_checker(e):
    global members

    # Clear the previous output
    document.getElementById('output').innerHTML = " "

    # Read the text boxes
    first = document.getElementById('first_name').value.strip()
    last = document.getElementById('last_name').value.strip()
    full_name = f"{first} {last}".strip()

    # Put the new member in a set
    new_member = {full_name} - {""}

    members = members | new_member

    # Display with f-string
    member_list = "<br>".join(sorted(members))
    document.getElementById('output').innerHTML = f"""
        <h4>All Members:</h4>
        <p>{member_list}</p>
        <h4>Total Members: {len(members)}</h4>
    """

    # Clear the text boxes for the next entry
    document.getElementById('first_name').value = ""
    document.getElementById('last_name').value = ""