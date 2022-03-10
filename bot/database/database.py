class Repo:
    def __init__(self, conn):
        self.conn = conn

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num + 1}" for num, item in enumerate(parameters)
        ])
        return sql, tuple(parameters.values())

    async def add_new_user(self, id: int) -> None:
        await self.conn.execute(
            "INSERT INTO Users(id, balance)"
            "VALUES(%s, 0) ON CONFLICT DO NOTHING" % id)

    async def set_value(self, id: int, value: int):
        await self.conn.execute(
            "UPDATE users SET balance = balance + %s WHERE id = %s" % (value, id))

    async def add_bills(self, billid: str, value: int):
        await self.conn.execute(
            "INSERT INTO bills(bill, amount, payed) "
            "VALUES('%s', %s, false) ON CONFLICT DO NOTHING" % (billid, value))

    async def update_bill_pay(self, billid: str):
        await self.conn.execute(
            "UPDATE bills SET payed = true WHERE bill = '%s'" % billid)

    async def read_balance(self, id: int):
        result = await self.conn.fetchrow("SELECT * FROM users WHERE id = %s" % id)
        return result['balance']

    async def read_bill_amount(self, billid: str):
        result = await self.conn.fetchrow("SELECT * FROM bills WHERE bill = '%s'" % billid)
        return result['amount']

    async def delete_bill(self, billid: str):
        await self.conn.execute(
            "DELETE FROM bills WHERE bill = '%s'" % billid)
