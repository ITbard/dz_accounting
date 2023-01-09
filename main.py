from package.application.salary import *
from package.application.db.people import *
import datetime
import nectarine
if __name__ == '__main__':
    calculate_salary()
    get_employees()
    # dt_now = datetime.datetime.now()
    # print(dt_now)
    current_date = datetime.date.today()
    print(current_date)
