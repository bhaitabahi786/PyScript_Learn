
from js import document, Object
from pyscript import window, display



def addExpense(event):
    print("addExpense")
    nameId = document.getElementById('name')
    amountId = document.getElementById('amount')
    name = nameId.value
    amount = amountId.value
    if name and amount:
        expense = {'name': name, 'amount': amount}
        expenses.append(expense)
        renderExpenses()

    nameId.value = ''
    amountId.value = ''

def deleteExpense(e):
    index = e.target.parentNode.parentNode.id.split('-')[1]
    # print("deleteExpense index ",index)
    # print("deleteExpense expenses ",expenses)
    # print("deleteExpense  ",index)
    expenses.pop(int(index))
    renderExpenses()
    # if int(index) < len(expenses):
    #     expenses.pop(index)
    #     renderExpenses()

def renderExpenses():
    tableBody = document.getElementById('expenseTableBody')
    tableBody.innerHTML = ''
    for i, expense in enumerate(expenses):
        print("RENDER exp ",expense)
        print("RENDER i ",i)
        row = document.createElement('tr')
        row.id = f'expense-{i}'
        print("RENDER row ",row.id)
        nameCell = document.createElement('td')
        nameCell.textContent = expense['name']
        amountCell = document.createElement('td')
        amountCell.textContent = expense['amount']
        actionCell = document.createElement('td')
        deleteButton = document.createElement('button')
        deleteButton.textContent = 'Delete'
        deleteButton.onclick = deleteExpense
        # deleteButton.setAttribute('onclick', f'deleteExpense({i})')
        actionCell.appendChild(deleteButton)
        row.appendChild(nameCell)
        row.appendChild(amountCell)
        row.appendChild(actionCell)
        tableBody.appendChild(row)

expenses = []

# Initial render
renderExpenses()



