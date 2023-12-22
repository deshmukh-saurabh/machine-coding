from swiggy.utils.utility import distanceBetween
class RestaurantDisplayManager:
	def show(self,restaurants,customer,radius):
		restaurantListToDisplay =[]
		#find restaurants where distanceBetween(customer.getLocation(), restaurant.getLocation()) <= radius
		for restaurant in restaurants:
			if distanceBetween(customer.getLocation(), restaurant.getLocation()) <= radius:
				restaurantListToDisplay.append(restaurant)

		return restaurantListToDisplay