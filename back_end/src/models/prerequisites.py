from __future__ import annotations

from typing import List

from ..setup import db

from flask_login import UserMixin



class Prerequisites(db.Model, UserMixin):
    __tablename__ = "Prerequisites"

    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, primary_key = True, db.ForeignKey('AllClasses.id'), nullable=False)
    required_classes = db.Column(db.String(255), nullable=False, default='None')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def to_json(self):
        ret = {}
        ret['id'] = self.id
        ret['class_id'] = self.class_id
        ret['required_classes'] = self.required_classes
        return ret

    def update_attr(self, class_id: int, required_classes: str) -> bool:
        if class_id:
            self.class_id = class_id
        if required_classes:
            self.required_classes = required_classes
        return True

    def save(self):
        db.session.commit()

    @staticmethod
    def create_prereq(class_id: int, required_classes: str) -> bool:
        # This is a pre done thing before the app goes public
        if User.get_prereq_by_class_id(class_id=class_id):
            return False    # user exists
        prereq = Prerequisites(class_id=class_id, required_classes = required_classes)
        db.session.add(prereq)
        user.save()
        return True

    @staticmethod
    def get_prereqs() -> List[Prerequisites]:
        get_prereqs = Prerequisites.query.all()
        get_prereqs = list(map(lambda x: x.to_json(), get_prereqs))
        return get_prereqs

    @staticmethod
    def get_prereq_by_class_id(class_id: int) -> User:
        return Prerequisites.query.filter_by(class_id=class_id).first()

    @staticmethod
    def update_profile(user_id: int, first_name: str = None,
                       last_name: str = None,
                       user_name: str = None,
                       intended_grad_quarter: str = None,
                       college: str = None, major: str = None,
                       minor: str = None) -> bool:
        # TODO: Maybe we want to use **kwargs, but maybe not...
        usr = User.get_user_by_id(user_id=user_id)
        return usr.update_attr(first_name=first_name, user_name=user_name,
                               last_name=last_name, college=college,
                               intended_grad_quarter=intended_grad_quarter,
                               major=major, minor=minor)
