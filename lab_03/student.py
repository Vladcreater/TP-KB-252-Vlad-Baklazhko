class Student:
    def __init__(self, name: str, phone: str) -> None:
        name = name.strip()
        phone = phone.strip()
        if not name or not phone:
            raise ValueError("Ім'я та номер телефону не можуть бути порожніми.")
        self.name = name
        self.phone = phone

    def update_phone(self, new_phone: str) -> None:
        new_phone = new_phone.strip()
        if not new_phone:
            raise ValueError("Новий номер телефону не може бути порожнім.")
        self.phone = new_phone

    def to_dict(self) -> dict[str, str]:
        return {"Name": self.name, "Phone": self.phone}

    def __str__(self) -> str:
        return f"Ім'я: {self.name} | Телефон: {self.phone}"

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, phone={self.phone!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return (
            self.name.lower() == other.name.lower()
            and self.phone.strip() == other.phone.strip()
        )