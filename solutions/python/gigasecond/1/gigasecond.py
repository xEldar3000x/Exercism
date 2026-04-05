from datetime import timedelta, datetime

def add(moment):
    difference = timedelta(seconds = 1e9)
    end = moment + difference
    return end
