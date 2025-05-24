class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} уже открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Rating of {self.restaurant_name} Рейтинг лучших блюд  {self.rating}")


# Создание экземпляра newRestaurant
newRestaurant = Restaurant("Токио сити", "Италянский")

# Вывод атрибутов по отдельности
print("Название ресторана:", newRestaurant.restaurant_name)
print("Тип кухни:", newRestaurant.cuisine_type)

# Вызов методов
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

# Создание трех разных экземпляров и вызов метода describe_restaurant() для каждого
restaurant1 = Restaurant("Бурито", "Мексиканский")
restaurant2 = Restaurant("Святая корова", "индинский")
restaurant3 = Restaurant("Суши вок", "Японский")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Обновление рейтинга ресторана
newRestaurant.update_rating(4.5)
