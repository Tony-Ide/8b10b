import encodecode as e
running_disp = 0
byte_to_enc = 0
encoded = e.EncDec_8B10B.enc_8b10b(byte_to_enc, running_disp)
print(bin(encoded))