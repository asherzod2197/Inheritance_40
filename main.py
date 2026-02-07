# 40. Ta’til xarajatlari

class VacationExpense:
    def __init__(self, category, amount):
        self.category = category    # "Transport", "Ovqatlanish", "Mehmonxona" va h.k.
        self.amount = amount        # summasi ($)

    def get_cost(self):
        """Xarajat summasi"""
        return self.amount

    def __str__(self):
        return f"{self.category:16} | {self.amount:8.2f}$"


# -----------------------------------------------
# Voris sinflar (emoji va chiroyli format bilan)
# -----------------------------------------------

class TransportExpense(VacationExpense):
    def __str__(self):
        return f"✈️  {self.category:14} → {self.amount:7.2f}$"


class FoodExpense(VacationExpense):
    def __str__(self):
        return f"🍽️  {self.category:14} → {self.amount:7.2f}$"


# Qo‘shimcha kategoriyalar (foydali bo‘lishi mumkin)
class AccommodationExpense(VacationExpense):
    def __str__(self):
        return f"🏨  {self.category:14} → {self.amount:7.2f}$"


class EntertainmentExpense(VacationExpense):
    def __str__(self):
        return f"🎡  {self.category:14} → {self.amount:7.2f}$"


# --------------------------------------------------
# Ta’til xarajatlarini chiqarish
# --------------------------------------------------

def show_vacation_expenses(expenses):
    print("\n" + "═" * 60)
    print("       TA’TIL XARAJATLARI HISOBI       ".center(60))
    print("═" * 60)
    print("Xarajat turi                  Summa ($)")
    print("─" * 60)

    total = 0

    for exp in expenses:
        print(exp)
        total += exp.get_cost()

    print("─" * 60)
    print(f"JAMI TA’TIL XARAJATLARI:            {total:10.2f}$")
    print("═" * 60 + "\n")


# Test ma'lumotlari
xarajatlar = [
    TransportExpense("Aviachipta", 320.00),
    FoodExpense("Ovqatlanish (haftalik)", 180.50),
    AccommodationExpense("Mehmonxona (5 tun)", 480.00),
    EntertainmentExpense("Ekskursiyalar va kirish chiptalari", 95.00),
    TransportExpense("Mahalliy transport", 45.20),
    FoodExpense("Kofe va shirinliklar", 38.75),
]

show_vacation_expenses(xarajatlar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol xarajatlaringiz:\n")
misol_xarajatlar = [
    TransportExpense("Transport", 200),
    FoodExpense("Ovqatlanish", 100),
]

show_vacation_expenses(misol_xarajatlar)
