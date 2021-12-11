
class Expenses:

    def __init__(self):
        self.expense_list = [2200, 2350, 2600, 2130, 2190]

    def feb_jan(self):
        """ 1. In Feb, how many dollars you spent extra 
            compare to January?"""
        return self.expense_list[1] - self.expense_list[0]

    def first_quarter(self):
        """ 2. Find out your total expense in first 
            quarter (first three months) of the year."""
        total = 0

        for mouth in self.expense_list[:3]:
            total += mouth
        return total

    def find_exacly(self):
        """ 3. Find out if you spent exactly 2000 
            dollars in any month """
        return 2000 in self.expense_list

    def june_update(self):
        """ 4. June month just finished and your expense is 1980 dollar. 
            Add this item to our monthly expense list """
        self.expense_list.append(1980)
        return self.expense_list

    def refound(self):
        """ 5. You returned an item that you bought 
        in a month of April and got a refund of 200$. 
        Make a correction to your monthly expense list
        based on this"""

        self.expense_list[3] = self.expense_list[3] - 200
        return self.expense_list


if __name__ == '__main__':
    expense = Expenses()
    print(expense.feb_jan())
    print(expense.first_quarter())
    print(expense.find_exacly())
    print(expense.june_update())
    print(expense.refound())
