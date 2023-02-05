import unittest


class SignupTest(unittest.TestCase):
    def test_signupEmail(self):
        print("this is signup by email test")
        self.assertTrue(True)

    def test_signupFacebook(self):
        print("this is signup by facebook test")
        self.assertTrue(False)

    def test_signupTwitter(self):
        print("this is signup by twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
