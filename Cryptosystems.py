'''
_____SECTION 3_____
Group members
Abraham Wendmeneh...UGR/9155/13
Biruktawit Abera....UGR/9634/13 
Ebissa Chemeda......UGR/1032/13
Esayas Nigussie.....UGR/5132/13
'''


import math, random
class affine:
    def __init__(self, key1,key2,string):
        self.key1=key1
        self.key2=key2
        self.text=string
        self.cipher=""
        self.plain_text=""
    def encrypt(self):
        # An affine cipher is an example of a substitution cipher
        # each time a given letter occurs in the plaintext 
        # it always is replaced by the same ciphertext letter
        for letter in self.text:
            if letter != " ":    
                if ord(letter)<96:
                    self.cipher += chr(( self.key1*(ord(letter)-65) + self.key2) % 26 + 65)
                else:
                    self.cipher += chr(((self.key1*(ord(letter)-97) + self.key2) %26) + 97)
            else:
                self.cipher += letter
        print("Encrypted text is: ", self.cipher)
        
    def decrypt(self):
        for x in range(1,26):
            if (self.key1 * x) % 26 == 1:
                self.key1 = x
        for letter in self.text:
            if letter != " ": 
                if letter.isupper():
                    self.plain_text += chr((self.key1*(ord(letter) + 65 - self.key2)) % 26 +65)
                else:
                    self.plain_text += chr((self.key1 * (ord(letter) - self.key2- 97 + 26)) % 26 + 97)
            else:
                self.plain_text += letter
        print("Decrypted text is: ", self.plain_text)

# =============================================================================


class transposition:
    
    def __init__(self, key, string):
        self.key = key
        self.text = string
    def encrypt(self):
        ciphertext = [''] * self.key
        # Loop through each column in ciphertext.
        for col in range(self.key):
            pointer = col
            # Keep looping until pointer goes past the length of the message.
            while pointer < len(self.text): 
                ciphertext[col] += self.text[pointer] 
                pointer += self.key
        print(''.join(ciphertext))
        
    def decrypt(self):
        # The transposition decrypt function will simulate the "columns" and
        # "rows" of the grid that the plaintext is written on by using a list  
        # of strings. First, we need to calculate a few values. 
        
        # The number of "columns" in our transposition grid: 
        numOfColumns = math.ceil(len(self.text) / self.key) 
        # The number of "rows" in our grid will need: 
        numOfRows = self.key 
        # The number of "empty boxes" in the last "column" of the grid
        numOfEmptyBoxes = (numOfColumns * numOfRows) - len(self.text) 
        
        # Each string in plaintext represents a column in the grid. 
        plaintext = [''] * numOfColumns 
        # The col and row variables point to where in the grid the next 
        # character in the encrypted message will go.
        col = 0
        row = 0
        
        for symbol in self.text:
            plaintext[col] += symbol 
            col += 1
            # If there are no more columns OR we're at an empty box, go back to
            # the first column and the next row.
            if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfEmptyBoxes):
                col = 0 
                row += 1
        print(''.join(plaintext))
#=====================================================================================



class RSA:
    def __init__(self, p, q, string):
        self.p = p
        self.q = q
        self.text = string
        
    def encrypt(self):
        def is_prime(num):
            if num == 2:
                return True
            if num < 2 or num % 2 == 0:
                return False
            for n in range(3, int(num**0.5)+2, 2):
                if num % n == 0:
                    return False
            return True
        
        def gcd(a, b):
            # this is Euclid's Algorithm to find gcd
            while b != 0:
                a, b = b, a % b
            return a
        
        def multiplicative_inverse(e, phi):
            # this will be used to find the multiplicative inverses in modular arithmetic
            d, num1 = 0, 0
            num2, y1 = 1, 1
            temp_phi = phi
            while e > 0:
                temp1 = temp_phi//e
                temp2 = temp_phi - temp1 * e
                temp_phi = e
                e = temp2
                num = num2- temp1* num1
                y = d - temp1 * y1
                num2, num1 = num1, num
                d, y1= y1, y
            if temp_phi == 1:
                return d + phi
            
            
        if not (is_prime(self.p) and is_prime(self.q)):
            raise ValueError('Both numbers must be prime.')
        elif self.p == self.q:
            raise ValueError('p and q cannot be equal')
        n = self.p * self.q
        phi = (self.p-1)*(self.q-1)
        
        #Choose an integer e such that e and phi(n) are coprime
        e = random.randrange(1, phi)
        
        #Use Euclid's Algorithm to verify copprimes for e and phi(n)
        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)
        d = multiplicative_inverse(e, phi)
        #Public key is (e, n) and private key is (d, n)
        public, private = ((e, n), (d, n))
        print ("\nYour public key is {} and your private key is {}\n".format(public, private))
        key, n = public
        #Convert each letter in the plaintext to numbers based on the character using a^b mod m
        cipher = [(ord(char) ** key) % n for char in self.text]
        print ("Your encrypted message is: {}".format(' '.join(map(lambda x:str(x), cipher))))
        # we used the map function to join the list of numbers separated by a space so that 
        # they can also be decrypted using the private key at later time if needed
        
    def decrypt(pvk1, pvk2, cipher):
        #takes in the previously generated private key(d, e) to decrypt the cipher
        list = str(cipher).split(" ")
        ciphertext = map(int, list)
        key, n = pvk1, pvk2
        plain = [chr((char ** key) % n) for char in ciphertext]
        #Return the array of bytes as a string
        print(''.join(plain))
        
        
        

def main():
    text = input("Enter the message to be encrypted/decrypted: \n =>")
    ctype = int(input("Choose the type of cryptosystem to run; \n 1.Affine \n 2.Transposition \n 3.RSA \n =>"))
    if ctype not in [1,2,3]:
        raise ValueError("Please enter from the given choices")
    mode = int(input("Choose mode; \n 1.Encryption \n 2.Decryption \n =>"))
    
    if ctype == 1:
        if mode == 1:
            a = int(input("Enter the first key, a: "))
            b = int(input("Enter the second key, b: "))
            affine(a,b,text).encrypt()
        
        else:
            a = int(input("Enter the first key, a: "))
            b = int(input("Enter the second key, b: "))
            affine (a,b, text).decrypt()
            
    elif ctype == 2:
        if mode == 1:
            a = int(input("Enter the key: "))
            transposition(a, text).encrypt()
        else:
            a = int(input("Enter the key: "))
            transposition(a, text).decrypt()
            
    else :
        if mode == 1:
            p = int(input("Enter the first prime number, p : "))
            q = int(input("Enter the second prime number, q : "))
            RSA(p, q, text).encrypt()
        else:
            pvk1 = int(input("Enter the first private key, pvk1: "))
            pvk2 = int(input("Enter the second private key, pvk2: "))
            RSA.decrypt(pvk1, pvk2, text)
        
        
if __name__=='__main__':
    main()
    