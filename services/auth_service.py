from typing import Annotated
from fastapi import Depends, HTTPException
from starlette import status
from schemas.user import User
from router.cards import oauth2_scheme

fake_db = {
    "allan" : {
        'full_name': 'allan le lay',
        'email': 'allan@lelay-zaibatsu.fr',
        'hashed_password': 'totofake_hashed',
    },
    "charlotte" : {
        'full_name': 'charlotte de choudens',
        'email': 'charlotte.dechoudens@laposte.net',
        'hashed_password': 'tatafake_hashed'
    }
}

#On lui donne le token et on extrait le user du token
def fake_decode_token(token):
    return User(email="test@email.com",
                hashed_password="totofake_hashed",
                full_name=token + "fake_decoded_token"
                )

#Sert à transformer le password du form pour s'adapter au hashed_password en db
def fake_hash_password(password):
    return password + "fake_hashed"

#On retourne le user extrait du token si trouvé, si non une erreur
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,)
    return user

async def create_token(username, password):
    #verifier que le user existe en DB
    user = fake_db.get(username)
    user = User(**user)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Username does not exist")
    #verifier que le mdp est le bon
    hashed_password = fake_hash_password(password)
    if user.hashed_password != hashed_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password, provided :"  + hashed_password + " / Expected " + user.hashed_password)
    #Generer le token & renvoyer le token
    return {"access token" : user.full_name, "type" : "Baerer"}