from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    LOCKED = "LOCKED"
    PROVISIONAL = "PROVISIONAL"
    DEVELOPMENT = "DEVELOPMENT_COMPONENT"
    PURCHASE_DEPENDENT = "PURCHASE-DEPENDENT"


@dataclass(frozen=True)
class PartMeta:
    part_number: str
    name: str
    material: str
    food_contact: bool
    status: Status


PARTS = {
    "A01-001": PartMeta("A01-001", "base pan", "SS304", False, Status.PROVISIONAL),
    "A01-003": PartMeta("A01-003", "sanitary partition", "SS304", False, Status.LOCKED),
    "A02-001": PartMeta("A02-001", "hopper shell", "SS304", True, Status.PROVISIONAL),
    "A04-004": PartMeta("A04-004", "feeder paddles", "POM_FOOD", True, Status.DEVELOPMENT),
    "A07-C34": PartMeta("A07-C34", "C34 lower cartridge", "POM_FOOD", True, Status.DEVELOPMENT),
    "A08-C34": PartMeta("A08-C34", "C34 upper cartridge", "POM_FOOD", True, Status.DEVELOPMENT),
}
