from django import forms
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# 작성자 : 김성우
# 내용 : 유저 생성 폼
# 최초 작성일 :23년6월7일
# 업데이트 일자 :23년6월7일
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# 작성자 : 김성우
# 내용 : 유저 수정 폼
# 최초 작성일 :23년6월7일
# 업데이트 일자 :23년6월7일
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()
    # 유저 정보들을 수정할 때에 패스워드는 해싱되어, 오로지 읽기만 가능하도록 합니다.
    class Meta:
        model = User
        fields = ["password", "is_active", "is_admin"]
