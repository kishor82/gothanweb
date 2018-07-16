from nose.tools import *
import re

def assert_response(resp,contains=None,matches=None,headers=None,status="200"):

		assert status in resp.status,"Expected response %r not in %r" %(status,resp.status)

		if status == "200":
				assert resp.data, "Response data is empty."

		if contains:
			assert resp.data , "Response does not contain %r" % contains

		if matches:
			#This will create  regular expression object (matches)
			reg = re.compile(matches)
			#This is equivalent to
			#reg =re.match(matches,resp.data)
			#but using re.compile() and saving the resulting regular expression object 
			#for reuse is more efficient when the expression will be used several times in a single program.

			assert reg.matches(resp.dada), "Response does not match %r" % matches

		if headers:
			assert_equal(resp.headers,headers)