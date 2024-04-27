
from js import document, Object, localStorage
from pyscript import window, display
import json


def addExpense(event):
    
    ExpIdCheck = []
    
    print("addExpense")
    dateId = document.getElementById('date')
    categoryId = document.getElementById('category')
    nameId = document.getElementById('name')
    amountId = document.getElementById('amount')

    date = dateId.value
    category = categoryId.value
    name = nameId.value
    amount = amountId.value

    keyAdd = Object.keys(localStorage)
    
    keyAdd.sort()
    for i in keyAdd:
        id = i.split('-')[1]
        ExpIdCheck.append(int(id))
        
    if len(ExpIdCheck) == 0:
        ExpId = 0
    else:
        ExpId = max(ExpIdCheck) + 1

    if date and amount and category :
        if name == '':
            name = category
        # expense = f'{{"date": {date}, "category": {category}, "name": {name}, "amount": {amount}}}'
        expense = f'{{"date": "{date}", "category": "{category}", "name": "{name}", "amount": "{amount}"}}'
        localStorage.setItem(f'expense-{ExpId}', expense)
        print("addExp local storage ",expense)
        
        renderExpenses()
        ExpId += 1


    dateId.value = ''
    categoryId.value = 'Food'
    nameId.value = ''
    expenseNameDiv = document.getElementById('expenseNameDiv')
    expenseNameDiv.style.display = 'none'
    amountId.value = ''

def deleteExpense(e):
    index = e.target.parentNode.parentNode.id.split('-')[1]
    indexLocal = e.target.parentNode.parentNode.id
    
    localStorage.removeItem(indexLocal)

    print("deleteExp local storage " ,indexLocal)
    # localStorage.clear()
    renderExpenses()
    

def renderExpenses():
    tableBody = document.getElementById('expenseTableBody')
    tableBody.innerHTML = ''

    totalAmount = 0

    keys = Object.keys(localStorage)
    print("RENDER keys ",keys)
    print("RENDER keys ",len(keys))

    # value to sort the keys
    keys.sort()
    print("RENDER keys after sort ",keys)

    for i in keys:
        id = i.split('-')[1]
        expense = localStorage.getItem(f'expense-{id}')
        print("RENDER local expense ", expense)
        print("RENDER i ",i)

        if expense != None:
            
            row = document.createElement('tr')
            row.id = f'expense-{id}'
            
            expenseId = json.loads(expense)

            dateCell = document.createElement('td')
            dateCell.textContent = expenseId['date']

            categoryCell = document.createElement('td')
            categoryCell.textContent = expenseId['category']
            nameCell = document.createElement('td')
            nameCell.textContent = expenseId['name']
            amountCell = document.createElement('td')
            amountCell.textContent = expenseId['amount']
            totalAmount += float(expenseId['amount'])
            actionCell = document.createElement('td')
            deleteButton = document.createElement('button')
            deleteButton.textContent = 'Delete'
            deleteButton.className = 'btn btn-danger'
            deleteButton.onclick = deleteExpense
            actionCell.appendChild(deleteButton)

            row.appendChild(dateCell)
            row.appendChild(categoryCell)
            row.appendChild(nameCell)
            row.appendChild(amountCell)
            row.appendChild(actionCell)
            tableBody.appendChild(row)

        else :
            print(f"RENDER local expense is None for expense-{i}")

    totalAmountDiv = document.getElementById('totalAmount')
    totalAmountDiv.textContent = totalAmount
    print("RENDER totalAmount ",totalAmount)

expenses = []

# Initial render
renderExpenses()



