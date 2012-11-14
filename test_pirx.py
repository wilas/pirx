#!/usr/bin/env python

import unittest
import tempfile
import subprocess
import os

class PirxTest(unittest.TestCase):

    def setUp(self):
        # creating temp directory with sample files
        self.path = tempfile.mkdtemp()
        DEBUG = False
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
        if DEBUG:
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
        """pirx -v roadtrip --> Default settings: sorted_by_name, basic_filtr"""
        expected_output = ['roadtrip00001.jpg', 'roadtrip00002.jpg', 'roadtrip00003.JPG', 'simple1.avi', 'simple2.AVI']
        self._run_pirx(["-v","roadtrip"])
        self.assertEqual(self._tell_me_true(), expected_output, "script with default settings not work")
    
    def test_sorted_by_time_reverse(self):
        """pirx -vt roadtrip --> Settings: sorted_by_time_in_reverse_order, basic_filtr"""
        expected_output = ['roadtrip00001.jpg', 'roadtrip00002.JPG', 'roadtrip00003.jpg', 'simple1.avi', 'simple2.AVI']
        self._run_pirx(["-vt","roadtrip"])
        self.assertEqual(self._tell_me_true(), expected_output, "script with sorting by time in reverse order not work")

    def test_set_output_file_extension(self):
        """pirx -v roadtrip -o jpg --> Settings: sorted_by_name, set_output_ext"""
        expected_output = ['roadtrip00001.jpg', 'roadtrip00002.jpg', 'roadtrip00003.jpg', 'simple1.avi', 'simple2.AVI']
        self._run_pirx(["-v","roadtrip","-o","jpg"])
        self.assertEqual(self._tell_me_true(), expected_output, "script with setting output extension not work")
    
    def test_set_extra_input_file_extension(self):
        """pirx -v roadtrip -i avi --> Settings: sorted_by_name, set_extra_input_ext"""
        expected_output = ['roadtrip00001.jpg', 'roadtrip00002.jpg', 'roadtrip00003.JPG', 'roadtrip00004.avi', 'simple2.AVI']
        self._run_pirx(["-v","roadtrip","-i","avi"])
        self.assertEqual(self._tell_me_true(), expected_output, "script with setting extra input extension not work")
    
    def test_set_extra_input_output_file_extension_and_use_pattern(self):
        """pirx -v -i avi|.AVI -p simple -o avi roadtrip --> sorted_by_name, set_extra_input_ext, set_output_ext, use_pattern"""
        expected_output = ['DSC0001 123.jpg', 'DSC0002 122.jpg', 'DSC1234 145.JPG', 'roadtrip00001.avi', 'roadtrip00002.avi']
        self._run_pirx(["-v","-i","avi|.AVI","-p","simple","-o","avi","roadtrip"])
        self.assertEqual(self._tell_me_true(), expected_output, "script with setting extra input, output extension and match pattern not work")
    
    def test_replace_space(self):
        """pirx -vb _ --> replace spaces with _"""
        expected_output = ['DSC0001_123.jpg', 'DSC0002_122.jpg', 'DSC1234_145.JPG', 'simple1.avi', 'simple2.AVI']
        self._run_pirx(["-vb","_"])
        self.assertEqual(self._tell_me_true(), expected_output, "script with replacing spaces not work")
    
    def tearDown(self):
        # remove temp directory
        subprocess.call(["rm","-rf",self.path])


if __name__ == '__main__':
    unittest.main()
