from django.contrib.auth.models import Group, Permission, User

class Configuration():


	def get_permission(self, name):
		permissions = Permission.objects.filter(codename=name)
		if permissions.count() > 0:
			return permissions[0]
		
		return None
		

	def create_groups(self):
		admin, created = Group.objects.get_or_create(name="admin")
		permission1 = self.get_permission(name = "delete_booking")
		admin.permissions.add(permission1)	
		permission2 = self.get_permission(name = "add_booking")
		admin.permissions.add(permission2)
		permission3 = self.get_permission(name = "change_booking")
		admin.permissions.add(permission3)
		permission4 = self.get_permission(name = "delete_userprofile")
		admin.permissions.add(permission4)	
		permission5 = self.get_permission(name = "add_userprofile")
		admin.permissions.add(permission5)
		permission6 = self.get_permission(name = "change_userprofile")
		admin.permissions.add(permission6)
		permission7 = self.get_permission(name = "delete_user")
		admin.permissions.add(permission7)	
		permission8 = self.get_permission(name = "add_user")
		admin.permissions.add(permission8)
		permission9 = self.get_permission(name = "change_user")
		admin.permissions.add(permission9)
		permission10 = self.get_permission(name = "delete_place")
		admin.permissions.add(permission10)	
		permission11 = self.get_permission(name = "add_place")
		admin.permissions.add(permission11)
		permission12 = self.get_permission(name = "change_place")
		admin.permissions.add(permission12)
		admin.save()
		academic_staff, created = Group.objects.get_or_create(name="academic_staff")
		academic_staff.permissions.add(permission2)
		academic_staff.permissions.add(permission3)
		academic_staff.permissions.add(permission4)
		academic_staff.permissions.add(permission5)
		academic_staff.permissions.add(permission6)
		academic_staff.permissions.add(permission7)
		academic_staff.permissions.add(permission8)
		academic_staff.permissions.add(permission9)
		academic_staff.save()
