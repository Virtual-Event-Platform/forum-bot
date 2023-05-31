import ampalibe
from presentation.test_kavio import TestKavio 

testKavio = TestKavio()

@ampalibe.command('/test_kavio')
def test_kavio(sender_id, **ext):
    return testKavio.get_started(sender_id, **ext)

@ampalibe.command('/test_kavio/cancel')
async def test_kavio_cancel(sender_id, **ext):
    return await testKavio.cancel(sender_id, **ext)

@ampalibe.command('/test_kavio/part')
def test_kavio_start_part(sender_id, **ext):
    return testKavio.start_part(sender_id, **ext)

@ampalibe.command('/test_kavio/choice')
async def test_kavio_choice(sender_id, **ext):
    return await testKavio.choice(sender_id, **ext)


@ampalibe.command('/test_kavio/result')
def test_kavio_result(sender_id, **ext):
    return testKavio.result(sender_id, **ext)

@ampalibe.command('/test_kavio/continue')
async def test_kavio_continue(sender_id, **ext):
    return await testKavio.continue_test(sender_id, **ext)

@ampalibe.command('/test_kavio/restart')
def test_kavio_restart(sender_id, **ext):
    return testKavio.restart_test(sender_id, **ext)