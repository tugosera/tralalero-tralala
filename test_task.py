from task import task 

def test_mark_done():
    task = task("Testi ülesanne")
    task.mark_done()
    assert task.status == "done"