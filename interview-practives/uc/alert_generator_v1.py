import yaml
import asyncio

from utils import parse_config
from rule_engine import run_engine


if  __name__ == '__main__':
    conf = parse_config()

    asyncio.run(run_engine(conf))
