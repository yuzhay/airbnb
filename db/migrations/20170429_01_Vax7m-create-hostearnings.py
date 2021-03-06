"""
Create HostEarnings
"""

from yoyo import step

__depends__ = {'20170428_01_SiUGE-create-hostactivities'}

steps = [
    step(
        """CREATE TABLE host_earnings(
            year                integer NOT NULL,
            month               integer NOT NULL,
            cancellation_fees   integer NOT NULL,
            cohosting_earnings  integer NOT NULL,
            paid_out            integer NOT NULL,
            pending             integer NOT NULL,
            total               integer NOT NULL,

            updated_at  timestamp without time zone default (now() at time zone 'utc'),
            created_at  timestamp without time zone default (now() at time zone 'utc'),

            UNIQUE (year, month)
        )""",
        "DROP TABLE host_earnings")
]
