# Copyright (C) 2018 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

"""Handlers for list type values."""

from ggrc.converters.handlers import handlers


class ValueListHandler(handlers.ColumnHandler):
  """Handler for cells where the content represents a list of values.

  This column handler will take a comma or new line separated values and turn
  it into a comma separated values. It should be used only for simple strings
  and can be later converted into json column handler.
  """

  def parse_item(self):
    values = self.raw_value.replace(",", "\n").splitlines()
    return ",".join(value.strip() for value in values if value.strip())
