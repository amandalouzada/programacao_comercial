from django.contrib.auth.mixins import UserPassesTestMixin

class ParticipanteMixin(UserPassesTestMixin):
    """
    CBV Mixin that allows you to define a test function which must return True
    if the current user can access the view.
    """

    def test_func(self):
        return self.request.user.is_staff

    def get_test_func(self):
        """
        Override this method to use a different test_func method.
        """
        return self.test_func

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        print(user_test_result)
        if not user_test_result:
            return self.handle_no_permission()
        return super(UserPassesTestMixin, self).dispatch(request, *args, **kwargs)
