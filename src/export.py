import csv

class Transactions:

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Category', 'Name', 'Amount'])  # Cabeçalho do arquivo CSV

            for category, transactions in self.items.items():
                for transaction in transactions:
                    name = transaction['name']
                    amount = transaction['amount']
                    writer.writerow([category, name, amount])


transactions = Transactions()

transactions.save_to_csv('transactions.csv')
