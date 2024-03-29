from project.models import User

def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email and password_hashed fileds are defined correctly
    """
    assert new_user.password_hashed != '12341234'
    assert new_user.email == 'admin@admin.com'
    assert new_user.phone == '01011111111'
