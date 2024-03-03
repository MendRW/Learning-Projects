## Double split pattern
## split the line once, grab pieces of the line and split that piece again
## '@([^]*)' Look until the string until you find an @ sign, then match the non blank characters and then stop once you hit a blank character
## This means it'll start looking until it finds an @ sign and then start matching the characters until it encounters a blank character