from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import hashes

priv_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

pub_key = priv_key.public_key()

data_to_sign = b"Sample data to sign" # rsa expects bytes

def sign():
    signature = priv_key.sign(
        data_to_sign,
        padding.PSS( # adds randomness
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH # adds a salt
        ),
        hashes.SHA256()  # for security change to fixed size   
    )
    return signature

def verify(signed):
    try:
        pub_key.verify(
            signed,
            data_to_sign,
            padding.PSS( # adds randomness
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH# adds a salt
            ),
            hashes.SHA256() # for security change to fixed size
        )
        return True
    except:
        return False

signature = sign()
verified = verify(signature)
if (verified):
    print("Signature was verified")
else:
    print("Signature was not verified")