#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2023 Pynguin Contributors
#
#  SPDX-License-Identifier: LGPL-3.0-or-later
#
from tests.fixtures.cluster.diamond_bottom import FooBar
from tests.fixtures.cluster.diamond_bottom import foo


def foobar():
    foo()
    FooBar()
