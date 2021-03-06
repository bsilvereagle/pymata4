"""
 Copyright (c) 2020 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import sys

from pymata4 import pymata4

"""
This example retrieves the Pymata4 version, which consists
of the major and minor version numbers.
"""


def retrieve_pymata_version(my_board):
    """

    :param my_board: pymata_express instance
    :return: the pymata version
    """
    print(my_board.get_pymata_version())


board = pymata4.Pymata4()
try:
    retrieve_pymata_version(board)
    board.shutdown()
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
