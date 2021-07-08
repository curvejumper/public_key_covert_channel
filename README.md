# public_key_covert_channel
The group will be creating a covert channel that uses public keys to transmit information during secure handshake processes. 
The channel will be developed to as closely as possible mimic the types of ambient key exchanges a network administrator might expect to see frequently occurring, thus minimizing the threat of detection. This project will include the implementation of the channel, from both the sender and receiver side, a discussion of its capabilities in terms of bandwidth and robustness, and analysis of possible prevention or detection.

## Outline
The project will have the following parts to send and receive the covert channel over a Public Key handshake.

1. A client which can send a covert channel
   - The client will create a RSA key exchange
   - The client will manipulate the key or the handshake packet with a covert message
   - The client will send the key exchange to a server

2. A server which can receive the covert channel
   - The server will listen for RSA key exchange protocols on the system
   - The server will grab any packets that are flagged with the covert channels signature
   - The server will decode the secret covert channel

## Other Questions
- How are we planning to evade any active wardens?

- Can any one easily identify from failed handshakes that, if there is some thing wrong, in that case can we establish the handshake itself? and then terminate the connection?

- Can we start again for sending further messages,

- Can we randomize such connections, so that it will be similar to any other connection attempts / number of connections?