import database_operation

resultado = database_operation.insert(53221, "usuario@email.com", "auto")

if resultado:
    print("✅ Série inserida com sucesso!")
else:
    print("❌ Falha na inserção.")