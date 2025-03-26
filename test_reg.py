from student_register import register
def test_register():
    assert register('name','email_id','passwd') == list['abc','email_id','12345']