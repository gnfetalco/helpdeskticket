# These are global variables that can be overwritten all throughout the program
counter = 2000
tic_count = []
staff_id = []
emp_name = []
emp_eadd = []
emp_desc = []
tic_stat = []
resp = []


# Clears the screen by printing blank lines 100 times
def cls():
    print("\n" * 100)


# This method is to add new entries to the global lists above
def staff_info(tic, id, name, eadd, desc, tics, res):
    global tic_count
    global staff_id
    global emp_name
    global emp_eadd
    global emp_desc
    global tic_stat
    global resp
    tic_count.append(tic)
    staff_id.append(id)
    emp_name.append(name)
    emp_eadd.append(eadd)
    emp_desc.append(desc)
    tic_stat.append(tics)
    resp.append(res)


class TicketStats:
    def ticketCounter(self):   # The method that shows the total numbers of all the tickets
        global counter
        global tic_stat
        resolved = tic_stat.count('Closed')
        solved = tic_stat.count('Open')
        cls()
        print("Tickets Created : ", counter - 2000)
        print("Tickets Resolved : ", resolved)
        print("Tickets To Solve : ", solved)
        input("\nPress any key to return to Main Menu")
        cls()
        menu.menu()

# Class that will handle re opening closed tickets and adding response to tickets
class ProblemHandler:
    def ticketSearch(self):
        global tic_count
        global staff_id
        global emp_name
        global emp_eadd
        global emp_desc
        global tic_stat
        global resp
        temp_count = []
        temp_staff = []
        for x, y in zip(tic_count, staff_id):
            temp_count.append(str(x))
            temp_staff.append(str(y))
        cls()
        print("Help Desk Ticketing System - Responding to a Ticket\n")
        i = input("Enter the 4 digit Ticket No : ")
        if i not in temp_count:
            print("Ticket no. does not exist!")
            self.ticketSearch()
        else:
            b = temp_count.index(i)
            print("\n")
            print("Ticket No. : " + temp_count[b])
            print("Ticket Owner : " + emp_name[b])
            print("Submitted by Staff ID : " + temp_staff[b])
            print("Contact E-mail : " + emp_eadd[b])
            print("Description of Issue : " + emp_desc[b])
            print("Response : " + resp[b])
            print("Ticket Status : " + tic_stat[b])
            print("\n")
            print("------------------------------------------------------")

        select = input("Is this the Ticket you want to Select Y/N : ")
        while True:
            if select.lower() == "y":
                b = temp_count.index(i)
                print("Enter your response to this ticket:")
                temp_res = input("=>")
                resp[b] = temp_res
                tic_stat[b] = "Closed"
                input("Response has been submitted")
            elif select.lower() == "n":
                self.ticketSearch()
            else:
                print("Please type in only Y or N")
                continue
            break

        answer = input("Do you have other tickets you need to respond? Y/N: ")
        while True:
            if answer.lower() == "y":
                self.ticketSearch()
            elif answer.lower() == "n":
                input("\nPress any key to return to Main Menu")
                cls()
                menu.menu()
            else:
                print("Please type in only Y or N")
                continue
            break

    def reOpen(self):
        global tic_count
        global staff_id
        global emp_name
        global emp_eadd
        global emp_desc
        global tic_stat
        global resp
        temp_count = []
        temp_staff = []
        for x, y in zip(tic_count, staff_id):
            temp_count.append(str(x))
            temp_staff.append(str(y))
        cls()
        print("Help Desk Ticketing System - Re-open resolved Tickets\n")
        i = input("Enter the 4 digit Ticket No : ")
        b = temp_count.index(i)
        if i not in temp_count:
            print("Ticket no. does not exist!")
            input("Type the correct ticket no.")
            self.ticketSearch()
        elif tic_stat[b] == "Open":
            print('Ticket is already "Open"')
            input("Press Enter and select another ticket no.")
            self.ticketSearch()
        else:
            print("\n")
            print("Ticket No. : " + temp_count[b])
            print("Ticket Owner : " + emp_name[b])
            print("Submitted by Staff ID : " + temp_staff[b])
            print("Contact E-mail : " + emp_eadd[b])
            print("Description of Issue : " + emp_desc[b])
            print("Response : " + resp[b])
            print("Ticket Status : " + tic_stat[b])
            print("\n")
            print("------------------------------------------------------")

        select = input("Is this the Ticket you want to Select Y/N : ")
        while True:
            if select.lower() == "y":
                resp[b] = "Not Yet Provided"
                tic_stat[b] = "Open"
                input("Ticket has been re-opened.")
                break
            elif select.lower() == "n":
                self.ticketSearch()
            else:
                print("Please type in only Y or N")
                continue
            break

        answer = input("Do you have other tickets you need to respond? Y/N: ")
        while True:
            if answer.lower() == "y":
                self.ticketSearch()
            elif answer.lower() == "n":
                input("\nPress any key to return to Main Menu")
                cls()
                menu.menu()
            else:
                print("Please type in only Y or N")
                continue
            break

