from datetime import datetime

from commits import generate_commits, skip_nights


def test_generate_commits():
    start_time = datetime(year=2018,month=4,day=3,hour=9)
    commits = generate_commits(100, start_time, min_interval=5,max_interval=30)
    assert len(commits) == 100
    assert commits[0].name == "#001"
    assert commits[0].time == start_time
    assert commits[-1].name == "#100"


def test_generate_commits_during_working_hours():
    start_time = datetime(year=2018,month=4,day=3,hour=17, minute=59)
    commits = generate_commits(2, start_time, min_interval=5,max_interval=30)
    assert start_time < commits[1].time
    assert commits[1].time > datetime(year=2018,month=4,day=4,hour=8)


def test_skip_nights():
    start_time = datetime(year=2018,month=4,day=3,hour=18)
    next_time = skip_nights(start_time, 8, 18)
    assert next_time == datetime(year=2018, month=4, day=4, hour=8)

