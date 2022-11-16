# Crypto-Systems_-2nd-yr-
Three crypto systems(2nd yr)

			                      	----INSTRUCTIONS----

After the program is run, the code will ask the user to enter/insert the string to be encrypted/decrypted
via the python console. After the user enters the string, the program will ask the user to Choose the type 
of cryptosystem to run from given alternatives i.e affine, transposition and RSA. The user replies to it 
using the integers 1, 2, 3 coresponding to the above cryptosystems respectively. Next, the user will be 
required to choose mode i.e. encryption/decryption.

	I. If the user has chosen 1(affine): To encrypt a string the user must provide encryption keys a, b which are 
		in the set {0, 1, ...25} and gcd(a,26)=1 and then the encrypted text will be printed out to the screen.

		=> For decrypting an affine cipher, the user must provide the keys used for encrypting the cipher and the
		decrypted text will be printed out.

	II. If the user has chosen 2(transposition): To encrypt a string message the user has to enter a key and the 
		encrypted text will be printed out.

		=> For decryption the key is needed and the decrypted string will be printed out.

	III. If the user has chosen RSA(3): For encryption the user will be asked to enter the first and the second 
		primes(higher primes are better though they need higher CPU) which are then used to generate the public and 
		private keys. Both the keys are printed out to the screen for the user to use it. The program will encrypt the 
		string(might contain characters and numbers as well) using the public key and print it out.
		
		=> For decryption the user is required to enter the private key and the program will decrypt it using the
		private key and print the text out.
Theorems and/or concepts used: Number theory; Euclid's Algorithm(GCD), fermat's little theorem, Modular Arithmethic, congruences
Affine cipher :encryption is accomplished using key (α, β) via the formula y ≡ αx + β (mod 26)  where α, β ∈ {0, 1, . . . , 25} and 
	gcd(α, 26) = 1. S =18  then 3 · 18 + 7 ≡ 9 (mod 26) gives J with encryption Key k=(α, β ) α=3 and β = 7.
	Decryption is accomplished Using  key (α, β) via the formula  ( x ≡ α^-1(c −  β ) (mod 26).
	The affine cipher encryption/decryption works fine but if someone can find the plaintext of two ciphertext characters, 
	they can solve simultaneous equation to find the key.
Transposition cipher:Character positions in plain text are changed via the transposition cipher technique. The position of the 
	character is altered but the identity of the character is preserved.
	 It is done by writing the message in rows , then forming encrypted messagefrom the text in the columns.
	 We create rectangle in which the size is decided on the senders and receiver. Sender write plain text row by
	 row and cipher text is generated (read) in column by column form to decrypt. Here the most important thing 
	is key it tells which column is read first.
The transposition cipher holds a significant improvement in crypto security than affine cipher.

RSA cipher:  The first step of encrypting a message with RSA is to generate the keys. First we have to select 2 prime numbers p and, q. 
second calculate n = p * q . Third calculate $ = (p -1 ) * (  q – 1 ). fourth, select e, as relative prime to $  gcd ( e, $(n) ) = 1  and 1 < e < $(n) 
Here e becomes public key for the algorithm then calculate d which is private key D = e^-1 mod $(n) or ed = 1 mod  , then d = (($(n) * i) + 1) $(n)
Then public key  =( e, n) Private key ( d, n )
For encryption we use the formula  C = P^e mod n, where p < n, C is assigned for cipher text , p for plain text, and e for encryption key and n to block size.
Then this is send to the receiver side.For decryption We use the formula P = C ^d mod n , where d is decryption key. Here we get original message after decryption at receiver side. 
After this we can implement both encryption and decryption well through the above process.

And encryption/decryption with RSA works best 
	so far of the three because their characteristics make it possible to exchange public keys without compromising the message or disclosing the 
	secret/private key. Additionally, they enable data to be encrypted with a single key in a fashion that can only be unlocked using 
	the second key in the pair.