# This class holds all methods relating to ticket creation
class Ticketing:
    def ticket(self):
        global counter
        cls()
        while True:
            i = (input("Enter your 5 digit staff id : "))
            if len(i) != 5:
                print("Enter a valid Staff ID")
                continue
            elif not i.isdigit():
                print("Enter a valid Staff ID")
                continue
            break
        id = int(i)
        name = (input("Enter your name : "))
        eadd = (input("Enter your email address : "))
        print("Enter the description of your problem below.")
        temp = str(
            input('If you require a new password type "Password Change"\nOtherwise, just type in your problem : '))
        if temp.lower() == "password change":
            pw = self.passChange(id, name)
            tics = "Closed"
            res = "User password changed to " + pw
            staff_info(counter, id, name, eadd, temp, tics, res)
            temp2 = input("Do you have another problem to submit? Y/N : ")
            while True:
                if temp2.lower() == "y":
                    ticket.ticket()
                elif temp2.lower() == "n":
                    menu.menu()
                else:
                    print("Please type in only Y or N")
                    continue
                break
        else:
            counter += 1
            print("Your ticket has been submitted to the queue")
            tics = "Open"
            temp3 = input("Do you want to leave a response to this ticket before exiting? Y/N : ")
            while True:
                if temp3.lower() == "y":
                    print("Type in below your response to this ticket.")
                    res = input("=>")
                    staff_info(counter, id, name, eadd, temp, tics, res)
                    break
                elif temp3.lower() == "n":
                    res = "Not Yet Provided"
                    staff_info(counter, id, name, eadd, temp, tics, res)
                    break
                else:
                    print("Please type in only Y or N")
                    continue
            temp2 = input("Do you have another problem to submit? Y/N : ")
            while True:
                if temp2.lower() == "y":
                    ticket.ticket()
                elif temp2.lower() == "n":
                    break
                else:
                    print("Please type in only Y or N")
                    continue

        input("\nPress any key to return to Main Menu")
        menu.menu()

    def passChange(self, id, name):   # Method that will generate a new password for the customer
        global counter
        counter += 1
        tempid = str(id)
        pw = tempid[:2] + name[:3]
        print("Your new Password is " + pw)
        return pw

    def showTickets(self):
        # I used zip() so i can pass through multiple list at the same time
        for a, b, c, d, e, f, g in zip(tic_count, staff_id, emp_name, emp_eadd, emp_desc, tic_stat, resp):
            print("\n")
            print("Ticket No. : " + str(a))
            print("Ticket Owner : " + c)
            print("Submitted by Staff ID : " + str(b))
            print("Contact E-mail : " + d)
            print("Description of Issue : " + e)
            print("Response : " + g)
            print("Ticket Status : " + f)
            print("\n")
            print("------------------------------------------------------")

        input("\nPress any key to return to Main Menu")
        cls()
        menu.menu()


# The Main Menu
class MainMenu:
    global counter

    # Main menu selections
    def menu(self):
        print('\n\nSelect from our Options')
        print('1: Submit helpdesk ticket')
        print('2: Show all tickets')
        print('3: Respond to ticket by number')
        print('4: Re-open resolved ticket')
        print('5: Display ticket stats')
        print('0: Exit')
        print('------------------------------\n')
        selection = input('Enter menu selection 0 - 5 : ')
        # Submit Help Desk Tickets
        if selection == "1":
            cls()
            ticket.ticket()
        # Shows all ticket that has been created
        elif selection == "2":
            cls()
            if counter == 2000:
                print("No Tickets submitted yet!")
                input("\nPress any key to continue...")
                menu.menu()
            else:
                ticket.showTickets()
        # Option to Respond to an open ticket
        elif selection == "3":
            cls()
            if counter == 2000:
                print("No Tickets submitted yet!")
                input("\nPress any key to continue...")
                menu.menu()
            else:
                ticSearch.ticketSearch()
        # Re-opening of a closed ticket
        elif selection == "4":
            cls()
            if counter == 2000:
                print("No Tickets submitted yet!")
                input("\nPress any key to continue...")
                menu.menu()
            else:
                ticSearch.reOpen()
        # Display the total amount of tickets
        elif selection == "5":
            cls()
            stats.ticketCounter()
        # Exit the program
        elif selection == "0":
            print("\nThank you for using the Help Desk Ticketing System")
            exit()
        elif selection == "":
            print("Invalid selection. Choose only from 1-5 or 0 to Exit")
            input("Press any key to continue...")
            cls()
            menu.menu()
        else:
            print("Invalid selection. Choose only from 1-5 or 0 to Exit")
            input("Press any key to continue...")
            cls()
            menu.menu()


print("Welcome to the Help Desk Ticketing System")
ticSearch = ProblemHandler()
stats = TicketStats()
ticket = Ticketing()
menu = MainMenu()
menu.menu()
