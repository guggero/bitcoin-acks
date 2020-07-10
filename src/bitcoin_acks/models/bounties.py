from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from bitcoin_acks.database.base import Base
from bitcoin_acks.models import PullRequests
from bitcoin_acks.models.users import Users


class Bounties(Base):
    __tablename__ = 'bounties'

    id = Column(String, primary_key=True)

    amount = Column(Integer)

    published_at = Column(DateTime(timezone=True), nullable=False)

    pull_request_id = Column(String,
                             ForeignKey('pull_requests.id'),
                             nullable=False)

    pull_request = relationship(PullRequests, backref='bounties')

    recipient_user_id = Column(String)
    recipient = relationship(Users,
                             primaryjoin=recipient_user_id == Users.id,
                             foreign_keys='[Invoices.recipient_user_id]',
                             backref='invoices_receivable'
                             )

    payer_user_id = Column(String)
    payer = relationship(Users,
                         primaryjoin=payer_user_id == Users.id,
                         foreign_keys='[Invoices.payer_user_id]',
                         backref='invoices_payable'
                         )
