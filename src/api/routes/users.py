import json
from fastapi import APIRouter, Depends

from src.database.database import engine
from src.helper import redis_handler

router = APIRouter()


@router.get("/dump")
async def dump(ma_ddo: str):
    try:
        data = {
            'ma_khang': 'PD05000131264',
            'evn_diem_do': {
                'ma_dviqly': 'PD0500',
                'loai_ddo': 1,
                'ma_capda': 1,
                'csuat': 10,
                'kimua_cspk': 0
            },
            'evn_bien_ban_ap_gia': [
                {
                    'loai_bcs': 'BT',
                    'tgian_bdien': 'BT',
                    'ma_nhomnn': 'SHBT',
                    'ma_ngia': 'A'
                },
                {
                    'loai_bcs': 'CD',
                    'tgian_bdien': 'CD',
                    'ma_nhomnn': 'SHBT',
                    'ma_ngia': 'A'
                },
                {
                    'loai_bcs': 'TD',
                    'tgian_bdien': 'TD',
                    'ma_nhomnn': 'SHBT',
                    'ma_ngia': 'A'
                }
            ]
        }
        data = json.dumps(data)
        redis_handler.dump_data(ma_ddo=ma_ddo, data=data)
        return {"status": "success", "msg": f"{ma_ddo}"}
    except Exception as e:
        return {"status": "error", "msg": f"{e}"}
    
@router.get("/load")
async def load(ma_ddo: str):
    try:
        data = redis_handler.load_data(ma_ddo=ma_ddo)
        data = json.loads(data)
        return {"status": "success", "msg": data}
    except Exception as e:
        return {"status": "error", "msg": f"{e}"}
    




# from typing_extensions import final
# from fastapi import APIRouter, Depends

# from src.database.database import engine
# from src.services import redis_handler

# router = APIRouter()


# @router.get("")
# async def get_users():
#     try:
#         connection = engine.raw_connection()
#         return {"status": f"success"}
#     except Exception as e:
#         connection.rollback()
#         return {"status": f"{e}"}
#     finally:
#         connection.close()