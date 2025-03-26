from student_register import register
def test_register():
    assert register("name","email_id","passwd") == ("abc","abc@gmail.com","12345")