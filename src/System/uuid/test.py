import uuid

MOBO_UUID = str(uuid.UUID(int=uuid.getnode()))

print(MOBO_UUID)
print(MOBO_UUID.split('-')[-1])
print(bytes(MOBO_UUID,'utf-8')[-32:])

UNIQUE_ID = str(uuid.getnode())
print(UNIQUE_ID)