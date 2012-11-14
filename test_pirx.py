#!/usr/bin/env python

import unittest
import tempfile
import subprocess
import os

class PirxTest(unittest.TestCase):

    def setUp(self):
        print "Setup: creating temp directory with sample files"
        self.path = tempfile.mkdtemp()
        self.filelist = ['DSC0001 123.jpg', 'DSC1234 145.JPG', 'DSC0002 122.jpg', 'simple2.AVI', 'simple1.avi']
        min = 10
        for file in self.filelist:
            filename = "%s/%s" % (self.path,file)
            # create file
            with open(filename,'w') as f:
                f.write("")
            # set modification time
            subprocess.call(["touch", "-m", "-t", "073019%d"%min, filename])
            min += 1
        print "\nSetup: List of files sorted by name"
        subprocess.call(["ls", "-l", self.path])
        print "\nSetup: List of files sorted by modification time in reverse order"
        subprocess.call(["ls", "-lrt", self.path])
        print "\n" 

    def _tell_me_true(self,check_cmd=['ls']):
        process = subprocess.Popen(check_cmd, cwd=self.path, stdout=subprocess.PIPE)
        out, err = process.communicate()
        return out.split("\n")[:-1]

    def _run_pirx(self,opt):
        # get script_path and add run options
        pirx_run = ["%s/%s" % (os.getcwd(),"pirx")] + opt
        process = subprocess.Popen(pirx_run, cwd=self.path, stdout=subprocess.PIPE)
        out, err = process.communicate()

    def test_default_settings(self):
        """pirx -v roadtrip --> Test default settings (sorted_by_name, basic_filtr)"""
        expected_output = ['roadtrip00001.jpg', 'roadtrip00002.jpg', 'roadtrip00003.JPG', 'simple1.avi', 'simple2.AVI']
        self._run_pirx(["-v","roadtrip"])
        self.assertEqual(self._tell_me_true(), expected_output, "script with default settings not work")

    def tearDown(self):
        # remove temp directory
        subprocess.call(["rm","-rf",self.path])


if __name__ == '__main__':
    unittest.main()
