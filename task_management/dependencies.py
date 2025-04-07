import requests
from fastapi import HTTPException,Request

# def is_authenticated(req: Request):
#     print("http://"+config.USER_API_URL+"/auth/validate")
#     try:
#         response = requests.get(
#             "http://"+config.USER_API_URL+"/auth/validate",
#             headers={"Authorization": req.headers.get("Authorization")}
#         )
#         if response.status_code != 200:
#             raise HTTPException(status_code=401, detail="Invalid token")
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         raise HTTPException(
#             status_code=503,
#             detail=f"Authentication service unavailable: {str(e)}"
#         )

def is_authenticated(req: Request):
    print(req.headers)
    if req.headers.get("X-User-ID"):
        return req.headers.get("X-User-ID")
    else:
        raise HTTPException(status_code=401, detail="Unauthenticated")