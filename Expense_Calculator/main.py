
from js import document, Object
from pyscript import window, display


def addExpense(event):
    print("addExpense")
    dateId = document.getElementById('date')
    categoryId = document.getElementById('category')
    nameId = document.getElementById('name')
    amountId = document.getElementById('amount')

    date = dateId.value
    category = categoryId.value
    name = nameId.value
    amount = amountId.value

    if date and amount and category :

        if name == '':
            name = category

        expense = {'date': date, 'category': category, 'name': name, 'amount': amount}
        expenses.append(expense)
        renderExpenses()

    dateId.value = ''
    categoryId.value = 'Food'
    nameId.value = ''
    expenseNameDiv = document.getElementById('expenseNameDiv')
    expenseNameDiv.style.display = 'none'
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

    totalAmount = 0

    for i, expense in enumerate(expenses):
        print("RENDER exp ",expense)
        print("RENDER i ",i)
        row = document.createElement('tr')
        row.id = f'expense-{i}'
        print("RENDER row ",row.id)

        dateCell = document.createElement('td')
        dateCell.textContent = expense['date']
        categoryCell = document.createElement('td')
        categoryCell.textContent = expense['category']
        nameCell = document.createElement('td')
        nameCell.textContent = expense['name']
        amountCell = document.createElement('td')
        amountCell.textContent = expense['amount']
        totalAmount += float(expense['amount'])
        actionCell = document.createElement('td')
        deleteButton = document.createElement('button')
        deleteButton.textContent = 'Delete'
        deleteButton.onclick = deleteExpense
        # deleteButton.setAttribute('onclick', f'deleteExpense({i})')
        actionCell.appendChild(deleteButton)

        row.appendChild(dateCell)
        row.appendChild(categoryCell)
        row.appendChild(nameCell)
        row.appendChild(amountCell)
        row.appendChild(actionCell)
        tableBody.appendChild(row)

    totalAmountDiv = document.getElementById('totalAmount')
    totalAmountDiv.textContent = totalAmount
    print("RENDER totalAmount ",totalAmount)

expenses = []

# Initial render
renderExpenses()



