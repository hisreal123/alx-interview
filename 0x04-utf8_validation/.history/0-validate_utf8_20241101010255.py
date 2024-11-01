#!/usr/env/bin python3
""" UTF8 interview"""

def validUTF8(data):
  """Check if a byte array is valid UTF-8"""
  if not data:
    return False