# Copyright (C) 2018 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

"""This module contains 'modified_by' filter test classes definition."""
from api_search.test_person_filters_complete import generate_classes
from ggrc.snapshotter.rules import Types


generate_classes(Types.all, "modified_by")
