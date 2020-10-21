from typing import Any, Optional, Dict, List, Tuple, Iterator
from typing import NewType

__copyright__: str
logg: logging.Logger
MAX_PATH: int
MAX_NAME: int
MAX_PART: int
MAX_VERSION: int
TMPDIR: str
DOCKER: str
KEEPDIR: int
KEEPDATADIR: bool
KEEPSAVEFILE: bool
KEEPINPUTFILE: bool
KEEPOUTPUTFILE: bool
OK: bool
NULL: str
StringConfigs: Dict[str, str]
StringMeta: Dict[str, str]
StringCmd: Dict[str, str]

def sh(cmd: str = ..., shell: bool = ..., check: bool = ..., ok: Optional[bool] = ..., default: str = ...) -> Result: ...
def portprot(arg: str) -> Tuple[str, str]: ...

def podman() -> bool: ...
def cleans(text: str) -> str: ...
def os_jsonfile(filename: str) -> None: ...

class ImageName:
    registry: Optional[str] = ...
    image: str = ...
    version: Optional[str] = ...
    def __init__(self, image: str) -> None: ...
    def __str__(self) -> str: ...
    def parse(self, image: str) -> None: ...
    def tag(self) -> str: ...
    def valid(self) -> bool: ...
    def problems(self) -> Iterator[str]: ...

Commands = List[Tuple[str, Optional[str], Optional[str]]]
def edit_image(inp: Optional[str], out: Optional[str], edits: Commands) -> bool: ...
def edit_datadir(datadir: str, out: Optional[str], edits: Commands) -> int:
    replaced: Dict[str, Optional[str]]
    args: List[str]
    found: List[int]
def parsing(args: Any) -> Tuple[Optional[str], Optional[str], Commands]:
    commands: Commands

# def edit_image(inp: Optional[str], out: Optional[str], edits: List[Tuple[str, Optional[str], Optional[str]]]) -> None: ...
# def edit_datadir(datadir: str, out: Optional[str],     edits: List[Tuple[str, Optional[str], Optional[str]]]) -> int: ...
# def parsing(args: Any) -> Tuple[Optional[str], Optional[str], List[Tuple[str, Optional[str], Optional[str]]]]: ...

def docker_tag(inp: Optional[str], out: Optional[str]) -> None: ...
