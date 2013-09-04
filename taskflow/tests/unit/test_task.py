# -*- coding: utf-8 -*-

# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Copyright (C) 2013 Yahoo! Inc. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from taskflow import task
from taskflow import test


class MyTask(task.Task):
    def execute(self, context, spam, eggs):
        pass


class TaskTestCase(test.TestCase):

    def test_passed_name(self):
        my_task = MyTask(name='my name')
        self.assertEquals(my_task.name, 'my name')

    def test_generated_name(self):
        my_task = MyTask()
        self.assertEquals(my_task.name,
                          '%s.%s' % (__name__, 'MyTask'))

    def test_requirements_added(self):
        my_task = MyTask()
        self.assertEquals(my_task.requires, set(['spam', 'eggs']))

    def test_requirements_can_be_ignored(self):
        my_task = MyTask(requires_from_args=False)
        self.assertEquals(my_task.requires, set())