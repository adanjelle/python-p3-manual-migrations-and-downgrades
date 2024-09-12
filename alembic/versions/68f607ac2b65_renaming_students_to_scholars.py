"""Renaming students to scholars

Revision ID: 68f607ac2b65
Revises: 
Create Date: 2024-09-12 10:33:22.039767

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68f607ac2b65'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
