from aloe import step, world
from aloe_webdriver.util import find_field_by_id, find_any_field, find_field_by_value
from aloe_webdriver import TEXT_FIELDS
from selenium.common.exceptions import NoSuchElementException
from booking.models import Booking, Place, BookTime, Building, date_range
from user.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.test import Client
from django.core.management import call_command
from datetime import date, datetime, timedelta
from dateutil import parser

@step(r'I type in "(.*)" to "(.*)"')
def fill_bootstrap_field(step, text, field):
	words_list = field.lower().split()
	words_list.insert(0, "id")
	id_field = "_".join(words_list)
	date_field = find_any_field(world.browser, TEXT_FIELDS, id_field)
	date_field.send_keys(text)


@step(r'I type in "(.*)" to id "(.*)"')
def fill_bootstrap_field(step, text, id_field):
	date_field = find_any_field(world.browser, TEXT_FIELDS, id_field)
	date_field.send_keys(text)


@step(r'I click on an element with id of "(.*)"')
def click_on_element_by_id(step, id):
	try:
		elem = world.browser.find_element_by_id(id)
	except NoSuchElementException:
		raise AssertionError("Element with ID '{}' not found.".format(id))
	elem.click()


@step(r'I click on an element "(.*)" called "(.*)"')
def click_on_element_by_value(step, value, typeelement):
	try:
		text = find_field_by_value(world.browser, typeelement, elementtext)
	except NoSuchElementException:
		raise AssertionError("Element not found.")
	text.click()


@step(r'I register the user "(.*)" with the password "(.*)" and registration number "(.*)"')
def register_user(step, username, password,registration_number):
	user = UserProfile()
	user.user = User()				
	user.registration_number = registration_number	
	user.user.email = username
	user.user.username = username
	user.user.first_name = "Usuário"
	user.user.set_password(password)
	user.save()

@step(r'I register the booking "(.*)" with the building "(.*)" with the place name "(.*)" and start_date "(.*)" and end_date "(.*)" of user "(.*)"')
def new_booking(step, booking_name, building, place_name, start_date, end_date, username):
	booking = Booking()
	booking.user = User()
	booking.user = User.objects.get(username=username)
	booking.name = booking_name
	booking.start_date = start_date
	booking.end_date = end_date
	booking.place = Place()
	booking.place.name = place_name
	booking.place.building = Building()
	booking.place.building.name = building
	booking.save()
	for day in range(0, 10):
		book = BookTime()
		book.date_booking = parser.parse(start_date) + timedelta(days=day)
		book.start_hour = "20:00"
		book.end_hour = "22:00"
		book.save()
		booking.time.add(book)
	booking.save()


@step(r'I login in with email "(.*)" and password "(.*)"')
def login_user(step, email, password):
	step.given("I visit site page \"/\"")
	c = Client()
	response = c.login(username=email, password=password)
	cookies = {}
	for co in c.cookies.values():
		cookies['name'] = co.key
		cookies['value'] = co.value
		world.browser.add_cookie(cookies)
	world.browser.refresh()

@step(r'I run loaddata to populate dropdowns')
def run_command_line(step):
	call_command('loaddata', 'buildings', 'places')
