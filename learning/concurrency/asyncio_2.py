import asyncio
from  contextlib import asynccontextmanager
import shlex

async def main(cmd):

    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await asyncio.wait_for(proc.communicate(),timeout=5.0)

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')


    proc2 = await asyncio.create_subprocess_exec(
        *shlex.split(cmd),
        stdout = asyncio.subprocess.PIPE,
        stderr = asyncio.subprocess.PIPE
    )
    stdout , stderr = await asyncio.wait_for(proc2.communicate(),timeout=1.0)
    print(f'[{cmd!r} exited with return code {proc2.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')


asyncio.run(main('ls -al'))
##This commands times out
#asyncio.run(main('find / -type f -name asyncio_2.py'))
