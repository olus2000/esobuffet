from .model import Session, init_db, File, Round, PLayer, Solution
from .templates import config_template, html_template

from datetime import datetime, timedelta
import configparser
import os


config = configparser.ConfigParser()


def init_round(round_num):

    session = Session()
    exists = session.query(Round).filter(id=round_num).one_or_none()
    if exists is not None:
        raise ValueError(round_num)

    if not os.path.exists(str(round_num)):
        os.mkdir(str(round_num))

    with open(f'{round_num}/config.cfg', 'w') as f:
        print(

    new_round = Round(id=round_num,
                      start=datetime.now(),
                      first_deadline=datetime.now() + timedelta(days=7),
    )
    
