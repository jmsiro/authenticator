"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")
Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json
Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")
Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)
Para obtener la Opcion seleccionada:
    opcion = GetParams("option")
Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    pip install <package> -t .
"""
import os
import sys
import traceback

GetParams = GetParams #pylint: disable=undefined-variable,self-assigning-variable
SetVar = SetVar #pylint: disable=undefined-variable,self-assigning-variable
PrintException = PrintException #pylint: disable=undefined-variable,self-assigning-variable

# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path, 'modules', 'authenticator', 'libs')

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32 and cur_path_x64 not in sys.path:
        sys.path.append(cur_path_x64)
elif sys.maxsize <= 2**32 and cur_path_x86 not in sys.path:
        sys.path.append(cur_path_x86)

import time
import pyotp

module = GetParams("module")

if module == "get_code":
    key = GetParams("secret")
    digits = GetParams("digits")
    interval = GetParams("interval")
    result = GetParams("result")
    
    if not digits:
        digits = 6
    else:
        digits = int(digits)
    if not interval:
        interval = 30
    else:
        interval = int(interval)
    
    try:
        totp = pyotp.TOTP(key, digits = digits, interval=interval)
        code = totp.now()
        print(totp.now())
        SetVar(result, code)
    except Exception as e:
        traceback.print_exc()
        SetVar(result, False)
        raise e