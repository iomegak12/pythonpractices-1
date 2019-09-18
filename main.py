import services
import models

fileName = './data/customers.json'
customerService = services.CustomerService(fileName)
customers = customerService.getCustomers()

for customer in customers:
    print('{}, {}, {}'.format(
        customer.id, customer.name, customer.status))

filteredCustomers = customerService.getCustomersByName('old')

for filteredCustomer in filteredCustomers: print(filteredCustomer.name)