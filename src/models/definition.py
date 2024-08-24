from enum import Enum

class Definition(Enum):
    REGULAR_32 = "SYSCALL32_DEFINE"
    REGULAR = "SYSCALL_DEFINE"
    COMPAT = "COMPAT_SYSCALL_DEFINE"
    PPC_32 = "PPC32_SYSCALL_DEFINE"
