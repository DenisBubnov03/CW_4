from flask import abort


class BaseServices:
    def __init__(self, dao):
        self.dao = dao

    def get_by_id(self, pk):
        item = self.dao.get_by_id(pk)
        if not item:
            abort(404)
        return item

    def get_all(self, page, status=None):
        """get all items"""
        items = self.dao.get_all(page, status)
        if not items:
            abort(404)
        return items

    def create(self, data):
        return self.dao.create(data)
